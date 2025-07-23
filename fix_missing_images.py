#!/usr/bin/env python3
import os
import shutil

# Directorio base
base_dir = "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun"
uploads_dir = os.path.join(base_dir, "wp-content/uploads/2025/04")

# Mapeo de archivos faltantes a archivos existentes
missing_files = {
    "testimonio-brujo._1.webp": "testimonio-brujo._1-498x1024.webp",
    "testimonio-brujo._1-146x300.webp": "testimonio-brujo._1-498x1024.webp",
    "regreso-parejas-amor-768x768.webp": "regreso-parejas-amor.webp",
    "regreso-parejas-amor-300x300.webp": "regreso-parejas-amor.webp",
    "regreso-parejas-amor-1024x1024.webp": "regreso-parejas-amor.webp",
    "regreso-parejas-amor-150x150.webp": "regreso-parejas-amor.webp",
    "mexicano-eeuu-768x768.png": "mexicano-eeuu.png",
    "mexicano-eeuu-300x300.png": "mexicano-eeuu.png",
    "mexicano-eeuu-150x150.png": "mexicano-eeuu.png",
    "testimonio-amarres-amor-142x300.webp": "testimonio-amarres-amor.webp",
    "amarres-amor-testimonio-142x300.webp": "amarres-amor-testimonio.webp",
    "cliente-regreso-parejas-300x300.webp": "cliente-regreso-parejas.webp",
    "cliente-regreso-parejas-150x150.webp": "cliente-regreso-parejas.webp",
    "cliente-amarres-amor-300x300.jpg": "cliente-amarres-amor.jpg",
    "cliente-amarres-amor-150x150.jpg": "cliente-amarres-amor.jpg"
}

def create_missing_images():
    created_count = 0
    
    for missing_file, source_file in missing_files.items():
        missing_path = os.path.join(uploads_dir, missing_file)
        source_path = os.path.join(uploads_dir, source_file)
        
        # Verificar si el archivo fuente existe
        if os.path.exists(source_path):
            # Verificar si el archivo faltante ya existe
            if not os.path.exists(missing_path):
                try:
                    # Copiar el archivo fuente al archivo faltante
                    shutil.copy2(source_path, missing_path)
                    print(f"Creado: {missing_file} (copiado de {source_file})")
                    created_count += 1
                except Exception as e:
                    print(f"Error al crear {missing_file}: {e}")
            else:
                print(f"Ya existe: {missing_file}")
        else:
            print(f"Archivo fuente no encontrado: {source_file}")
    
    print(f"\nTotal de archivos creados: {created_count}")

if __name__ == "__main__":
    print("Creando versiones faltantes de imágenes...")
    create_missing_images()
    print("Proceso completado!")