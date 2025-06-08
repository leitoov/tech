<template>
  <section id="contacto" class="bg-nefe-beige-100 text-nefe-brown-600 py-16 px-6 md:px-12">
    <div class="max-w-4xl mx-auto">
      <h2 class="text-3xl md:text-4xl font-extrabold text-center mb-8 opacity-0 translate-y-[-20px] animate-fade-in-up">
        Contáctanos
      </h2>
      <p class="text-center text-nefe-brown-400 mb-12 opacity-0 translate-y-[-20px] animate-fade-in-up delay-100">
        ¿Tienes alguna consulta o proyecto en mente? Completa el formulario y nos pondremos en contacto contigo lo antes posible.
      </p>
      <form @submit.prevent="enviarContacto" class="space-y-6 opacity-0 translate-y-[20px] animate-fade-in-up delay-200">
        <!-- Nombre y Apellido -->
        <div class="flex flex-col md:flex-row md:space-x-4">
          <div class="flex-1">
            <label for="nombre" class="block text-sm font-semibold mb-2">Nombre</label>
            <input
              v-model="form.nombre"
              type="text"
              id="nombre"
              name="nombre"
              placeholder="Tu nombre"
              class="w-full px-4 py-2 border border-nefe-brown-200 rounded-md focus:outline-none focus:ring-2 focus:ring-nefe-gold-300"
            />
          </div>
          <div class="flex-1 mt-4 md:mt-0">
            <label for="apellido" class="block text-sm font-semibold mb-2">Apellido</label>
            <input
              v-model="form.apellido"
              type="text"
              id="apellido"
              name="apellido"
              placeholder="Tu apellido"
              class="w-full px-4 py-2 border border-nefe-brown-200 rounded-md focus:outline-none focus:ring-2 focus:ring-nefe-gold-300"
            />
          </div>
        </div>
        <!-- Email -->
        <div>
          <label for="email" class="block text-sm font-semibold mb-2">Email</label>
          <input
            v-model="form.email"
            type="email"
            id="email"
            name="email"
            placeholder="Tu correo electrónico"
            class="w-full px-4 py-2 border border-nefe-brown-200 rounded-md focus:outline-none focus:ring-2 focus:ring-nefe-gold-300"
          />
        </div>
        <!-- Celular -->
        <div>
          <label for="celular" class="block text-sm font-semibold mb-2">Celular</label>
          <input
            v-model="form.celular"
            type="tel"
            id="celular"
            name="celular"
            placeholder="Tu número de celular"
            class="w-full px-4 py-2 border border-nefe-brown-200 rounded-md focus:outline-none focus:ring-2 focus:ring-nefe-gold-300"
          />
        </div>
        <!-- Mensaje -->
        <div>
          <label for="mensaje" class="block text-sm font-semibold mb-2">Mensaje</label>
          <textarea
            v-model="form.mensaje"
            id="mensaje"
            name="mensaje"
            rows="5"
            placeholder="Escribe tu mensaje aquí..."
            class="w-full px-4 py-2 border border-nefe-brown-200 rounded-md focus:outline-none focus:ring-2 focus:ring-nefe-gold-300"
          ></textarea>
        </div>
        <!-- Botón Enviar -->
        <div class="text-center">
          <button
            type="submit"
            class="bg-nefe-gold-300 text-nefe-brown-600 px-6 py-3 rounded-md font-semibold hover:bg-nefe-gold-400 transition"
          >
            Enviar Mensaje
          </button>
        </div>
      </form>
      <!-- Botón de correo directo -->
      <div class="text-center mt-8 opacity-0 translate-y-[20px] animate-fade-in-up delay-300">
        <a
          href="mailto:leonelexequielvincent@gmail.com"
          class="text-nefe-gold-300 font-semibold hover:text-nefe-gold-400 transition"
        >
          O envíanos un correo directamente
        </a>
      </div>
    </div>
  </section>
</template>

<script>
import { crearContacto } from "../services/contactoService";

export default {
  data() {
    return {
      form: {
        nombre: "",
        apellido: "",
        email: "",
        celular: "",
        mensaje: "",
        tipo_dispositivo: "",
        campaña: "",
      },
    };
  },
  methods: {
    async enviarContacto() {
      if (!this.form.nombre || !this.form.apellido || !this.form.email) {
        alert("Por favor, completa todos los campos obligatorios.");
        return;
      }

      if (!this.validarEmail(this.form.email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
      }

      try {
        const response = await crearContacto(this.form);
        alert(response.mensaje); // Mostrar mensaje de éxito
        this.form = {
          nombre: "",
          apellido: "",
          email: "",
          celular: "",
          mensaje: "",
          tipo_dispositivo: "",
          campaña: "",
        };
      } catch (error) {
        console.error(error);
        alert("Error al enviar el contacto");
      }
    },
    validarEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    },
  },
  mounted() {
    // Activar las animaciones al montar el componente
    setTimeout(() => {
      const elements = document.querySelectorAll(".animate-fade-in-up");
      elements.forEach((el) => {
        el.classList.remove("opacity-0", "translate-y-[-20px]", "translate-y-[20px]");
      });
    }, 210);
  },
};
</script>

<style scoped>
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out forwards;
}

.delay-100 {
  animation-delay: 0.1s;
}

.delay-200 {
  animation-delay: 0.2s;
}

.delay-300 {
  animation-delay: 0.3s;
}
</style>