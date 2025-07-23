#!/usr/bin/env python3
"""
Script para limpiar y preparar el sitio descargado con httrack
para que sea completamente independiente del dominio original.
"""

import os
import re
import shutil
import json
from pathlib import Path

def remove_unwanted_files(root_dir):
    """Eliminar archivos que no son necesarios para un sitio estático"""
    unwanted_patterns = [
        '*.php',
        '*.json',
        'xmlrpc*',
        'wp-json/*',
        'wp-admin/*',
        'wp-includes/js/*',
        'comments/feed/*',
        'feed/*'
    ]
    
    unwanted_dirs = [
        'wp-json',
        'comments',
        'feed'
    ]
    
    # Eliminar directorios completos
    for dir_name in unwanted_dirs:
        dir_path = os.path.join(root_dir, dir_name)
        if os.path.exists(dir_path):
            print(f"Eliminando directorio: {dir_path}")
            shutil.rmtree(dir_path)
    
    # Eliminar archivos específicos
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            should_remove = False
            reason = ""
            
            # Eliminar archivos PHP
            if file.endswith('.php'):
                should_remove = True
                reason = "archivo PHP"
            
            # Eliminar archivos JSON de wp-json
            elif 'wp-json' in file_path and file.endswith('.json'):
                should_remove = True
                reason = "archivo JSON"
            
            # Eliminar archivos xmlrpc
            elif file.startswith('xmlrpc'):
                should_remove = True
                reason = "archivo xmlrpc"
            
            if should_remove and os.path.exists(file_path):
                print(f"Eliminando {reason}: {file_path}")
                os.remove(file_path)

def clean_html_content(file_path, original_domain):
    """Limpiar contenido HTML de referencias al dominio original"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remover comentarios de HTTrack
        content = re.sub(r'<!-- Mirrored from.*?-->', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Added by HTTrack.*?-->', '', content, flags=re.DOTALL)
        
        # Convertir URLs absolutas a relativas
        content = re.sub(rf'https?://{re.escape(original_domain)}/', './', content)
        content = re.sub(rf'https?://www\.{re.escape(original_domain)}/', './', content)
        
        # Remover referencias a feeds y APIs de WordPress
        content = re.sub(r'<link[^>]*feed[^>]*>', '', content)
        content = re.sub(r'<link[^>]*rsd\+xml[^>]*>', '', content)
        content = re.sub(r'<link[^>]*api\.w\.org[^>]*>', '', content)
        
        # Remover meta tags específicos de WordPress
        content = re.sub(r'<meta name="generator"[^>]*>', '', content)
        
        # Limpiar JSON-LD schema con URLs absolutas
        def clean_jsonld(match):
            jsonld_content = match.group(1)
            jsonld_content = re.sub(rf'https?://(www\.)?{re.escape(original_domain)}/', './', jsonld_content)
            return f'<script type="application/ld+json" class="yoast-schema-graph">{jsonld_content}</script>'
        
        content = re.sub(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', clean_jsonld, content, flags=re.DOTALL)
        
        # Remover scripts de Google Analytics y tracking
        content = re.sub(r'<script[^>]*googletagmanager[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script[^>]*gtag[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!--.*?tracking.*?-->', '', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<noscript>.*?googletagmanager.*?</noscript>', '', content, flags=re.DOTALL)
        
        # Remover scripts problemáticos de WordPress/Elementor
        content = re.sub(r'<script[^>]*jquery[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script[^>]*elementor[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script[^>]*joinchat[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script[^>]*wp-includes[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        
        # Remover enlaces a archivos JS
        content = re.sub(r'<script[^>]*src=["\'][^"\']*\.js[^"\']*["\'][^>]*></script>', '', content)
        content = re.sub(r'<link[^>]*modulepreload[^>]*>', '', content)
        
        # Limpiar referencias a WordPress.org
        content = re.sub(r'https://wordpress\.org[^"\']*', '#', content)
        content = re.sub(r'https://yoast\.com[^"\']*', '#', content)
        
        # Limpiar URLs de emojis externos
        content = re.sub(r'https://s\.w\.org/images/core/emoji/[^"\']*', '', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Limpiado: {file_path}")
        
    except Exception as e:
        print(f"Error procesando {file_path}: {e}")

def clean_css_content(file_path, original_domain):
    """Limpiar contenido CSS de referencias al dominio original"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convertir URLs absolutas a relativas en CSS
        content = re.sub(rf'url\(["\']?https?://{re.escape(original_domain)}/', 'url("./', content)
        content = re.sub(rf'url\(["\']?https?://www\.{re.escape(original_domain)}/', 'url("./', content)
        
        # Limpiar comentarios con URLs
        content = re.sub(r'/\*.*?https?://[^*]*\*/', '', content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"CSS limpiado: {file_path}")
        
    except Exception as e:
        print(f"Error procesando CSS {file_path}: {e}")

def process_site(root_dir, original_domain):
    """Procesar todo el sitio"""
    print(f"Procesando sitio en: {root_dir}")
    print(f"Dominio original: {original_domain}")
    
    # Paso 1: Eliminar archivos no deseados
    print("\n=== Eliminando archivos no deseados ===")
    remove_unwanted_files(root_dir)
    
    # Paso 2: Procesar archivos HTML
    print("\n=== Procesando archivos HTML ===")
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                clean_html_content(file_path, original_domain)
    
    # Paso 3: Procesar archivos CSS
    print("\n=== Procesando archivos CSS ===")
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.css'):
                file_path = os.path.join(root, file)
                clean_css_content(file_path, original_domain)
    
    print("\n=== Limpieza completada ===")
    print("El sitio ahora es independiente del dominio original.")
    print("Puedes subirlo a cualquier servidor web estático.")

if __name__ == "__main__":
    # Configuración
    site_directory = "/Users/edwarbechara/sitio_descargado/brujaefectiva.fun"
    original_domain = "brujaefectiva.fun"
    
    # Ejecutar limpieza
    process_site(site_directory, original_domain)