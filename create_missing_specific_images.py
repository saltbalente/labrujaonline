#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont
import shutil

def create_missing_images():
    """Crear las imágenes específicas que faltan según los archivos HTML"""
    
    base_dir = "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun"
    uploads_dir = os.path.join(base_dir, "wp-content/uploads/2025/04")
    theme_images_dir = os.path.join(base_dir, "wp-content/themes/twentytwentyfive/assets/images")
    
    # Crear directorio del tema si no existe
    os.makedirs(theme_images_dir, exist_ok=True)
    
    # Lista de imágenes que necesitamos crear
    missing_images = [
        # Imágenes del tema
        ("404-image.webp", theme_images_dir, 800, 600),
        
        # Imágenes de uploads que faltan
        ("bruja-efectiva-300x300.webp", uploads_dir, 300, 300),
        ("bruja-efectiva-150x150.webp", uploads_dir, 150, 150),
        ("bruja-efectiva.webp", uploads_dir, 1080, 1080),
        ("amarres-de-amor-300x300.webp", uploads_dir, 300, 300),
        ("amarres-de-amor-150x150.webp", uploads_dir, 150, 150),
        ("amarres-de-amor.webp", uploads_dir, 1080, 1080),
        ("bruja-amarres-300x300.webp", uploads_dir, 300, 300),
        ("bruja-amarres-150x150.webp", uploads_dir, 150, 150),
        ("brujo-efectivo-225x300.webp", uploads_dir, 225, 300),
        ("amarres-efectivos-300x300.webp", uploads_dir, 300, 300),
        ("amarres-efectivos-150x150.webp", uploads_dir, 150, 150),
        ("mejor-bruja-amarres-300x300.webp", uploads_dir, 300, 300),
        ("mejor-bruja-amarres-150x150.webp", uploads_dir, 150, 150),
        ("signo-de-verificacion.png", uploads_dir, 512, 512),
    ]
    
    created_count = 0
    
    for filename, directory, width, height in missing_images:
        filepath = os.path.join(directory, filename)
        
        if os.path.exists(filepath):
            print(f"Ya existe: {filename}")
            continue
            
        # Buscar imagen base para redimensionar
        base_name = filename.split('-')[0] + '-' + filename.split('-')[1] if '-' in filename else filename.split('.')[0]
        base_extensions = ['.webp', '.png', '.jpg', '.jpeg']
        
        source_image = None
        for ext in base_extensions:
            # Buscar imagen más grande existente
            for existing_file in os.listdir(uploads_dir):
                if existing_file.startswith(base_name) and existing_file.endswith(ext):
                    if '1024x1024' in existing_file or '768x768' in existing_file or existing_file == base_name + ext:
                        source_path = os.path.join(uploads_dir, existing_file)
                        if os.path.exists(source_path):
                            source_image = source_path
                            break
            if source_image:
                break
        
        try:
            if source_image:
                # Redimensionar imagen existente
                with Image.open(source_image) as img:
                    # Convertir a RGB si es necesario
                    if img.mode in ('RGBA', 'LA', 'P'):
                        img = img.convert('RGB')
                    
                    # Redimensionar manteniendo aspecto
                    img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
                    
                    # Guardar en el formato correcto
                    if filename.endswith('.webp'):
                        img_resized.save(filepath, 'WEBP', quality=85, optimize=True)
                    elif filename.endswith('.png'):
                        img_resized.save(filepath, 'PNG', optimize=True)
                    else:
                        img_resized.save(filepath, 'JPEG', quality=85, optimize=True)
                    
                    print(f"Creado: {filename} (redimensionado desde {os.path.basename(source_image)})")
                    created_count += 1
            else:
                # Crear imagen placeholder
                img = Image.new('RGB', (width, height), color='#8B4513')
                draw = ImageDraw.Draw(img)
                
                # Texto para el placeholder
                if 'bruja' in filename.lower():
                    text = "Bruja Efectiva"
                elif 'amarre' in filename.lower():
                    text = "Amarres de Amor"
                elif '404' in filename:
                    text = "Imagen no encontrada"
                elif 'verificacion' in filename:
                    text = "✓"
                else:
                    text = "Imagen"
                
                # Calcular tamaño de fuente
                font_size = min(width, height) // 8
                try:
                    font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
                
                # Centrar texto
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                x = (width - text_width) // 2
                y = (height - text_height) // 2
                
                draw.text((x, y), text, fill='white', font=font)
                
                # Guardar
                if filename.endswith('.webp'):
                    img.save(filepath, 'WEBP', quality=85, optimize=True)
                elif filename.endswith('.png'):
                    img.save(filepath, 'PNG', optimize=True)
                else:
                    img.save(filepath, 'JPEG', quality=85, optimize=True)
                
                print(f"Creado placeholder: {filename}")
                created_count += 1
                
        except Exception as e:
            print(f"Error creando {filename}: {e}")
    
    print(f"\nTotal de archivos creados: {created_count}")
    print("Proceso completado!")

if __name__ == "__main__":
    create_missing_images()