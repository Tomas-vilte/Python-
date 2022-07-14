# Profundizando en set
# Un set es una coleccion de elementos unicos y es mutables
# Los elementos de un set deben ser inmutables
#conjunto = {[1,2], [3,4]}

#conjunto = {[1,2],[3,4]}

conjunto = {'Juan', True, 12.1}
print(conjunto)

# Set vacio
#conjunto = {}
#print(type(conjunto)) Genera un diccionario vacio

# Set vacio correcto
conjunto = set()
print(type(conjunto))

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores unicos
conjunto.add('Juan')
print(conjunto)

# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)

# Podemos agregar mas elementos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,50])
print(conjunto)

# Copiar un set (copia poca profunda, solo copia referencias)
conjuntoCopia = conjunto.copy()
print(conjuntoCopia)

# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjuntoCopia}')
print(f'Es igual en referencia? {conjunto is conjuntoCopia}')

# Opereaciones de conjuntos con set
# Personas con distintas caracteristicas

peloNegro = {'Juan', 'Karla', 'Pedro', 'Maria'}
peloRubio = {'Lorenzo', 'Laura', 'Marco'}
ojosCafe = {'Karla', 'Laura'}
menores30 = {'Juan', 'Karla', 'Maria'}
# Todos con ojosCafe y peloRubio (Union) (No se repiten los elementos)
print(ojosCafe.union(peloRubio))
# Invertir el orden con el mismo resultado (Conmutativa)
print(peloRubio.union(ojosCafe))

# (Intersection) Solo las personas con ojos color cafe y pelo rubio (Conmutativa)
print(ojosCafe.intersection(peloRubio))

# (Difference) Pelo negro sin ojos cafe (Conmutativa)
# las personas que se encuentran en el primer set pero NO en el segundo
print(peloNegro.difference(ojosCafe))

# (diferencia simetrica) Pelo negro u ojos cafe, pero NO ambos (Conmutativa)
print(peloNegro.symmetric_difference(ojosCafe))

# Preguntar si un set esta contenido en otro (subset)
# Revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores30.issubset(peloNegro))

# Preguntar si un set contiene a otro set (superset)
# Revisar si los elementos del primer set estan contenidos en el segundo set
print(menores30.issuperset(peloNegro))

# Preguntar si los de pelo negro no tienen pelo rubio (distjoint)
print(peloNegro.isdisjoint(peloRubio))