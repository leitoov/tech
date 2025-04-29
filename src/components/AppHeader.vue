<template>
  <header
    :class="[
      'w-full flex justify-between items-center p-4 bg-nefe-beige-200 text-white transition-all duration-300 fixed top-0 left-0 z-50',
      isAtTop ? 'opacity-100' : 'opacity-90',
      isAtTop ? 'shadow-none' : 'shadow-md'
    ]"
  >
    <div class="flex items-center">
      <img src="@/assets/X2.png" alt="Logo NefeTech" class="h-10 w-auto" />
    </div>

    <!-- Menú de escritorio -->
    <nav class="hidden md:flex">
      <ul class="flex space-x-6 text-sm font-semibold">
        <li><a href="#inicio" @click="scrollToSection('inicio')" class="hover:text-nefe-gold-300 text-nefe-brown-600">Inicio</a></li>
        <li><a href="#servicios" @click="scrollToSection('servicios')" class="hover:text-nefe-gold-300 text-nefe-brown-600">Servicios</a></li>
        <li><a href="#quienes-somos" @click="scrollToSection('quienes-somos')" class="hover:text-nefe-gold-300 text-nefe-brown-600">Nosotros</a></li>
        <li><a href="#contacto" @click="scrollToSection('contacto')" class="hover:text-nefe-gold-300 text-nefe-brown-600">Contacto</a></li>
      </ul>
    </nav>

    <!-- Botón hamburguesa para menú móvil -->
    <button @click="toggleMenu" @click.stop="preventImmediateClose" class="md:hidden focus:outline-none">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-black" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
      </svg>
    </button>

    <!-- Menú móvil -->
    <div
      ref="mobileMenu"
      :class="['fixed top-0 right-0 h-full bg-nefe-beige-200 shadow-lg p-4 transform transition-transform duration-300', menuOpen ? 'translate-x-0' : 'translate-x-full']"
      class="w-64 md:hidden"
    >
      <button @click="menuOpen = false" class="absolute top-4 right-4 text-nefe-brown-600">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <ul class="flex flex-col space-y-4 text-sm font-semibold mt-10">
        <li><a href="#inicio" @click="scrollToSection('inicio')" class="hover:text-nefe-gold-300 text-nefe-brown-600 text-base">Inicio</a></li>
        <li><a href="#servicios" @click="scrollToSection('servicios')" class="hover:text-nefe-gold-300 text-nefe-brown-600 text-base">Servicios</a></li>
        <li><a href="#quienes-somos" @click="scrollToSection('quienes-somos')" class="hover:text-nefe-gold-300 text-nefe-brown-600 text-base">Nosotros</a></li>
        <li><a href="#contacto" @click="scrollToSection('contacto')" class="hover:text-nefe-gold-300 text-nefe-brown-600 text-base">Contacto</a></li>
      </ul>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const menuOpen = ref(false)
const isAtTop = ref(true)
const mobileMenu = ref(null)

// Función para manejar el scroll y verificar si estamos en el tope de la página
const handleScroll = () => {
  isAtTop.value = window.scrollY === 0
}

// Función para alternar el menú móvil
const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

// Función para cerrar el menú móvil al hacer clic fuera de él
const handleClickOutside = (event) => {
  if (menuOpen.value && mobileMenu.value && !mobileMenu.value.contains(event.target)) {
    menuOpen.value = false
  }
}

// Prevenir que el clic en el botón hamburguesa cierre el menú inmediatamente
const preventImmediateClose = (event) => {
  event.stopPropagation()
}

// Función para hacer scroll a una sección específica
const scrollToSection = (id) => {
  const section = document.getElementById(id)
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' })
  }
  menuOpen.value = false // Cerrar el menú móvil después de hacer scroll
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  document.addEventListener('click', handleClickOutside)
  handleScroll() // Verificar el estado inicial
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  document.removeEventListener('click', handleClickOutside)
})
</script>
