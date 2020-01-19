from datetime import datetime
from exinvent import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Insumo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(25), nullable=False)
    cant_previa=db.Column(db.Integer, nullable=False)
    pedido=db.Column(db.Integer, nullable=False)
    cant_actual=db.Column(db.Integer, nullable=False)
    venta_supuesta=db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Insumo('{self.nombre}', '{self.cant_previa}', '{self.pedido}','{self.cant_actual}', '{self.venta_supuesta}')"

    def __init__(self, id, nombre, cant_previa, pedido,  cant_actual, venta_supuesta):
        self.id=id
        self.nombre=nombre
        self.cant_actual=cant_actual
        self.pedido=pedido
        self.cant_previa=cant_previa
        self.venta_supuesta=venta_supuesta

class Venta(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(25), nullable=False)
    venta=db.Column(db.Integer, nullable=False)
    fecha= db.Column(db.DateTime, nullable=False, default= datetime.utcnow)

    def __repr__(self):
        return f"Venta('{self.nombre}', '{self.venta}', '{self.fecha}')"
