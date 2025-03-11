Sistema de Gestión de Reparaciones de Electrodomésticos
Sistema web desarrollado en Flask para la gestión de reparaciones de electrodomésticos, incluyendo seguimiento de estado y generación de documentos.

Características Principales
Gestión de usuarios (técnicos/recepcionistas)
Registro y seguimiento de reparaciones
Consulta pública de estado de reparaciones
Generación de notas de recepción
Dashboard administrativo
Requisitos
Python 3.8 o superior
pip (gestor de paquetes de Python)
Instalación
Clonar el repositorio:
git clone [url-del-repositorio]
Crear un entorno virtual:
python -m venv venv
Activar el entorno virtual:
Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate
Instalar dependencias:
pip install -r requirements.txt
Configurar variables de entorno: Crear un archivo .env en la raíz del proyecto con:
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
Inicializar la base de datos:
flask db init
flask db migrate
flask db upgrade
Ejecutar la aplicación:
flask run
Uso
La aplicación estará disponible en http://localhost:5000

Estructura del Proyecto
/app
  ├── __init__.py
  ├── models/
  ├── routes/
  ├── templates/
  ├── static/
  └── utils/
