<template>
  <section id="servicios" class="bg-nefe-beige-100 text-nefe-brown-600 py-16 px-6 md:px-12">
    <div class="max-w-7xl mx-auto">
      <!-- Título -->
      <h2 class="text-3xl md:text-4xl font-extrabold text-center mb-8">
        Nuestros Servicios
      </h2>
      <p class="text-center text-nefe-brown-400 mb-12 leading-relaxed">
        Transformamos tus ideas en soluciones digitales únicas. Descubre todo lo que podemos hacer por ti.
      </p>

      <!-- Servicios -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Servicio 1 -->
        <div
          class="card flex flex-col items-center text-center bg-white shadow-lg rounded-lg p-6 hover:shadow-xl transition cursor-pointer"
          @click="redirectToWhatsApp('Desarrollo de Sitios Web')"
        >
          <div class="bg-nefe-gold-300 text-white rounded-full p-4 mb-4">
            <!-- Ícono de desarrollo web -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v16a1 1 0 01-1 1H4a1 1 0 01-1-1V4z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9h8M8 13h5" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-2">Desarrollo de Sitios Web</h3>
          <p class="text-nefe-brown-400 leading-relaxed">
            Creamos sitios web modernos, responsivos y optimizados para ofrecer la mejor experiencia al usuario.
          </p>
        </div>

        <!-- Servicio 2 -->
        <div
          class="card flex flex-col items-center text-center bg-white shadow-lg rounded-lg p-6 hover:shadow-xl transition cursor-pointer"
          @click="redirectToWhatsApp('Aplicaciones Móviles')"
        >
          <div class="bg-nefe-gold-300 text-white rounded-full p-4 mb-4">
            <!-- Ícono de aplicaciones móviles -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4h10M7 20h10M12 4v16" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-2">Aplicaciones Móviles</h3>
          <p class="text-nefe-brown-400 leading-relaxed">
            Desarrollamos aplicaciones móviles personalizadas para Android e iOS, adaptadas a tus necesidades.
          </p>
        </div>

        <!-- Servicio 3 -->
        <div
          class="card flex flex-col items-center text-center bg-white shadow-lg rounded-lg p-6 hover:shadow-xl transition cursor-pointer"
          @click="redirectToWhatsApp('Sistemas de Gestión')"
        >
          <div class="bg-nefe-gold-300 text-white rounded-full p-4 mb-4">
            <!-- Ícono de sistemas de gestión -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6M9 16h6M9 8h6M4 6h16M4 18h16" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-2">Sistemas de Gestión</h3>
          <p class="text-nefe-brown-400 leading-relaxed">
            Diseñamos sistemas de gestión, control de stock y herramientas empresariales para optimizar tus procesos.
          </p>
        </div>

        <!-- Servicio 4 -->
        <div
          class="card flex flex-col items-center text-center bg-white shadow-lg rounded-lg p-6 hover:shadow-xl transition cursor-pointer"
          @click="redirectToWhatsApp('Asesoramiento y Acompañamiento')"
        >
          <div class="bg-nefe-gold-300 text-white rounded-full p-4 mb-4">
            <!-- Ícono de asesoramiento -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h8M8 14h8M12 18h0M12 6h0" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-2">Asesoramiento y Acompañamiento</h3>
          <p class="text-nefe-brown-400 leading-relaxed">
            Te guiamos en el desarrollo de tus ideas, brindando asesoramiento y acompañamiento en cada etapa del proyecto.
          </p>
        </div>

        <!-- Servicio 5 -->
        <div
          class="card flex flex-col items-center text-center bg-white shadow-lg rounded-lg p-6 hover:shadow-xl transition cursor-pointer"
          @click="redirectToWhatsApp('Diseño de Marca')"
        >
          <div class="bg-nefe-gold-300 text-white rounded-full p-4 mb-4">
            <!-- Ícono de diseño de marca -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16M8 8h8M8 16h8" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-2">Diseño de Marca</h3>
          <p class="text-nefe-brown-400 leading-relaxed">
            Creamos diseños de marca, logotipos, imágenes y contenido para redes sociales que destacan tu identidad.
          </p>
        </div>

        <!-- Servicio 6 -->
        <div
          class="card flex flex-col items-center text-center bg-white shadow-lg rounded-lg p-6 hover:shadow-xl transition cursor-pointer"
          @click="redirectToWhatsApp('Redes Sociales')"
        >
          <div class="bg-nefe-gold-300 text-white rounded-full p-4 mb-4">
            <!-- Ícono de redes sociales -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16M8 8h8M8 16h8" />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-2">Redes Sociales</h3>
          <p class="text-nefe-brown-400 leading-relaxed">
            Gestionamos tus redes sociales, creando contenido atractivo y estrategias para aumentar tu presencia online.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  methods: {
    redirectToWhatsApp(service) {
      const phoneNumber = "+5491122512775";
      const message = `Hola, estoy interesado en el servicio de ${service}.`;
      const url = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
      window.open(url, "_blank");
    },
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

.card {
  animation: fade-in-up 0.8s ease-out forwards;
  opacity: 0; 
}
</style>