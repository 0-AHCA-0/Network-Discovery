#Clase donde estaran todos los algoritmosd de infiltracion (BFS, DFS)

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
    
        