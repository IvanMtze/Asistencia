-- Database: EmpleadoAsistencia

-- DROP DATABASE "EmpleadoAsistencia";

CREATE DATABASE "EmpleadoAsistencia"
    WITH 
    OWNER = gerardo
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
CREATE TABLE empleado(
	id SERIAL PRIMARY KEY,
	salario NUMERIC (10,3) NOT NULL,
	hora_entrada TIME NOT NULL,
	nombre TEXT NOT NULL,
	hora_salida TIME NOT NULL,
	fecha_nacimiento DATE NOT NULL,
	sexo CHAR(1),
	curp CHAR(18) NOT NULL
);

CREATE TABLE ejecutivo(
	id SERIAL PRIMARY KEY,
	salario NUMERIC (10,3) NOT NULL,
	biaticos NUMERIC (10,3) NOT NULL,
	nombre TEXT NOT NULL,
	nivel INTEGER NOT NULL,
	fecha_nacimiento DATE NOT NULL,
	sexo CHAR(1),
	curp CHAR(18) NOT NULL
);

CREATE TABLE asistenciaEmpleado(
	id SERIAL PRIMARY KEY,
	fecha DATE NOT NULL,
	id_empleado SERIAL REFERENCES empleado(id) NOT NULL
);

CREATE TABLE asistenciaEjecutivo(
	id SERIAL PRIMARY KEY,
	fecha DATE NOT NULL,
	id_ejecutivo SERIAL REFERENCES ejecutivo(id) NOT NULL
);

DROP TABLE asistenciaEjecutivo;
DROP TABLE asistenciaEmpleado;
DROP TABLE ejecutivo;
DROP TABLE empleado;
DROP TABLE infoEmpleado;