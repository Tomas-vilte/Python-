import sqlite3
import csv


conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

archivo = open(r'/home/tomi/Python-/datos_db.txt', encoding = 'latin1')

filas = csv.reader(archivo)

#cursor.executemany('INSERT INTO estudiantes VALUES (?,?,?,?)', filas)

cursor.execute('SELECT * FROM estudiantes')
print(cursor.fetchall())

conexion.commit()
conexion.close()