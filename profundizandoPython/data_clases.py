from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    contador_personas: ClassVar[int] = 0
    domicilio: Domicilio

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor de nombre vacio: {self.nombre}')


domicilio1 = Domicilio('Saturno', 15)
persona1 = Persona('Joan', 'Herrera', Domicilio('Marte', 17))
print(f'{persona1!r}')
# Variable de clase
print(f'Variable de clase: {Persona.contador_personas}')
# Variable de instancia
print(f'Variables de instancia: {persona1.__dict__}')
# Variables con valores vacios
persona_vacia = Persona('Alexis', 'Vilte', Domicilio('', 0))
print(f'Persona vacia: {persona_vacia}')
# Revisar igualdad entre objetos
persona2 = Persona('Joan', 'Herrera', Domicilio('Jupiter', 30))
print(f'Objetos iguales?: {persona1 == persona2}')
# Agregar esta clase a una colecciones
coleccion = {persona1, persona2}
print(coleccion)
#Frozen = True
#coleccion[0].nombre='Juan Carlos'
#persona1.nombre = 'Juan carlos'