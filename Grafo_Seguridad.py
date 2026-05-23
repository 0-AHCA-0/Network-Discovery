# Importamos Nodo y aristas de componentes
from Componentes import Nodo, Arista

#Clase para estructurar el grafo
class Grafo:
    #inicializamos la lista de nodos y sus adyacentes
    def __init__(self):
        self.nodos = {}
        self.lista_adyacencia = {}
    
    #Agregamos los nodos
    def agregar_nodo(self, nombre):
        #Si no ha estado como nodo entonces se añade a la lista de nodos y sus adyacentes
        if nombre not in self.nodos:
            nuevo_nodo = Nodo(nombre)
            self.nodos[nombre] = nuevo_nodo
            self.lista_adyacencia[nuevo_nodo] = []
        return self.nodos[nombre]
    
    #Conectar aristas (n1 a n2 y n2 a n1)
    def conectar_aristas(self, n1, n2):
        nodo1 = self.agregar_nodo(n1)
        nodo2 = self.agregar_nodo(n2)
        
        self.lista_adyacencia[nodo1].append(Arista(nodo1, nodo2))
        self.lista_adyacencia[nodo2].append(Arista(nodo2, nodo1))
        
    