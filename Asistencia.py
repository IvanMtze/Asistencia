class Asistencia(object):
    def __init__ (self, fecha, id_empleado):
        self.fecha = fecha
        self.id_empleado = id_empleado

    def __str__(self):
        return self.fecha + " , "  + self.id_empleado

        