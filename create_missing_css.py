#!/usr/bin/env python3
import os

# Directorio base
base_dir = "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun"

# Archivos CSS faltantes que necesitamos crear
missing_css_files = [
    "wp-content/plugins/elementor/assets/lib/eicons/css/elementor-icons.min2801.css",
    "wp-content/plugins/elementor/assets/lib/swiper/v8/css/swiper.min2801.css", 
    "wp-content/plugins/elementor/assets/lib/animations/animations.min2801.css"
]

# Contenido básico para cada tipo de archivo
css_contents = {
    "elementor-icons": """/* Elementor Icons CSS */
.eicon-star:before { content: "\\2605"; }
.eicon-heart:before { content: "\\2665"; }
.eicon-phone:before { content: "\\260E"; }
.eicon-envelope:before { content: "\\2709"; }
.eicon-whatsapp:before { content: "\\1F4F1"; }
""",
    "swiper": """/* Swiper CSS */
.swiper-container { margin: 0 auto; position: relative; overflow: hidden; list-style: none; padding: 0; z-index: 1; }
.swiper-wrapper { position: relative; width: 100%; height: 100%; z-index: 1; display: flex; transition-property: transform; box-sizing: content-box; }
.swiper-slide { flex-shrink: 0; width: 100%; height: 100%; position: relative; transition-property: transform; }
""",
    "animations": """/* Elementor Animations CSS */
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes fadeInUp { from { opacity: 0; transform: translate3d(0, 100%, 0); } to { opacity: 1; transform: none; } }
@keyframes fadeInDown { from { opacity: 0; transform: translate3d(0, -100%, 0); } to { opacity: 1; transform: none; } }
.elementor-animation-fadeIn { animation: fadeIn 1s; }
.elementor-animation-fadeInUp { animation: fadeInUp 1s; }
.elementor-animation-fadeInDown { animation: fadeInDown 1s; }
"""
}

def create_missing_css():
    for css_file in missing_css_files:
        full_path = os.path.join(base_dir, css_file)
        
        # Crear directorios si no existen
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Determinar el contenido basado en el nombre del archivo
        if "eicons" in css_file:
            content = css_contents["elementor-icons"]
        elif "swiper" in css_file:
            content = css_contents["swiper"]
        elif "animations" in css_file:
            content = css_contents["animations"]
        else:
            content = "/* CSS placeholder */"
        
        # Escribir el archivo
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Creado: {css_file}")

if __name__ == "__main__":
    create_missing_css()
    print("Archivos CSS faltantes creados exitosamente!")