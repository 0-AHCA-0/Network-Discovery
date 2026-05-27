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
Aidan LEE ESTO: ya q no tengo tengo claro cual es el objetivo y me muero de sueño, no mas voy a hacer
BFS para q busque normalmente, osea sin ningun objetivo definido o un nodo definido
IGUAL voy a poner el codigo donde si se busca con objetivo mas abajo comentado.
pilas
'''

    def bfs(self, grafo, nodo_inicio):
        cola_busqueda = deque([nodo_inicio])
        nodos_buscados = [nodo_inicio]
        recorrido_BFS = [] ## guardamos el orden en el que implementamos BFS

        while cola_busqueda:
            print(f"Nodos en cola para ser buscados: ", {list(cola_busqueda)})
            nodo_actual = cola_busqueda.popleft() ## Sacamos el primer nodo de la cola
            print("Nodo actual: ", nodo_actual)
            
            ## revisamos los vecinos del nodo actual siendo visitado
            for vecino in grafo.get(nodo_actual, []):
                ## si el vecino no esta en nuestra lista de buscados..
                if vecino not in nodos_buscados:
                    print(f"Nuevo nodo sin visitar {vecino}")
                    nodos_buscados.append(vecino)
                    cola_busqueda.append(vecino)
            
            print("Recorrido BFS completo.")
            return recorrido_BFS


'''
## BFS si es q necesitamos un nodo objetivo

from collections import deque

class GrafoBusqueda:
    def bfs_objetivo(self, grafo, nodo_inicio, nodo_objetivo):
        # 1. Inicializamos la cola con el nodo de inicio
        cola_busqueda = deque([nodo_inicio])
        
        # 2. Lista para rastrear los nodos que ya vimos y no repetir
        nodos_visitados = [nodo_inicio]

        while cola_busqueda:
            # Sacamos el primer nodo de la cola para evaluarlo
            nodo_actual = cola_busqueda.popleft()
            print(f"-> Revisando nodo: {nodo_actual}")
            
            # 3. Condición de victoria: verificamos si es el nodo que buscamos
            if nodo_actual == nodo_objetivo:
                print(f"¡Éxito! Hemos encontrado el objetivo: {nodo_objetivo}")
                return True  # Termina la ejecución de la función inmediatamente
            
            # 4. Si no es el objetivo, encolamos a sus vecinos
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in nodos_visitados:
                    nodos_visitados.append(vecino)
                    cola_busqueda.append(vecino)
                    
        # Si la cola se vacía y el bucle termina, significa que no estaba conectado
        print(f"Búsqueda finalizada. El objetivo '{nodo_objetivo}' no se encontró.")
        return False
'''