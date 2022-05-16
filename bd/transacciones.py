import psycopg2 as bd


conexion = bd.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            cursor = conexion.cursor()
            consulta = "INSERT INTO persona(nombre, apellido, email, lenguaje_preferido) VALUES (%s, %s, %s, %s)"
            valores = ('Alex', 'Perez', 'Alexperez@gmail.com', 'Matlab')
            cursor.execute(consulta, valores)


            conuslta = "UPDATE persona SET nombre=%s, apellido=%s, email=%s, lenguaje_preferido=%s WHERE id_persona=%s"
            valores = 'Juan', 'Del balle', 'Juanperez@gmail.com', 'Python, 22'
            cursor.execute(consulta, valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    cursor.close()
print('Termina la transsacion, se hizo commit')
    