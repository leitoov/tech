/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        colors: {
          nefe: {
            brown: {
              100: '#EAD8CC',  // Marrón clarito (fondos suaves)
              200: '#D3B6A2',  // Marrón claro
              300: '#A6693F',  // Marrón medio (acento)
              400: '#7A482B',  // Marrón más oscuro
              500: '#4B2E1A',  // Marrón oscuro (header/footer)
              600: '#2E1B0F'   // Marrón profundo (bordes, detalles)
            },
            beige: {
              100: '#F9F4EF',  // Beige muy claro (background)
              200: '#F3E1C7',  // Beige claro (cards)
              300: '#E4CBAA',  // Beige medio
              400: '#C7A97D',  // Beige intenso
              500: '#A3835C',  // Beige oscuro
              600: '#7C5D3D'   // Beige profundo
            },
            gold: {
              100: '#FFF3DC',  // Dorado clarito
              200: '#FFE0AA',  // Dorado suave
              300: '#E3A857',  // Dorado medio
              400: '#C98B35',  // Dorado fuerte
              500: '#A46A23',  // Dorado oscuro
              600: '#7D4C18'   // Dorado profundo
            },
            blue: {
              100: '#DBEAFE',  // Azul claro (backgrounds)
              200: '#93C5FD',  // Azul intermedio
              300: '#60A5FA',  // Azul medio
              400: '#3B82F6',  // Azul vibrante (botones)
              500: '#2563EB',  // Azul oscuro
              600: '#1D4ED8'   // Azul profundo
            }
          }
        },
        fontFamily: {
          sans: ['Poppins', 'sans-serif'], // Define Poppins como la fuente principal
        },
      },
    },
    plugins: [],
  }
