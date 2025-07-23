#!/usr/bin/env python3
import os
import re
import glob

def fix_image_paths_and_add_css():
    """Corrige las rutas de imágenes y agrega CSS faltantes"""
    
    # Directorio base
    base_dir = "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun"
    
    # CSS que necesitamos agregar
    css_links = """
    <!-- CSS de Elementor y tema -->
    <link rel='stylesheet' id='twentytwentyfive-style-css' href='wp-content/themes/twentytwentyfive/style4963.css' media='all' />
    <link rel='stylesheet' id='elementor-frontend-css' href='wp-content/plugins/elementor/assets/css/frontend.min2801.css' media='all' />
    <link rel='stylesheet' id='elementor-post-12-css' href='wp-content/uploads/elementor/css/post-128827.css' media='all' />
    <link rel='stylesheet' id='elementor-post-6-css' href='wp-content/uploads/elementor/css/post-68827.css' media='all' />
    <link rel='stylesheet' id='elementor-icons-css' href='wp-content/plugins/elementor/assets/lib/eicons/css/elementor-icons.min2801.css' media='all' />
    <link rel='stylesheet' id='swiper-css' href='wp-content/plugins/elementor/assets/lib/swiper/v8/css/swiper.min2801.css' media='all' />
    <link rel='stylesheet' id='e-animations-css' href='wp-content/plugins/elementor/assets/lib/animations/animations.min2801.css' media='all' />
    <link rel='stylesheet' id='widget-heading-css' href='wp-content/plugins/elementor/assets/css/widget-heading.min2801.css' media='all' />
    <link rel='stylesheet' id='widget-image-css' href='wp-content/plugins/elementor/assets/css/widget-image.min2801.css' media='all' />
    <link rel='stylesheet' id='widget-testimonial-css' href='wp-content/plugins/elementor/assets/css/widget-testimonial.min2801.css' media='all' />
    <link rel='stylesheet' id='google-fonts-1-css' href='wp-content/uploads/elementor/google-fonts/css/robotoe285.css' media='all' />
    <link rel='stylesheet' id='google-fonts-2-css' href='wp-content/uploads/elementor/google-fonts/css/portlligatsans37fa.css' media='all' />
    <link rel='stylesheet' id='google-fonts-3-css' href='wp-content/uploads/elementor/google-fonts/css/robotoslab255f.css' media='all' />
    """
    
    # Buscar todos los archivos HTML
    html_files = glob.glob(os.path.join(base_dir, "*.html"))
    html_files.extend(glob.glob(os.path.join(base_dir, "*/*.html")))
    
    for html_file in html_files:
        print(f"Procesando: {html_file}")
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Corregir rutas de imágenes inconsistentes
            # Cambiar ./wp-content/ por wp-content/
            content = re.sub(r'\./wp-content/', 'wp-content/', content)
            
            # Asegurar que todas las rutas de imágenes sean relativas
            content = re.sub(r'src="wp-content/', 'src="./wp-content/', content)
            content = re.sub(r'srcset="wp-content/', 'srcset="./wp-content/', content)
            content = re.sub(r'href="wp-content/', 'href="./wp-content/', content)
            
            # Corregir rutas duplicadas
            content = re.sub(r'src="\./\./wp-content/', 'src="./wp-content/', content)
            content = re.sub(r'srcset="\./\./wp-content/', 'srcset="./wp-content/', content)
            content = re.sub(r'href="\./\./wp-content/', 'href="./wp-content/', content)
            
            # Corregir rutas mixtas en srcset (ej: "file1.webp 1024w, wp-content/file2.webp 300w")
            content = re.sub(r'srcset="([^"]*)"', lambda m: 'srcset="' + re.sub(r'(?<!\./)(wp-content/)', r'./\1', m.group(1)) + '"', content)
            
            # Agregar CSS faltantes antes del </head>
            if '</head>' in content and 'elementor-frontend-css' not in content:
                content = content.replace('</head>', css_links + '\n</head>')
            
            # Escribir el archivo corregido
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"✓ Corregido: {html_file}")
            
        except Exception as e:
            print(f"✗ Error procesando {html_file}: {e}")

def create_missing_css_files():
    """Crear archivos CSS faltantes básicos si no existen"""
    
    base_dir = "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun"
    
    # CSS básico para Elementor si faltan archivos
    basic_elementor_css = """
/* CSS básico para Elementor */
.elementor-element {
    position: relative;
}

.elementor-widget-container {
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.elementor-heading-title {
    padding: 0;
    margin: 0;
    line-height: 1;
}

.elementor-widget-heading .elementor-heading-title {
    color: #6EC1E4;
}

.elementor-button {
    display: inline-block;
    line-height: 1;
    background-color: #61CE70;
    font-size: 15px;
    padding: 12px 24px;
    border-radius: 3px;
    color: #ffffff;
    text-decoration: none;
    text-align: center;
}

.elementor-button:hover {
    background-color: #4CAF50;
}

.elementor-widget-image img {
    vertical-align: middle;
    display: inline-block;
    max-width: 100%;
    height: auto;
}

.elementor-testimonial-wrapper {
    text-align: center;
}

.elementor-testimonial-content {
    font-size: 18px;
    font-style: italic;
    line-height: 1.8;
    margin-bottom: 20px;
}

.elementor-testimonial-meta {
    display: flex;
    align-items: center;
    justify-content: center;
}

.elementor-testimonial-image img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-right: 15px;
}

.elementor-testimonial-name {
    font-weight: bold;
    margin-bottom: 5px;
}

.elementor-testimonial-job {
    font-size: 14px;
    color: #666;
}

.e-con {
    display: flex;
    flex-direction: column;
}

.e-con-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.e-con-boxed .e-con-inner {
    padding: 20px;
}

@media (max-width: 768px) {
    .e-con-inner {
        padding: 10px;
    }
}
"""
    
    # Verificar y crear archivos CSS faltantes
    css_files_to_check = [
        'wp-content/plugins/elementor/assets/css/frontend.min2801.css',
        'wp-content/plugins/elementor/assets/css/widget-heading.min2801.css',
        'wp-content/plugins/elementor/assets/css/widget-image.min2801.css',
        'wp-content/plugins/elementor/assets/css/widget-testimonial.min2801.css'
    ]
    
    for css_file in css_files_to_check:
        full_path = os.path.join(base_dir, css_file)
        if not os.path.exists(full_path):
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            # Crear archivo CSS básico
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(basic_elementor_css)
            print(f"✓ Creado CSS faltante: {css_file}")

if __name__ == "__main__":
    print("🔧 Corrigiendo rutas de imágenes y agregando CSS...")
    fix_image_paths_and_add_css()
    
    print("\n📝 Creando archivos CSS faltantes...")
    create_missing_css_files()
    
    print("\n✅ ¡Corrección completada!")
    print("Las imágenes ahora deberían cargar correctamente y el sitio tendrá mejor estilo.")