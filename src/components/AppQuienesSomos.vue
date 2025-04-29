<template>
  <section id="quienes-somos" class="bg-nefe-beige-100 text-nefe-brown-600 px-6 md:px-12">
    <div class="max-w-5xl mx-auto">
      <h2 class="text-3xl md:text-4xl font-extrabold text-center mb-8 opacity-0 translate-y-[-20px] animate-fade-in-up">
        ¿Quiénes Somos?
      </h2>
      <p class="text-center text-nefe-brown-400 mb-12 leading-relaxed opacity-0 translate-y-[-20px] animate-fade-in-up delay-100">
        Somos un grupo de jóvenes que se dedica hace más de 7 años al área de tecnología y diseño UI/UX, mejorando la experiencia del usuario, brindando soluciones e ideas innovadoras. Con un enfoque humano y de participación con el cliente, trabajamos con claridad y transparencia, participando activamente en la reducción de costos y optimizando los proyectos de nuestros clientes al máximo.
      </p>
      <div class="flex flex-col md:flex-row items-center md:space-x-8">
        <div class="md:w-1/2 mb-8 md:mb-0 opacity-0 translate-x-[-50px] animate-slide-in-left">
          <img src="@/assets/logo2.png" alt="Nuestro equipo" class="w-full h-auto">
        </div>
        <div class="md:w-1/2 opacity-0 translate-x-[50px] animate-slide-in-right">
          <h3 class="text-2xl font-bold mb-4">
            Nuestro Enfoque
          </h3>
          <p class="text-nefe-brown-400 leading-relaxed">
            Creemos en la importancia de la colaboración y la comunicación constante con nuestros clientes. Nuestro objetivo es transformar ideas en soluciones digitales únicas, adaptadas a las necesidades específicas de cada proyecto. Nos esforzamos por ofrecer resultados de alta calidad, optimizando recursos y asegurando la satisfacción del cliente.
          </p>
          <p class="mt-4 text-nefe-brown-400 leading-relaxed">
            En NefeTech, no solo desarrollamos proyectos, sino que también construimos relaciones de confianza a largo plazo con nuestros clientes, basadas en la transparencia y el compromiso.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  mounted() {
    setTimeout(() => {
      const elements = document.querySelectorAll('.animate-slide-in-left, .animate-slide-in-right, .animate-fade-in-up');
      elements.forEach(el => {
        el.classList.remove('opacity-0', 'translate-x-[-50px]', 'translate-x-[50px]', 'translate-y-[-20px]');
      });
    }, 150);
  }
}
</script>

<style scoped>
@keyframes slide-in-left {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slide-in-right {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slide-in-left {
  animation: slide-in-left 0.8s ease-out forwards;
}

.animate-slide-in-right {
  animation: slide-in-right 0.8s ease-out forwards;
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out forwards;
}

.delay-100 {
  animation-delay: 0.1s;
}
</style>