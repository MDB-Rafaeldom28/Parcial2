# Sistema de Gestión de Reparaciones de Electrodomésticos

Sistema web desarrollado en Flask para la gestión de reparaciones de electrodomésticos, incluyendo seguimiento de estado y generación de documentos.

## Características Principales
- Gestión de usuarios (técnicos/recepcionistas)
- Registro y seguimiento de reparaciones
- Consulta pública de estado de reparaciones
- Generación de notas de recepción
- Dashboard administrativo

## Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone [url-del-repositorio]
```

2. Crear un entorno virtual:
```bash
python -m venv venv
```

3. Activar el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

5. Configurar variables de entorno:
Crear un archivo `.env` en la raíz del proyecto con:
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
```

6. Inicializar la base de datos:
```bash
flask db init
flask db migrate
flask db upgrade
```

7. Ejecutar la aplicación:
```bash
flask run
```

## Uso
La aplicación estará disponible en `http://localhost:5000`

## Estructura del Proyecto
```
/app
  ├── __init__.py
  ├── models/
  ├── routes/
  ├── templates/
  ├── static/
  └── utils/
``` 