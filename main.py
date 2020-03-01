from Empleado import Empleado
import datetime
import time
from Ejecutivo import Ejecutivo
from DAOEjecutivo import DAOEjecutivo
from DAOAsistencias import DAOAsistencias
from DAOEmpleado import DAOEmpleado
from Asistencia import Asistencia



def muestraMenu():
    print("Presione una opción")
    print("1.- Alta de empleado")
    print("2.- Alta de ejecutivo")
    print("3.- registrar asistencia de empleado")
    print("4.- Mostrar nomina")

def menu(opcion):
    if(opcion == 1):
        altaEmpleado()
    elif(opcion == 2):
        altaEjecutivo()
    elif(opcion == 3):
        registrarAsistencia()
    elif(opcion == 4):
        mostrarNomina()

def altaEmpleado():
    nombre = str(input("Ingrese el nombre del empleado: "))
    fechaNacimiento = input('ingresa la fecha de nacimiento (YYYY-MM-DD): ')
    year, month, day = map(int, fechaNacimiento.split('-'))
    fecha = datetime.date(year, month, day)
    curp = str(input("Ingrese la curp: "))
    sexo = str(input("Ingrese el genero (H/M): "))
    horaEntrada = datetime.datetime.strptime(input('Ingrese la hora de entrada en el formato: '),"%H:%M")
    horaSalida = datetime.datetime.strptime(input('Ingrese la hora de salida en el formato HHMM: '),"%H:%M")
    salario = float(input("Ingrese el salario: "))

    empleado = Empleado(nombre, fecha, curp, sexo, horaEntrada, horaSalida, salario)

    dao = DAOEmpleado()
    dao.insertaEmpleado(empleado)
    
def altaEjecutivo():
    nombre = str(input("Ingrese el nombre del empleado: "))
    fechaNacimiento = input('ingresa la fecha de nacimiento (YYYY-MM-DD): ')
    year, month, day = map(int, fechaNacimiento.split('-'))
    fecha = datetime.date(year, month, day)
    curp = str(input("Ingrese la curp: "))
    sexo = str(input("Ingrese el genero (H/M): "))
    salario = float(input("Ingrese el salario: "))
    biaticos = float(input("Ingrese los biaticos: "))
    nivel = int(input("Ingrese el nivel: "))
    
    ejecutivo = Ejecutivo(nombre, fecha, curp, sexo, salario, biaticos, nivel)
    dao = DAOEjecutivo()
    dao.insertaEjecutivo(ejecutivo)

def registrarAsistencia():
    fecha = input('ingresa la fecha de asistencia (YYYY-MM-DD): ')
    year, month, day = map(int, fecha.split('-'))
    fechaAsistencia = datetime.date(year, month, day)

    id = int(input("Ingresa el id del empleado: "))
    dao  = DAOAsistencias()
    dao.insertaEmpleado(Asistencia(fechaAsistencia, id))

def mostrarNomina():
    pass

if __name__ == "__main__":
    muestraMenu()
    opcion = int(input("Seleccione: "))
    menu(opcion)