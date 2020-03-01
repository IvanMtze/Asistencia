import psycopg2
from Empleado import Empleado

class DAOEmpleado(object):
    def insertaEmpleado(self, empleado):
        try:
            connection = psycopg2.connect(user="gerardo@empleadosparadigmas",
                                        password="Trikitrakes1",
                                        host="empleadosparadigmas.postgres.database.azure.com",
                                        port="5432",
                                        database="EmpleadoAsistencia")

            cursor = connection.cursor()

            # Update single record now
            sql_insert_query = """INSERT INTO empleado (salario, hora_entrada,
            nombre, hora_salida, fecha_nacimiento, sexo, curp) 
            VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql_insert_query, (empleado.salario, empleado.hrEntrada, empleado.nombre,
                                            empleado.hrSalida, empleado.fechaNacimiento, empleado.sexo, empleado.curp))

            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


    def getEmpleados(self):


        try:
            connection = psycopg2.connect(user="gerardo@empleadosparadigmas",
                                        password="Trikitrakes1",
                                        host="empleadosparadigmas.postgres.database.azure.com",
                                        port="5432",
                                        database="EmpleadoAsistencia",
                                        sslmode='true')

            cursor = connection.cursor()

            # Update single record now
            sql_insert_query = """
                SELECT * FROM empleado
                """
            cursor.execute(sql_insert_query)

            return cursor.fetchall()

        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
