<template>
  <div class="min-h-screen flex flex-col overflow-x-hidden">
    <AppHeader />
    <main class="flex-grow pt-[64px]">
      <AppHero />
      <AppServicios />
      <AppQuienesSomos />
      <AppContacto />
    </main>
    <AppFooter />

    <a
      href="https://wa.me/5491122512775?text=Hola,%20quiero%20más%20información!"
      target="_blank"
      class="fixed bottom-4 right-4 bg-green-500 text-white rounded-full p-4 shadow-lg hover:bg-green-600 transition z-50"
      aria-label="Contactar por WhatsApp"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
        <path d="M20.52 3.48A11.94 11.94 0 0012 0a11.94 11.94 0 00-8.52 3.48A11.94 11.94 0 000 12c0 2.11.55 4.17 1.6 6.01L0 24l5.99-1.6A11.94 11.94 0 0012 24a11.94 11.94 0 008.52-3.48A11.94 11.94 0 0024 12a11.94 11.94 0 00-3.48-8.52zM12 22c-1.85 0-3.66-.5-5.24-1.44l-.38-.22-3.55.95.95-3.55-.22-.38A9.94 9.94 0 012 12c0-5.52 4.48-10 10-10s10 4.48 10 10-4.48 10-10 10zm5.27-7.73l-1.5-.43c-.2-.06-.42-.02-.58.11l-.7.56a6.27 6.27 0 01-3.03-3.03l.56-.7c.13-.16.17-.38.11-.58l-.43-1.5a.58.58 0 00-.56-.41h-1.5c-.31 0-.58.25-.58.56a7.94 7.94 0 007.94 7.94c.31 0 .56-.27.56-.58v-1.5c0-.25-.17-.47-.41-.56z" />
      </svg>
    </a>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import AppHero from './components/AppHero.vue'
import AppQuienesSomos from './components/AppQuienesSomos.vue'
import AppContacto from './components/AppContacto.vue'
import AppServicios from './components/AppServicios.vue'

export default {
  components: { AppHeader, AppFooter, AppHero, AppQuienesSomos, AppContacto, AppServicios },
}
</script>

<style>
html, body {
  overflow-x: hidden;
}
</style>
