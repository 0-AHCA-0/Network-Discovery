#Clase donde estaran todos los algoritmos de infiltracion (BFS, DFS)

from collections import deque

class Algoritmos:
    #Obtenemos el inicio del grafo
    def dfs(self, grafo, inicio):
        inicio = grafo.nodos.get(inicio)
        #Si no existe un nodo valido paramos
        if not inicio: return []
        
        #Creacion de conjunto set para almacenar los visitados
        visitados = set()
        
        #Guardamos el orden de los comprometidos en la red
        orden_descubrimiento = []

        #inicio de la funcion recursiva
        def inicio_dfs(nodo):
            #Entra al nodo actual
            visitados.add(nodo)
            #Agregamos el nodo en decubiertos (hackeados)
            orden_descubrimiento.append(nodo.nombre)
            
            #iteramos en los nodos conectados
            for arista in grafo.lista_adyacencia[nodo]:
                #Revisa elementos conectados del vecino
                vecino = arista.destino
                
                #Verifica si ya se visito
                #Si no esta visitado, busca en profundidad
                if vecino not in visitados:
                    inicio_dfs(vecino)
        
        #Pasa el nodo actual para continuar con el algoritmo
        inicio_dfs(inicio)
        #retorna la ruta 
        return orden_descubrimiento
    
    '''
    OE PELADA DEJA A TU NOVIO OE :(
    '''

    def bfs(self, grafo, nodo_inicio, nodo_objetivo=None):
        # Buscamos primero el objeto Nodo real que coincide con el nombre de inicio
        inicio = grafo.nodos.get(nodo_inicio)
        if not inicio: return []
        
        cola_busqueda = deque([inicio])
        nodos_buscados = [inicio]
        recorrido_BFS = [] # guardamos el orden en el que implementamos BFS

        while cola_busqueda:
            # Convertimos los nombres en una lista limpia para imprimir sin errores
            nodos_nombres = [n.nombre for n in cola_busqueda]
            
            
            nodo_actual = cola_busqueda.popleft() # Sacamos el primer nodo de la cola
            recorrido_BFS.append(nodo_actual.nombre)
            
            
            #Si el usuario paso un nodo objetivo
            if nodo_objetivo and nodo_actual.nombre == nodo_objetivo:
                print(f"¡Se ha encontrado el nodo objetivo: {nodo_objetivo}!")
                return recorrido_BFS
            
            # revisamos los vecinos usando las aristas de la lista de adyacencia
            for arista in grafo.lista_adyacencia[nodo_actual]:
                vecino = arista.destino
                # si el vecino no esta en nuestra lista de buscados..
                if vecino not in nodos_buscados:
                    
                    nodos_buscados.append(vecino)
                    cola_busqueda.append(vecino)
            
        # Validacion si no se encontro un nodo objetivo tras vaciar la cola
        if nodo_objetivo:
            print(f"SE DETUVO LA BUSQUEDA. NODO {nodo_objetivo} NO ENCONTRADO UNU")
            
        print("Recorrido BFS completo.")
        return recorrido_BFS