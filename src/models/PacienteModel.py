from database.db import get_connection #sacarlo afuera en app.py
from .entities.Paciente import Paciente 
from werkzeug.security import generate_password_hash

class PacienteModel():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            sql_query = '''SELECT id, dni, nombre, apellido, contrasenia, telefono, email, domicilio, obra_social,
            sexo, fecha_de_nacimiento FROM paciente WHERE 
            dni = %s'''
            cursor.execute(sql_query, (user.dni,))
            row = cursor.fetchone()
            if row != None: 
                paciente = Paciente(row[0], row[1], row[2], row[3], Paciente.check_password(row[4], user.contrasenia), row[5], row[6], row[7], row[8], row[9], row[10])
                return paciente
            else:
                return None
        except Exception as ex: 
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.cursor()
            sql_query = """SELECT id, dni, nombre, apellido, contrasenia, telefono, email, domicilio, obra_social,
            sexo, fecha_de_nacimiento FROM paciente WHERE 
            id = {}""".format(id)
            cursor.execute(sql_query)
            row = cursor.fetchone()
            if row != None: 
                return Paciente(row[0], row[1], row[2], row[3], None, row[4], row[5], row[6], row[7], row[8], row[9])
            else:
                None
        except Exception as ex: 
            raise Exception(ex)

    @classmethod
    def get_paciente(self, db, dni):
        try:
            cursor = db.cursor()
            sql_query = '''SELECT id, dni, nombre, apellido, contrasenia, telefono, email, domicilio, obra_social,
            sexo, fecha_de_nacimiento FROM paciente WHERE  
            dni = %s'''
            cursor.execute(sql_query, (dni,))
            row = cursor.fetchone()
            if row != None: 
                return row
            else:
                return None
        except Exception as ex: 
            raise Exception(ex)

    @classmethod
    def add_paciente(self,db, paciente): 
        try:
            cursor = db.cursor()
            hashed_password = generate_password_hash(paciente.contrasenia)
            cursor.execute("""INSERT INTO paciente (dni, nombre, apellido, contrasenia, telefono, email, domicilio, obra_social,
            sexo, fecha_de_nacimiento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (paciente.dni, paciente.nombre, paciente.apellido, hashed_password, paciente.telefono, paciente.email, paciente.domicilio, paciente.obra_social, 
            paciente.sexo,paciente.fecha_de_nacimiento))
               
            affected_rows = cursor.rowcount
            db.commit()
            return affected_rows
        except Exception as ex: 
            raise Exception(ex)

        