from Persona import Persona 
class Ejecutivo(Persona):
    def __init__ (self, nombre, fechaNacimiento, curp, sexo, salario, biaticos, nivel):
        Persona.__init__(self, nombre, fechaNacimiento, curp, sexo)
        self.salario = salario
        self.biaticos = biaticos
        self.nivel = nivel        

    def __str__(self):
        return Persona.__str__(self) + ","  + "," + str(self.salario)

        