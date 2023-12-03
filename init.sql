CREATE TABLE paciente 
    (id serial, 
    dni bigint unique not null, 
    nombre varchar(50) not null, 
    apellido varchar(50) not null,
    contrasenia varchar(200) not null,
    telefono varchar(40),
    email varchar(40) not null,
    domicilio varchar(50),
    obra_social varchar(30) not null,
    sexo varchar(10),
    fecha_de_nacimiento date);
