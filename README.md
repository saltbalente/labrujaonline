# Sitio Web Estático - brujaefectiva.fun

Este sitio ha sido procesado y limpiado para ser completamente independiente del dominio original. Ahora es un sitio web estático que puede ser subido a cualquier servidor web.

## ✅ Cambios Realizados

### Archivos Eliminados:
- ❌ Archivos PHP (xmlrpc0db0.php)
- ❌ Directorios dinámicos (wp-json/, comments/feed/, feed/)
- ❌ Referencias a APIs de WordPress
- ❌ Scripts de tracking y analytics

### Contenido Limpiado:
- ✅ URLs absolutas convertidas a relativas
- ✅ Comentarios de HTTrack removidos
- ✅ Meta tags de WordPress removidos
- ✅ Referencias al dominio original eliminadas
- ✅ Scripts de Google Analytics removidos
- ✅ Enlaces a feeds RSS eliminados

## 📁 Estructura del Sitio

```
/
├── index.html              # Página principal
├── c.html                  # Página adicional
├── OPR/
│   └── index.html         # Página OPR
└── wp-content/
    ├── plugins/           # Archivos CSS y JS de plugins
    ├── themes/           # Archivos del tema
    └── uploads/          # Imágenes y recursos multimedia
```

## 🚀 Instrucciones de Subida

### Opción 1: Servidor Web Tradicional
1. Sube todos los archivos al directorio raíz de tu servidor web
2. Asegúrate de que `index.html` esté en la raíz
3. Configura tu servidor para servir archivos estáticos

### Opción 2: Servicios de Hosting Estático
- **Netlify**: Arrastra la carpeta completa a netlify.com/drop
- **Vercel**: Conecta con GitHub o sube directamente
- **GitHub Pages**: Sube a un repositorio y activa Pages
- **Firebase Hosting**: Usa `firebase deploy`

### Opción 3: CDN/Storage
- **AWS S3**: Configura bucket para hosting estático
- **Google Cloud Storage**: Habilita hosting de sitio web
- **Azure Blob Storage**: Configura para sitio web estático

## ⚙️ Configuración del Servidor

### Apache (.htaccess)
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.html [L]

# Habilitar compresión
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>
```

### Nginx
```nginx
server {
    listen 80;
    server_name tu-nuevo-dominio.com;
    root /path/to/site;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    # Habilitar compresión
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
}
```

## 🔧 Personalización

### Cambiar Enlaces de WhatsApp
Los enlaces de WhatsApp están configurados como `https://wa.link/mljar2`. Para cambiarlos:

1. Busca y reemplaza `https://wa.link/mljar2` en todos los archivos HTML
2. Usa tu propio enlace de WhatsApp Business

### Actualizar Metadatos
Edita los siguientes elementos en `index.html`:
- `<title>`: Título de la página
- `<meta name="description">`: Descripción SEO
- `<meta property="og:*">`: Metadatos de redes sociales

## 📱 Funcionalidades Mantenidas

- ✅ Diseño responsive
- ✅ Imágenes optimizadas
- ✅ Fuentes web locales
- ✅ Estilos CSS completos
- ✅ Funcionalidad de botones
- ✅ Enlaces de WhatsApp
- ✅ Estructura SEO básica

## ⚠️ Notas Importantes

1. **Dominio Nuevo**: Actualiza todas las referencias al dominio en metadatos
2. **SSL**: Configura certificado SSL para tu nuevo dominio
3. **Analytics**: Agrega nuevo código de Google Analytics si lo necesitas
4. **Backup**: Mantén una copia de seguridad de estos archivos
5. **Testing**: Prueba todas las funcionalidades en el nuevo dominio

## 🆘 Soporte

Si necesitas ayuda adicional:
1. Verifica que todos los archivos se hayan subido correctamente
2. Revisa los logs del servidor web para errores
3. Usa herramientas de desarrollo del navegador para debuggear
4. Asegúrate de que las rutas de archivos sean correctas

---

**¡Tu sitio está listo para ser independiente! 🎉**