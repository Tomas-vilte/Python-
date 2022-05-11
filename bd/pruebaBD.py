import psycopg2

conexion = psycopg2.connect(user ='postgres', password ='admin', host ='localhost', port ='5432', database ='test_db')
try:
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
