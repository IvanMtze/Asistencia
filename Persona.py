
class Persona(object):
    def __init__(self, nombre, fechaNacimiento, curp, sexo):
        self.nombre = nombre
        self.curp = curp
        self.sexo = sexo
        self.fechaNacimiento = fechaNacimiento

    def __str__(self):
        return self.nombre + "," + self.curp + "," + self.sexo + "," + self.fechaNacimiento 
    
    def obtenerSalario(self):
        pass
