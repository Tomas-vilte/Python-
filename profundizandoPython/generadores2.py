def generalPares(limite):
    num = 1

    while num<limite:
        yield num*2
        num = num+1

devuelvePares = generalPares(10)

print(next(devuelvePares))

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subElemnto in elemento:
            yield from elemento

ciudadesDevueltas = devuelveCiudades('Madrid', 'Barcelona', 'Buenos aires', 'Valencia')
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))