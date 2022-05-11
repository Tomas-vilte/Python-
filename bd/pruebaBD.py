import psycopg2

conexion = psycopg2.connect(user ='postgres', password ='admin', host ='localhost', port ='5432', database ='test_db')

#Haciendo consulta "SELECT" y mostrando los registros en la terminal
"""try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta =" SELECT * FROM persona WHERE id_persona IN %s"
            #llavesPrimarias = ((1,2,3),)
            entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            llavesPrimarias = (tuple(entrada.split(',')),)
            cursor.execute(consulta, llavesPrimarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:

    cursor.close()

"""

#Insertando nuevo registro en la base de datos
"""try:
    with conexion:
         with conexion.cursor() as cursor:
             consulta = " INSERT INTO persona (nombre, apellido, email, lenguaje_preferido) VALUES (%s, %s, %s, %s) "
             valores = (
                 ('Marcos', 'Cantu', 'Marcoscantu@gmail.com', 'R'),
                 ('Angel', 'Quitana', 'Angelquintana@gmail.com', 'Ruby'),
                 ('Maria', 'Gonzalez', 'Mariagonzalez@gmail.com', 'C++')
                 )
             cursor.executemany(consulta, valores)
             registrosInsertados = cursor.rowcount
             print(f'Registros insertados: {registrosInsertados}')
except Exception as e:
    print(f'Ocurrio un error {e}')  
finally:
    cursor.close()

"""
#Actualizando registro de la base de datos (UPDATE)
"""try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = " UPDATE persona SET nombre =%s, apellido=%s, email=%s, lenguaje_preferido=%s WHERE id_persona=%s   "
            valores = (
                ('Juan carlos', 'Juarez', 'Juanjuarez@gmail.com', '.NET', 16))
            cursor.execute(consulta, valores)
            registrosModificados = cursor.rowcount
            print(f'RegistrosActualizados: {registrosModificados}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    cursor.close()

"""