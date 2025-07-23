// Protección avanzada contra copia y scraping
(function() {
    'use strict';
    
    // Variables de configuración
    const config = {
        blockRightClick: true,
        blockTextSelection: true,
        blockKeyboardShortcuts: true,
        detectDevTools: true,
        obfuscateContent: true,
        preventIframeEmbedding: true,
        detectExtensions: true,
        showWarnings: true
    };

    // Función para mostrar advertencias
    function showWarning(message) {
        if (!config.showWarnings) return;
        
        const warning = document.createElement('div');
        warning.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #ff4444;
            color: white;
            padding: 15px;
            border-radius: 5px;
            z-index: 999999;
            font-family: Arial, sans-serif;
            font-size: 14px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        `;
        warning.textContent = message;
        document.body.appendChild(warning);
        
        setTimeout(() => {
            if (warning.parentNode) {
                warning.parentNode.removeChild(warning);
            }
        }, 3000);
    }

    // Deshabilitar clic derecho
    if (config.blockRightClick) {
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
            showWarning('⚠️ Clic derecho deshabilitado por seguridad');
            return false;
        });
    }

    // Deshabilitar selección de texto
    if (config.blockTextSelection) {
        document.addEventListener('selectstart', function(e) {
            e.preventDefault();
            return false;
        });
        
        document.addEventListener('dragstart', function(e) {
            e.preventDefault();
            return false;
        });
        
        // CSS para deshabilitar selección
        const style = document.createElement('style');
        style.textContent = `
            * {
                -webkit-user-select: none !important;
                -moz-user-select: none !important;
                -ms-user-select: none !important;
                user-select: none !important;
                -webkit-touch-callout: none !important;
                -webkit-tap-highlight-color: transparent !important;
            }
            input, textarea {
                -webkit-user-select: text !important;
                -moz-user-select: text !important;
                -ms-user-select: text !important;
                user-select: text !important;
            }
        `;
        document.head.appendChild(style);
    }

    // Deshabilitar atajos de teclado
    if (config.blockKeyboardShortcuts) {
        document.addEventListener('keydown', function(e) {
            // F12 - Developer Tools
            if (e.keyCode === 123) {
                e.preventDefault();
                showWarning('🚫 Herramientas de desarrollador bloqueadas');
                return false;
            }
            
            // Ctrl+Shift+I - Developer Tools
            if (e.ctrlKey && e.shiftKey && e.keyCode === 73) {
                e.preventDefault();
                showWarning('🚫 Herramientas de desarrollador bloqueadas');
                return false;
            }
            
            // Ctrl+Shift+J - Console
            if (e.ctrlKey && e.shiftKey && e.keyCode === 74) {
                e.preventDefault();
                showWarning('🚫 Consola bloqueada');
                return false;
            }
            
            // Ctrl+U - View Source
            if (e.ctrlKey && e.keyCode === 85) {
                e.preventDefault();
                showWarning('🚫 Ver código fuente bloqueado');
                return false;
            }
            
            // Ctrl+S - Save Page
            if (e.ctrlKey && e.keyCode === 83) {
                e.preventDefault();
                showWarning('🚫 Guardar página bloqueado');
                return false;
            }
            
            // Ctrl+A - Select All
            if (e.ctrlKey && e.keyCode === 65) {
                e.preventDefault();
                showWarning('🚫 Seleccionar todo bloqueado');
                return false;
            }
            
            // Ctrl+C - Copy
            if (e.ctrlKey && e.keyCode === 67) {
                e.preventDefault();
                showWarning('🚫 Copiar bloqueado');
                return false;
            }
            
            // Ctrl+V - Paste
            if (e.ctrlKey && e.keyCode === 86) {
                e.preventDefault();
                return false;
            }
            
            // Ctrl+X - Cut
            if (e.ctrlKey && e.keyCode === 88) {
                e.preventDefault();
                showWarning('🚫 Cortar bloqueado');
                return false;
            }
            
            // Ctrl+P - Print
            if (e.ctrlKey && e.keyCode === 80) {
                e.preventDefault();
                showWarning('🚫 Imprimir bloqueado');
                return false;
            }
            
            // Ctrl+Shift+C - Inspect Element
            if (e.ctrlKey && e.shiftKey && e.keyCode === 67) {
                e.preventDefault();
                showWarning('🚫 Inspeccionar elemento bloqueado');
                return false;
            }
        });
    }

    // Detectar herramientas de desarrollador
    if (config.detectDevTools) {
        let devtools = {
            open: false,
            orientation: null
        };
        
        const threshold = 160;
        
        setInterval(function() {
            if (window.outerHeight - window.innerHeight > threshold || 
                window.outerWidth - window.innerWidth > threshold) {
                if (!devtools.open) {
                    devtools.open = true;
                    showWarning('🚨 Herramientas de desarrollador detectadas');
                    // Opcional: redirigir o ocultar contenido
                    document.body.style.display = 'none';
                    setTimeout(() => {
                        document.body.style.display = 'block';
                    }, 2000);
                }
            } else {
                devtools.open = false;
            }
        }, 500);
        
        // Detectar usando console
        let devToolsChecker = () => {
            let before = new Date();
            debugger;
            let after = new Date();
            if (after - before > 100) {
                showWarning('🚨 Debugger detectado');
            }
        };
        
        setInterval(devToolsChecker, 1000);
    }

    // Ofuscar contenido
    if (config.obfuscateContent) {
        // Cambiar título dinámicamente
        let originalTitle = document.title;
        let fakeTitles = [
            'Error 404 - Página no encontrada',
            'Acceso denegado',
            'Sitio en mantenimiento',
            'Contenido no disponible'
        ];
        
        setInterval(() => {
            if (document.hidden) {
                document.title = fakeTitles[Math.floor(Math.random() * fakeTitles.length)];
            } else {
                document.title = originalTitle;
            }
        }, 1000);
        
        // Agregar elementos DOM falsos
        setTimeout(() => {
            for (let i = 0; i < 10; i++) {
                let fakeDiv = document.createElement('div');
                fakeDiv.style.display = 'none';
                fakeDiv.innerHTML = `<!-- Fake content ${i} -->`;
                fakeDiv.setAttribute('data-fake', 'true');
                document.body.appendChild(fakeDiv);
            }
        }, 2000);
    }

    // Prevenir embedding en iframe
    if (config.preventIframeEmbedding) {
        if (window.top !== window.self) {
            window.top.location = window.self.location;
        }
    }

    // Detectar extensiones del navegador
    if (config.detectExtensions) {
        // Detectar extensiones comunes de scraping
        const extensionDetectors = [
            'chrome-extension://',
            'moz-extension://',
            'safari-extension://',
            'ms-browser-extension://'
        ];
        
        setTimeout(() => {
            extensionDetectors.forEach(ext => {
                if (window.location.href.includes(ext)) {
                    showWarning('🚨 Extensión de navegador detectada');
                }
            });
        }, 1000);
    }

    // Protección adicional contra bots
    const botDetection = () => {
        // Verificar si es un bot basado en características del navegador
        const isBot = (
            !window.navigator.webdriver === undefined ||
            window.navigator.webdriver === true ||
            window.callPhantom ||
            window._phantom ||
            window.phantom ||
            window.Buffer ||
            window.emit ||
            window.spawn
        );
        
        if (isBot) {
            document.body.innerHTML = '<h1>Acceso no autorizado</h1>';
            return;
        }
    };
    
    // Ejecutar detección de bots
    setTimeout(botDetection, 100);
    
    // Protección contra headless browsers
    const headlessDetection = () => {
        const isHeadless = (
            !window.navigator.plugins.length ||
            !window.navigator.languages ||
            window.navigator.webdriver ||
            window.outerWidth === 0 ||
            window.outerHeight === 0
        );
        
        if (isHeadless) {
            document.body.innerHTML = '<h1>Navegador no compatible</h1>';
            return;
        }
    };
    
    setTimeout(headlessDetection, 200);
    
    // Limpiar consola periódicamente
    setInterval(() => {
        console.clear();
        console.log('%c🚫 ACCESO RESTRINGIDO', 'color: red; font-size: 30px; font-weight: bold;');
        console.log('%cEste sitio está protegido contra copia y scraping.', 'color: red; font-size: 16px;');
    }, 1000);
    
    // Protección final
    window.addEventListener('beforeunload', function() {
        // Limpiar datos sensibles antes de cerrar
        sessionStorage.clear();
        localStorage.clear();
    });
    
    console.log('🛡️ Sistema de protección activado');
    
})();