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
            <span class="material-symbols-outlined icon-size">code_blocks</span>
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
            <span class="material-symbols-outlined icon-size">smartphone</span>
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
            <span class="material-symbols-outlined icon-size">tune</span>
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
            <span class="material-symbols-outlined icon-size">support_agent</span>
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
            <span class="material-symbols-outlined icon-size">palette</span>
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
            <span class="material-symbols-outlined icon-size">campaign</span>
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

.material-symbols-outlined.icon-size {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 48;
  font-size: 3rem;
}
</style>
