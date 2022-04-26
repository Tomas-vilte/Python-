try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos informacion al archivo\n')
    archivo.write('Adios')
except FileExistsError as e:
    print(f'Este archivo no se encuentra en la ruta - Ocurrio un error: {e}')
finally:
    archivo.close()
    print('Fin del archivo')
    #archivo.write('Nueva info')