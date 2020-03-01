import psycopg2
from Ejecutivo import Ejecutivo

class DAOEjecutivo:
    def insertaEjecutivo(self,ejecutivo):
        try:
            connection = psycopg2.connect(user="gerardo@empleadosparadigmas",
                                        password="Trikitrakes1",
                                        host="empleadosparadigmas.postgres.database.azure.com",
                                        port="5432",
                                        database="EmpleadoAsistencia")

            cursor = connection.cursor()

            # Update single record now
            sql_insert_query = """INSERT INTO ejecutivo (salario, nombre,
            biaticos, nivel, fecha_nacimiento, sexo, curp) 
            VALUES (%s,%s,%s,%s,%s,%s, %s)"""
            cursor.execute(sql_insert_query, (ejecutivo.salario, ejecutivo.nombre, ejecutivo.biaticos,
                                            ejecutivo.nivel, ejecutivo.fechaNacimiento, ejecutivo.sexo, ejecutivo.curp))

            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


    def getEjecutivos(self):


        try:
            connection = psycopg2.connect(user="gerardo@empleadosparadigmas",
                                        password="Trikitrakes1",
                                        host="empleadosparadigmas.postgres.database.azure.com",
                                        port="5432",
                                        database="EmpleadoAsistencia")

            cursor = connection.cursor()

            # Update single record now
            sql_insert_query = """
                SELECT * FROM ejecutivo
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