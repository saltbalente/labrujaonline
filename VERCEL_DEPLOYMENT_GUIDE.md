# Guía de Despliegue en Vercel - Bruja Efectiva

## 📋 Archivos Preparados para Vercel

### ✅ Archivos de Configuración
- **`vercel.json`** - Configuración principal de Vercel con headers de seguridad
- **`robots.txt`** - Bloqueo de scrapers optimizado para Vercel
- **`.htaccess`** - Protección adicional (funciona si Vercel usa Apache)

### ✅ Protecciones Implementadas
- **`protection.js`** - Script avanzado anti-copia y anti-scraping
- Headers de seguridad configurados en `vercel.json`
- Meta tags de seguridad en todos los archivos HTML

## 🚀 Pasos para Desplegar en Vercel

### 1. Preparar el Repositorio
```bash
# Si no tienes git inicializado
git init
git add .
git commit -m "Sitio preparado para Vercel con protecciones"
```

### 2. Subir a GitHub/GitLab
- Crea un repositorio en GitHub o GitLab
- Sube tu código al repositorio

### 3. Conectar con Vercel
1. Ve a [vercel.com](https://vercel.com)
2. Conecta tu cuenta de GitHub/GitLab
3. Importa tu repositorio
4. Vercel detectará automáticamente que es un sitio estático

### 4. Configuración Automática
Vercel usará automáticamente:
- `vercel.json` para headers de seguridad
- `robots.txt` para bloquear scrapers
- Los archivos HTML con protecciones JavaScript

## 🛡️ Protecciones Activas en Vercel

### Headers de Seguridad (via vercel.json)
- ✅ X-Frame-Options: DENY
- ✅ X-Content-Type-Options: nosniff
- ✅ X-XSS-Protection: 1; mode=block
- ✅ Referrer-Policy: no-referrer
- ✅ Content-Security-Policy
- ✅ Strict-Transport-Security
- ✅ Permissions-Policy

### Bloqueo de Scrapers
- ✅ HTTrack bloqueado via robots.txt
- ✅ wget, curl, python-requests bloqueados
- ✅ Protección JavaScript contra copia de código

### Protecciones del Cliente
- ✅ Clic derecho deshabilitado
- ✅ Selección de texto bloqueada
- ✅ Herramientas de desarrollador bloqueadas
- ✅ Atajos de teclado deshabilitados
- ✅ Detección de bots y extensiones

## 📝 Notas Importantes

### Archivos Eliminados
- ❌ `wp-config.php` - No necesario para Vercel (era específico de PHP/WordPress)

### Archivos Optimizados
- ✅ `vercel.json` - Configuración específica para Vercel
- ✅ `robots.txt` - Simplificado y optimizado
- ✅ `.htaccess` - Mantenido como respaldo (funciona si Vercel usa Apache)

## 🔧 Configuración Post-Despliegue

Una vez desplegado en Vercel:

1. **Verificar Headers**: Usa herramientas como [securityheaders.com](https://securityheaders.com) para verificar que los headers de seguridad estén activos

2. **Probar Protecciones**: 
   - Intenta clic derecho (debe estar bloqueado)
   - Intenta F12 (debe mostrar advertencia)
   - Verifica que robots.txt esté accesible en `tudominio.com/robots.txt`

3. **Monitorear**: Vercel proporciona analytics para monitorear intentos de acceso

## 🌐 URL Final
Una vez desplegado, tu sitio estará disponible en:
- URL temporal de Vercel: `https://tu-proyecto.vercel.app`
- Dominio personalizado: `https://brujaefectiva.fun` (si configuras el dominio)

## ⚠️ Recomendaciones Adicionales

1. **Dominio Personalizado**: Configura tu dominio personalizado en Vercel para mejor SEO
2. **SSL Automático**: Vercel proporciona SSL automático
3. **CDN Global**: Tu sitio se servirá desde CDN global de Vercel
4. **Monitoreo**: Revisa regularmente los logs de Vercel para detectar intentos de scraping

¡Tu sitio está listo para desplegarse en Vercel con máxima protección! 🛡️