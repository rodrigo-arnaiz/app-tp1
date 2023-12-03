from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Paciente( UserMixin ): 

    def __init__(self, id, dni, nombre, apellido, contrasenia, telefono, email, domicilio, obra_social, sexo, fecha_de_nacimiento) -> None: 
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = contrasenia
        self.telefono = telefono
        self.email = email
        self.domicilio = domicilio
        self.obra_social = obra_social
        self.sexo = sexo
        self.fecha_de_nacimiento = fecha_de_nacimiento

    
    @classmethod
    def check_password (self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    

    """ def to_JSON(self):
        return {
            'id': self.id,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'usuario': self.usuario,
            'contrasenia': self.contrasenia,
            'telefono': self.telefono,
            'email': self.email,
            'fecha_de_nacimiento': DateFormat.convert_date(self.fecha_de_nacimiento)
        } """