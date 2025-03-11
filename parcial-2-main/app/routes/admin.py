from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.models.models import Reparacion
from app import db
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    estado_filtro = request.args.get('estado', '')
    if estado_filtro:
        reparaciones = Reparacion.query.filter_by(estado=estado_filtro).all()
    else:
        reparaciones = Reparacion.query.all()
    return render_template('admin/dashboard.html', reparaciones=reparaciones)

@admin_bp.route('/reparacion/nueva', methods=['GET', 'POST'])
@login_required
def nueva_reparacion():
    if request.method == 'POST':
        nueva_reparacion = Reparacion(
            nombre_cliente=request.form['nombre_cliente'],
            telefono_cliente=request.form['telefono_cliente'],
            email_cliente=request.form['email_cliente'],
            direccion_cliente=request.form['direccion_cliente'],
            marca=request.form['marca'],
            modelo=request.form['modelo'],
            numero_serie=request.form['numero_serie'],
            descripcion_problema=request.form['descripcion_problema'],
            observaciones=request.form['observaciones'],
            condiciones_recepcion=request.form['condiciones_recepcion'],
            tecnico_id=current_user.id
        )
        
        db.session.add(nueva_reparacion)
        db.session.commit()
        
        flash('Reparación registrada exitosamente')
        return redirect(url_for('admin.dashboard'))
        
    return render_template('admin/nueva_reparacion.html')

@admin_bp.route('/reparacion/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_reparacion(id):
    reparacion = Reparacion.query.get_or_404(id)
    
    if request.method == 'POST':
        reparacion.nombre_cliente = request.form['nombre_cliente']
        reparacion.telefono_cliente = request.form['telefono_cliente']
        reparacion.email_cliente = request.form['email_cliente']
        reparacion.direccion_cliente = request.form['direccion_cliente']
        reparacion.marca = request.form['marca']
        reparacion.modelo = request.form['modelo']
        reparacion.numero_serie = request.form['numero_serie']
        reparacion.descripcion_problema = request.form['descripcion_problema']
        reparacion.observaciones = request.form['observaciones']
        reparacion.estado = request.form['estado']
        
        db.session.commit()
        flash('Reparación actualizada exitosamente')
        return redirect(url_for('admin.dashboard'))
        
    return render_template('admin/editar_reparacion.html', reparacion=reparacion)

@admin_bp.route('/reparacion/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_reparacion(id):
    reparacion = Reparacion.query.get_or_404(id)
    db.session.delete(reparacion)
    db.session.commit()
    flash('Reparación eliminada exitosamente')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/reparacion/<int:id>/estado', methods=['POST'])
@login_required
def actualizar_estado(id):
    reparacion = Reparacion.query.get_or_404(id)
    nuevo_estado = request.form.get('estado')
    if nuevo_estado in ['Recibido', 'En Proceso', 'Terminado']:
        reparacion.estado = nuevo_estado
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'error': 'Estado inválido'}), 400 