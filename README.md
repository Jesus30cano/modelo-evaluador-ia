# 🤖 Evaluador IA – Demo

> Demo de Inteligencia Artificial con servicio de evaluación semántica. Desplegado con **Docker** y **Docker Compose** para máxima portabilidad.

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Powered-brightgreen?style=for-the-badge)](https://github.com/Jesus30cano/modelo-evaluador-ia)

## 📋 Tabla de Contenidos
- [Requisitos](#-requisitos)
- [Instalación Rápida](#-instalación-rápida)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso](#-uso)
- [Comandos Útiles](#-comandos-útiles)
- [Configuración](#-configuración)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribución](#-contribución)

## 🛠️ Requisitos

Antes de comenzar, asegúrate de tener instalado:

| Herramienta | Versión Mínima | Comando de Verificación |
|-------------|----------------|-------------------------|
| **Git** | 2.0+ | `git --version` |
| **Docker** | 20.0+ | `docker --version` |
| **Docker Compose** | 2.0+ | `docker-compose --version` |

## 🚀 Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/Jesus30cano/modelo-evaluador-ia.git

# 2. Navegar al directorio
cd modelo-evaluador-ia

# 3. Construir y levantar los servicios
docker-compose up -d --build

# 4. Verificar que esté funcionando
curl http://localhost:8081/health || echo "Servicio iniciando..."
```

🎉 **¡Listo!** El servicio estará disponible en `http://localhost:8081`

## 📁 Estructura del Proyecto

```
evaluador-ia/
├── 🐳 docker-compose.yml      # Configuración de servicios
├── 🐳 Dockerfile              # Imagen personalizada
├── 🧠 evaluador_semantico.py  # Lógica de evaluación IA
├── 🌐 server.py               # Servidor web Flask/FastAPI
├── 📊 respuestas.csv          # Dataset de respuestas
├── 📦 requirements.txt        # Dependencias Python
└── 📖 README.md              # Este archivo
```

## 💻 Uso

### Verificar Estado del Servicio
```bash
# Ver servicios activos
docker-compose ps

# Ver logs en tiempo real
docker-compose logs -f evaluador-ia
```

### Acceso al Contenedor
```bash
# Entrar al contenedor para debugging
docker-compose exec evaluador-ia bash

# Instalar dependencias manualmente (si es necesario)
docker-compose exec evaluador-ia pip install -r requirements.txt
```

## 🔧 Comandos Útiles

### Gestión del Servicio
```bash
# Iniciar servicios
docker-compose up -d

# Parar servicios
docker-compose down

# Reconstruir completamente
docker-compose down && docker-compose up -d --build

# Ver logs específicos
docker-compose logs evaluador-ia
```

### Limpieza del Sistema
```bash
# Parar y limpiar completamente
docker-compose down -v --remove-orphans

# Limpiar imágenes y cachés no utilizados
docker system prune -f

# Limpiar todo (¡Cuidado! Elimina todas las imágenes)
docker system prune -af
```

## ⚙️ Configuración

### Puertos
El servicio está configurado para ejecutarse en:
- **Puerto Host**: `8081`
- **Puerto Contenedor**: `8080`

```yaml
ports:
  - "8081:8080"  # host:contenedor
```

### Variables de Entorno
Puedes personalizar la configuración creando un archivo `.env`:

```env
# .env
PORT=8080
DEBUG=true
MODEL_PATH=/app/models
CSV_PATH=/app/respuestas.csv
```

## 🩺 Solución de Problemas

### El servicio no inicia
```bash
# Verificar logs detallados
docker-compose logs -f evaluador-ia

# Verificar que el puerto no esté en uso
lsof -i :8081

# Reconstruir desde cero
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Error de permisos
```bash
# En Linux/Mac, verificar permisos
sudo chown -R $USER:$USER .

# Verificar Docker daemon
sudo systemctl status docker
```

### Problemas de red
```bash
# Verificar conectividad
docker network ls
docker-compose exec evaluador-ia ping google.com
```

## 🚨 Estado del Servicio

Puedes monitorear el estado del servicio de las siguientes formas:

```bash
# Verificar salud del contenedor
docker-compose ps

# Monitorear recursos
docker stats

# Verificar endpoint (si disponible)
curl http://localhost:8081/health
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Soporte

- **Issues**: [GitHub Issues](https://github.com/Jesus30cano/modelo-evaluador-ia/issues)
- **Autor**: [@Jesus30cano](https://github.com/Jesus30cano)

---

⭐ **¡No olvides darle una estrella al proyecto si te fue útil!**