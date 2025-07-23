#!/bin/bash

# Script para corregir todas las rutas de imágenes de relativas a absolutas

echo "Corrigiendo rutas de imágenes..."

# Archivos HTML a corregir
files=(
    "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun/index.html"
    "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun/c.html"
    "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun/OPR/index.html"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "Procesando: $(basename $file)"
        
        # Crear backup
        cp "$file" "$file.backup"
        
        # Corregir rutas de imágenes
        sed -i '' 's|src="./wp-content/|src="/wp-content/|g' "$file"
        sed -i '' 's|srcset="./wp-content/|srcset="/wp-content/|g' "$file"
        
        # Corregir múltiples rutas en srcset
        sed -i '' 's|, ./wp-content/|, /wp-content/|g' "$file"
        
        echo "Corregido: $(basename $file)"
    else
        echo "No encontrado: $file"
    fi
done

echo "Proceso completado!"
echo "Se crearon backups con extensión .backup"