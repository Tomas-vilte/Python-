from pelicula import peliculas
from catalogoDePeliculas import catalogoDePeliculas as cp
opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Listar pelicula')
        print('3. Eliminar catalogo peliculas')
        print('4. Salir')
        opcion = int(input('Escibe tu opcion (1-4): '))

        if opcion == 1:
            nombrePelicula = input('Proporcione el nombre de la pelicula: ')
            pelicula = peliculas(nombrePelicula)
            cp.agregarPelicula(pelicula)
        elif opcion == 2:
            cp.listarPeiliculas()
        elif opcion == 3:
            cp.eliminarPelicula()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa....')