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

        print("\n RECORRIDO DFS")

        #inicio de la funcion recursiva
        def inicio_dfs(nodo):
            #Entra al nodo actual
            visitados.add(nodo)
            #Agregamos el nodo en decubiertos (hackeados)
            orden_descubrimiento.append(nodo.nombre)
            
            # Muestra en consola el nodo hackeado actualmente
            print(f"\n[ENTRANDO] Nodo actual: {nodo.nombre}")
            print(f"-> Nodos hackeados hasta ahora: {orden_descubrimiento}")
            
            #iteramos en los nodos conectados
            for arista in grafo.lista_adyacencia[nodo]:
                #Revisa elementos conectados del vecino
                vecino = arista.destino
                
                print(f"   Revisando cable desde {nodo.nombre} hacia: {vecino.nombre}")
                
                #Verifica si ya se visito
                #Si no esta visitado, busca en profundidad
                if vecino not in visitados:
                    print(f"   ¡El vecino {vecino.nombre} no esta visitado!")
                    inicio_dfs(vecino)
                else:
                    print(f"   VECINO IGNORADO. El vecino {vecino.nombre} ya fue hackeado antes.")
            
            # Al terminar los vecinos de esta rama, regresa al anterior
            print(f" No hay mas cables nuevos en: {nodo.nombre}. Volviendo...")
        
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
            
            # Imprimimos los nodos que estan esperando en la cola usando el list
            print("Nodos en cola para ser buscados: ", list(nodos_nombres))
            
            nodo_actual = cola_busqueda.popleft() # Sacamos el primer nodo de la cola
            recorrido_BFS.append(nodo_actual.nombre)
            
            # Imprimimos el nodo que se esta revisando en este turno
            print("Nodo actual: ", nodo_actual.nombre)
            
            #Si el usuario paso un nodo objetivo
            if nodo_objetivo and nodo_actual.nombre == nodo_objetivo:
                print(f"¡Se ha encontrado el nodo objetivo: {nodo_objetivo}!")
                return recorrido_BFS
            
            # revisamos los vecinos usando las aristas de la lista de adyacencia
            for arista in grafo.lista_adyacencia[nodo_actual]:
                vecino = arista.destino
                # si el vecino no esta en nuestra lista de buscados..
                if vecino not in nodos_buscados:
                    # Imprimimos el nuevo vecino que acabamos de descubrir
                    print(f"Nuevo nodo sin visitar {vecino.nombre}")
                    nodos_buscados.append(vecino)
                    cola_busqueda.append(vecino)
            
        # Validacion si no se encontro un nodo objetivo tras vaciar la cola
        if nodo_objetivo:
            print(f"SE DETUVO LA BUSQUEDA. NODO {nodo_objetivo} NO ENCONTRADO UNU")
            
        print("Recorrido BFS completo.")
        return recorrido_BFS