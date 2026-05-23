class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __repr__(self):
        return self.nombre
    
class Arista:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino