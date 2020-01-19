
from flask import Flask, render_template, request, redirect
import os
from datetime import datetime
from datetime import date
import time
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:Diegobr21@database-1.coq2c5qjnkpo.us-east-2.rds.amazonaws.com:3306/database-1' #'sqlite:///inventario.db'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///inventario.db'
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.email}')"

class Insumo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(25), nullable=False)
    cant_previa=db.Column(db.Integer, nullable=False)
    pedido=db.Column(db.Integer, nullable=False)
    cant_actual=db.Column(db.Integer, nullable=False)
    #venta_supuesta=db.Column(db.Integer, nullable=False)

    @staticmethod
    def get_all():
        return Insumo.query.all()

    def __repr__(self):
        return f"Insumo('{self.nombre}', '{self.cant_previa}', '{self.pedido}')"

    def __init__(self, nombre, cant_previa, pedido,  cant_actual):
        self.nombre=nombre
        self.cant_actual=cant_actual
        self.pedido=pedido
        self.cant_previa=cant_previa
        #self.venta_supuesta=venta_supuesta

class Venta(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(25), nullable=False)
    venta=db.Column(db.Integer, nullable=False)
    fecha= db.Column(db.DateTime, nullable=False, default= datetime.utcnow)

    def __repr__(self):
        return f"Venta('{self.nombre}', '{self.venta}', '{self.fecha}')"


#user=auth.sign_in_with_email_and_password(email, pssd)
#auth.get_account_info(user['idToken'])
def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

def format_server_date():
  today = date.today()
  d1 = today.strftime("%d/%m/%Y")
  return d1 #date.strftime("%B %d %Y", today)



@app.route("/",  methods=['GET', 'POST'])
def main():
    insumos=Insumo.get_all()
    context = {'Fecha': format_server_date(), 'Hora': format_server_time()}
    return render_template('index.html', insumos=insumos, context=context)

    
@app.route('/actualizar_insumo', methods=['GET', 'POST'])
def act_fmyog():
    if (request.method == 'POST'):    
        msg_act='Contenido actualizado!'  
        cantidad_actual=[]
        nom=[]  
        insumos=Insumo.get_all()

        for insu in insumos:
            nom.append(insu.nombre)
        for n in range(len(insumos)):
            #cantidad_actual.append(request.form[nom[n]])
            cantidad_actual.append(request.form[nom[n]])

    
        print(cantidad_actual)
        print(nom)
        """if lactualizacionescorrectaenlabd:
            msg_act='Contenido actualizado!'
            
        
        cant_act=request.form['act_cant_fmyog']
        cant_pre=db.child("insumos").child("form_yog").child("cant_actual").get().val()
        db.child("insumos").child("form_yog").child("cant_previa").push(cant_pre)

        db.child("insumos").child("form_yog").child("cant_actual").push(cant_act)
    """

    return render_template('index.html', ac=msg_act)

@app.route('/credenciales', methods=['GET', 'POST'])
def credenciales():
    if (request.method == 'POST'):
            email1 = request.form['correo']
            password = request.form['password']
                        
            user = User.query.filter_by(email=email1).first()
            if password == user.password:          
                print (' Hola, {} !'.format(email1)) 
                print ('contraseña: {} '.format(user.password))
                insumos=Insumo.get_all()
                context = {'Fecha': format_server_date()}
                return render_template('inventario.html', insumos=insumos, context=context)
            elif password!= user.password:
                unsuccessful = 'Acceso denegado'
                print ('usuario {} no autorizado'.format(email1))
                #flash('Acceso denegado. Checa correo y contraseña', 'danger')
                return render_template('credenciales.html', us=unsuccessful)
                
    return render_template('credenciales.html')

    
if __name__== "__main__":
    app.run(debug=True)
    