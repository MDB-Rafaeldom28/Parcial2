from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
import random
import string

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    reparaciones = db.relationship('Reparacion', backref='tecnico', lazy=True)

class Reparacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(8), unique=True, nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Datos del cliente
    nombre_cliente = db.Column(db.String(100), nullable=False)
    telefono_cliente = db.Column(db.String(20), nullable=False)
    email_cliente = db.Column(db.String(120))
    direccion_cliente = db.Column(db.String(200))
    
    # Datos del electrodoméstico
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    numero_serie = db.Column(db.String(50))
    descripcion_problema = db.Column(db.Text, nullable=False)
    observaciones = db.Column(db.Text)
    
    # Estado y seguimiento
    estado = db.Column(db.String(20), nullable=False, default='Recibido')  # Recibido/En Proceso/Terminado
    condiciones_recepcion = db.Column(db.Text)
    tecnico_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    
    def __init__(self, **kwargs):
        super(Reparacion, self).__init__(**kwargs)
        if not self.codigo:
            self.codigo = self.generar_codigo()
    
    @staticmethod
    def generar_codigo():
        caracteres = string.ascii_uppercase + string.digits
        while True:
            codigo = ''.join(random.choices(caracteres, k=8))
            if not Reparacion.query.filter_by(codigo=codigo).first():
                return codigo 