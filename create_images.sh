#!/bin/bash

# Script para crear imágenes faltantes usando ImageMagick o sips (macOS)

BASE_DIR="/Users/edwarbechara/sitio_descargado/brujaefectiva.fun"
UPLOADS_DIR="$BASE_DIR/wp-content/uploads/2025/04"
THEME_DIR="$BASE_DIR/wp-content/themes/twentytwentyfive/assets/images"

# Crear directorio del tema si no existe
mkdir -p "$THEME_DIR"

echo "Creando imágenes faltantes..."

# Función para crear imagen placeholder
create_placeholder() {
    local filename="$1"
    local directory="$2"
    local width="$3"
    local height="$4"
    local text="$5"
    
    local filepath="$directory/$filename"
    
    if [ -f "$filepath" ]; then
        echo "Ya existe: $filename"
        return
    fi
    
    # Crear imagen placeholder usando sips (macOS)
    # Primero crear una imagen temporal
    local temp_file="/tmp/temp_placeholder.png"
    
    # Crear imagen sólida usando sips
    sips -s format png --setProperty pixelWidth $width --setProperty pixelHeight $height -s formatOptions default /System/Library/CoreServices/DefaultDesktop.heic --out "$temp_file" 2>/dev/null
    
    if [ ! -f "$temp_file" ]; then
        # Alternativa: crear archivo SVG y convertir
        cat > "/tmp/placeholder.svg" << EOF
<svg width="$width" height="$height" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#8B4513"/>
  <text x="50%" y="50%" font-family="Arial" font-size="$(($width/10))" fill="white" text-anchor="middle" dominant-baseline="middle">$text</text>
</svg>
EOF
        
        # Intentar convertir SVG a imagen
        if command -v rsvg-convert >/dev/null 2>&1; then
            rsvg-convert -w $width -h $height "/tmp/placeholder.svg" -o "$temp_file"
        elif command -v convert >/dev/null 2>&1; then
            convert "/tmp/placeholder.svg" -resize "${width}x${height}" "$temp_file"
        else
            # Crear imagen simple con sips desde una imagen del sistema
            cp "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/GenericDocumentIcon.icns" "$temp_file" 2>/dev/null || touch "$temp_file"
        fi
    fi
    
    # Convertir al formato final
    if [ -f "$temp_file" ]; then
        if [[ "$filename" == *.webp ]]; then
            # Para WebP, usar sips si está disponible
            sips -s format webp "$temp_file" --out "$filepath" 2>/dev/null || cp "$temp_file" "$filepath"
        elif [[ "$filename" == *.png ]]; then
            sips -s format png "$temp_file" --out "$filepath" 2>/dev/null || cp "$temp_file" "$filepath"
        else
            cp "$temp_file" "$filepath"
        fi
        
        echo "Creado: $filename"
        rm -f "$temp_file"
    else
        echo "Error creando: $filename"
    fi
}

# Función para redimensionar imagen existente
resize_existing() {
    local source="$1"
    local target="$2"
    local width="$3"
    local height="$4"
    
    if [ -f "$target" ]; then
        echo "Ya existe: $(basename $target)"
        return
    fi
    
    if [ -f "$source" ]; then
        sips -Z $(($width > $height ? $width : $height)) "$source" --out "$target" 2>/dev/null
        echo "Redimensionado: $(basename $target)"
    fi
}

# Crear imagen 404
create_placeholder "404-image.webp" "$THEME_DIR" 800 600 "404"

# Crear versiones faltantes de bruja-efectiva
if [ -f "$UPLOADS_DIR/bruja-efectiva-1024x1024.webp" ]; then
    resize_existing "$UPLOADS_DIR/bruja-efectiva-1024x1024.webp" "$UPLOADS_DIR/bruja-efectiva-300x300.webp" 300 300
    resize_existing "$UPLOADS_DIR/bruja-efectiva-1024x1024.webp" "$UPLOADS_DIR/bruja-efectiva-150x150.webp" 150 150
    resize_existing "$UPLOADS_DIR/bruja-efectiva-1024x1024.webp" "$UPLOADS_DIR/bruja-efectiva.webp" 1080 1080
fi

# Crear versiones faltantes de amarres-de-amor
if [ -f "$UPLOADS_DIR/amarres-de-amor-1024x1024.webp" ]; then
    resize_existing "$UPLOADS_DIR/amarres-de-amor-1024x1024.webp" "$UPLOADS_DIR/amarres-de-amor-300x300.webp" 300 300
    resize_existing "$UPLOADS_DIR/amarres-de-amor-1024x1024.webp" "$UPLOADS_DIR/amarres-de-amor-150x150.webp" 150 150
    resize_existing "$UPLOADS_DIR/amarres-de-amor-1024x1024.webp" "$UPLOADS_DIR/amarres-de-amor.webp" 1080 1080
fi

# Crear versiones faltantes de bruja-amarres
if [ -f "$UPLOADS_DIR/bruja-amarres.webp" ]; then
    resize_existing "$UPLOADS_DIR/bruja-amarres.webp" "$UPLOADS_DIR/bruja-amarres-300x300.webp" 300 300
    resize_existing "$UPLOADS_DIR/bruja-amarres.webp" "$UPLOADS_DIR/bruja-amarres-150x150.webp" 150 150
fi

# Crear versiones faltantes de brujo-efectivo
if [ -f "$UPLOADS_DIR/brujo-efectivo.webp" ]; then
    resize_existing "$UPLOADS_DIR/brujo-efectivo.webp" "$UPLOADS_DIR/brujo-efectivo-225x300.webp" 225 300
fi

# Crear versiones faltantes de amarres-efectivos
if [ -f "$UPLOADS_DIR/amarres-efectivos.webp" ]; then
    resize_existing "$UPLOADS_DIR/amarres-efectivos.webp" "$UPLOADS_DIR/amarres-efectivos-300x300.webp" 300 300
    resize_existing "$UPLOADS_DIR/amarres-efectivos.webp" "$UPLOADS_DIR/amarres-efectivos-150x150.webp" 150 150
fi

# Crear versiones faltantes de mejor-bruja-amarres
if [ -f "$UPLOADS_DIR/mejor-bruja-amarres.webp" ]; then
    resize_existing "$UPLOADS_DIR/mejor-bruja-amarres.webp" "$UPLOADS_DIR/mejor-bruja-amarres-300x300.webp" 300 300
    resize_existing "$UPLOADS_DIR/mejor-bruja-amarres.webp" "$UPLOADS_DIR/mejor-bruja-amarres-150x150.webp" 150 150
fi

# Crear signo-de-verificacion.png si no existe
if [ -f "$UPLOADS_DIR/signo-de-verificacion-300x300.png" ]; then
    resize_existing "$UPLOADS_DIR/signo-de-verificacion-300x300.png" "$UPLOADS_DIR/signo-de-verificacion.png" 512 512
else
    create_placeholder "signo-de-verificacion.png" "$UPLOADS_DIR" 512 512 "✓"
fi

echo "Proceso completado!"