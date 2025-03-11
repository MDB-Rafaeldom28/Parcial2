from flask import Blueprint, render_template, request, jsonify
from app.models.models import Reparacion
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        reparacion = Reparacion.query.filter_by(codigo=codigo).first()
        if reparacion:
            return jsonify({
                'estado': reparacion.estado,
                'nombre_cliente': reparacion.nombre_cliente,
                'marca': reparacion.marca,
                'modelo': reparacion.modelo,
                'fecha_registro': reparacion.fecha_registro.strftime('%d/%m/%Y')
            })
        return jsonify({'error': 'Reparación no encontrada'}), 404
    return render_template('consulta.html') 