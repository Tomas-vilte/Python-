import sqlite3

conexion = sqlite3.connect("usuarios.db")

#Creamos cursor
cursor = conexion.cursor()
#Creamos la tabla estudiantes

#cursor.execute('CREATE TABLE estudiantes (email VARCHAR(100), carrera VARCHAR(100), nombre VARCHAR(100), edad INTEGER)')

#Insertamos un registro en la tabla


#cursor.execute("INSERT INTO estudiantes VALUES ('bluenote@googlemail.com','Artes','Sharon', 27)")

#Seleccionamos todos los registros en la tabla
cursor.execute('SELECT * FROM estudiantes')
usuario = cursor.fetchall()
print(usuario)

usuarios = [
    ('Pedro123@mail.com', 'Programador', 'Pedro', 26),
    ('Mariadb@oulok.com', 'Recrutadora', 'Maria', 24),
    ('Joseperez@yaho.com', 'Contador', 'Jose', 26),
    ('Roxanalopez@hotmail.com', 'Psicologa', 'Roxana', 28)
]
#cursor.executemany('INSERT INTO estudiantes VALUES (?,?,?,?)', usuarios)


# Guardamos los cambios haciendo commit
conexion.commit()

conexion.close()