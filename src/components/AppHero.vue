<template>
    <main>
        <section id="inicio" class="bg-nefe-beige-100 text-nefe-brown-600 py-16 px-6 md:px-12">
            <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between">
                <!-- Texto -->
                <div 
                    class="md:w-1/2 opacity-0 translate-x-[-50px] animate-slide-in-left"
                >
                    <h1 class="text-4xl md:text-5xl font-extrabold leading-tight">
                        Creamos soluciones digitales ágiles, personalizadas y con impacto real
                    </h1>
                    <p class="mt-6 text-lg text-nefe-brown-400">
                        En NefeTech transformamos tus ideas en soluciones digitales ágiles, funcionales y hechas a medida. Nos enfocamos en brindarte resultados concretos con una atención cercana que hace la diferencia.
                    </p>
                    <div class="mt-8 flex flex-col md:flex-row md:space-x-4 space-y-4 md:space-y-0">
                        <a href="#servicios" class="bg-nefe-gold-300 text-nefe-brown-600 px-6 py-3 rounded-md font-semibold hover:bg-nefe-gold-400 transition flex items-center justify-center">
                            Nuestros Servicios
                        </a>
                        <a href="#contacto" class="border border-nefe-gold-300 text-nefe-gold-300 px-6 py-3 rounded-md font-semibold hover:bg-nefe-gold-300 hover:text-nefe-brown-600 transition flex items-center justify-center">
                            Contáctanos
                        </a>
                    </div>
                </div>
                <!-- Imagen -->
                <div 
                    class="md:w-1/2 mt-10 md:mt-0 opacity-0 translate-x-[50px] animate-slide-in-right"
                >
                    <img src="@/assets/logo1.png" alt="Soluciones digitales NefeTech" class="w-full h-auto">
                </div>
            </div>
        </section>
    </main>
</template>

<script>
export default {
    mounted() {
        setTimeout(() => {
            const elements = document.querySelectorAll('.animate-slide-in-left, .animate-slide-in-right');
            elements.forEach(el => {
                el.classList.remove('opacity-0', 'translate-x-[-50px]', 'translate-x-[50px]');
            });
        }, 100); 
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

.animate-slide-in-left {
    animation: slide-in-left 0.8s ease-out forwards;
}

.animate-slide-in-right {
    animation: slide-in-right 0.8s ease-out forwards;
}
</style>
