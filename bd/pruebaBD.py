import psycopg2

conexion = psycopg2.connect(user ='postgres', password ='admin', host ='localhost', port ='5432', database ='test_db')

#Haciendo consulta sql y mostrando los registros en la terminal
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

try:
    with conexion:
         with conexion.cursor() as cursor:
             consulta = " INSERT INTO persona (nombre, apellido, email, lenguaje_preferido) VALUES (%s, %s, %s, %s) "
             valores = ('Michu', 'Vilte', 'michuvilte@gmail.com', 'Solidity')
             cursor.execute(consulta, valores)
             registrosInsertados = cursor.rowcount
             print(f'Registros insertados: {registrosInsertados}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    cursor.close()


