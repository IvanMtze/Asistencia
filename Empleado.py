from Persona import Persona
class Empleado(Persona):
    def __init__ (self, nombre, fechaNacimiento, curp, sexo, hrEntrada, hrSalida, salario):
        Persona.__init__(self, nombre, fechaNacimiento, curp, sexo)
        self.hrEntrada = hrEntrada
        self.hrSalida = hrSalida
        self.salario = salario

    def __str__(self):
        return Persona.__str__(self) + "," + str(self.hrEntrada) + "," + str(self.hrSalida) + "," + str(self.salario)

