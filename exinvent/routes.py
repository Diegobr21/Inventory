from flask import render_template, url_for, flash, redirect, request
from datetime import datetime
import time
from exinvent import app
from exinvent.forms import RegistrationForm, LoginForm
from exinvent.clases import User, Insumo, Venta

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route("/",  methods=['GET', 'POST'])
def main():
    context = { 'server_time': format_server_time() }
    return render_template('index.html', context=context)


@app.route('/act_fmyog', methods=['GET', 'POST'])
def act_fmyog():
    if request.method=='POST':
        """cant_act=request.form['act_cant_fmyog']
        cant_pre=db.child("insumos").child("form_yog").child("cant_actual").get().val()
        db.child("insumos").child("form_yog").child("cant_previa").push(cant_pre)

        db.child("insumos").child("form_yog").child("cant_actual").push(cant_act)
    """

    return render_template('index.html')

@app.route('/credenciales', methods=['GET', 'POST'])
def credenciales():
    if (request.method == 'POST'):
            email = request.form['correo']
            password = request.form['password']
            try:
                user = User.query.filter_by(email).first()
                user_psw=User.query.filter_by(password).first()               
                return render_template('inventario.html')
            except:
                unsuccessful = 'Acceso denegado'
                print ('usuario {} no autorizado'.format(email))
                flash('Acceso denegado. Checa correo y contraseña', 'danger')
                # return render_template('credenciales.html', us=unsuccessful)
                
    return render_template('credenciales.html')

    