class Orden():
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes +=1
        self._computadoras = list(computadoras)
        self._idOrden = Orden.contadorOrdenes

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self):
        return self._computadoras

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def idOrden(self):
        return self._idOrden

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        
        Id orden: {self._idOrden}
        Computadoras: {computadoras_str}
        
        '''
    
    
    
    def agregarComputadoras(self, computadora):
        self.computadoras.append(computadora)