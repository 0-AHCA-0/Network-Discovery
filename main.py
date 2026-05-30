from Grafo_Seguridad import Grafo
from Algoritmos_Infiltracion import Algoritmos
'''
No vi que decia grafo en un archivo. asi que se borro todas las cargas manuales.
'''

# instanciamos Grafo en red corporativa 
red = Grafo()

#AGREGAMOS LOS COMPONENTES DE LA RED (MEDIANTE JSON)

print("Cargando infraestructura de red corporativa...")

if red.cargar_archivo("red.json"):
    print("Red cargada con exito desde archivo JSON.\n")
else:
    print("No se pudo iniciar la simulacion sin datos de red.")
    exit()

#Inicializamos los algoritmos de busqueda 
herramienta = Algoritmos()

#COMPUTADORAS DISPONIBLES PARA HACKEAR 
computadoras_disponibles = [nombre for nombre in red.nodos if nombre.startswith("VPC")]
computadoras_disponibles.sort() # Ordenamos causas

#INICIO DEL PROGRAMA 
print("Dispositivos detectados que pueden ser atacados o comprometidos:")
print(f"    {computadoras_disponibles}")

#Pedir al usuario que escriba el nodo inicio
nodo_inicio = input("Escriba el nombre de la VPC para iniciar: ").strip()

#VALIDACION DE VPC
if nodo_inicio not in red.nodos:
    print(f"\n[ERROR] El dispositivo '{nodo_inicio}' no existe en el diagrama de red.")
else:
    
    print(f" SIMULACION INICIADA DESDE: [{nodo_inicio}]")

    ## MENU PARA ESCOGER ENTRE AMBOS ALGORITMOS
    while True:
        print("\nSeleccione un algoritmo..\n")
        print("1. DFS")
        print("2. BFS")
        print("3. Salir")

        opcion = input("Elija una opción del 1 al 3...\t").strip()
        
        match opcion:
            case '1': 
                print("Empezando la ejecución con DFS...\n")
                ruta_infiltracion = herramienta.dfs(red, nodo_inicio)
                print(f"Ruta: {ruta_infiltracion}")
            case '2':
                # Si el usuario quiere infiltrarse a un nodo en especifico
                buscar = input("¿Desea infiltrarse en un nodo en especifico? (si/no): ").strip().lower()
                
                if buscar == "si":
                    nodos_red = list(red.nodos.keys())
                    nodos_red.sort()
                    #nodos en la red
                    print(f"\n Dispositivos en la RED: {nodos_red}")
                    
                    nodo_objetivo = input("Escriba el nombre del nodo: ").strip()
                    #Validamos que exista el nodo objetivo
                    if nodo_objetivo in red.nodos:
                        print("Empezando la ejecución con BFS objetivo...\n")
                        ruta_bfs = herramienta.bfs(red, nodo_inicio, nodo_objetivo)
                        print(f"Ruta al objetivo: {ruta_bfs}")
                    else:
                        print(f"ERROR. EL NODO: {nodo_objetivo} NO EXISTE EN LA RED...")
                else:
                    print("Empezando la ejecución con BFS completo...\n")
                    ruta_bfs = herramienta.bfs(red, nodo_inicio)
                    print(f"Ruta Completa: {ruta_bfs}")
                    
            case '3':
                print("Saliendo del programa...")
                break
            case _:
                print("No se reconocio el comando ingresado, intentelo de nuevo.")