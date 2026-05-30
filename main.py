from Grafo_Seguridad import Grafo
from Algoritmos_Infiltracion import Algoritmos

# instanciamos Grafo en red corporativa 
red = Grafo()

#AGREGAMOS LOS COMPONENTES DE LA RED

# Conexiones desde el Router Principal
red.conectar_aristas("Router1", "Internet")
red.conectar_aristas("Router1", "Distro_Switch3")
red.conectar_aristas("Router1", "Distro_Switch4")

# Cable de conexion entre switches de Distribucion
red.conectar_aristas("Distro_Switch3", "Distro_Switch4")

# Servidor DHCP conectado a Distro 3
red.conectar_aristas("Distro_Switch3", "Winserver_DHCP")

# Enlaces cruzados entre capa de Distribucion y capa de Acceso
red.conectar_aristas("Distro_Switch3", "Access_Switch1")
red.conectar_aristas("Distro_Switch3", "Access_Switch2")
red.conectar_aristas("Distro_Switch3", "Access_Switch3")

red.conectar_aristas("Distro_Switch4", "Access_Switch1")
red.conectar_aristas("Distro_Switch4", "Access_Switch2")
red.conectar_aristas("Distro_Switch4", "Access_Switch4")

# Capa de Acceso conectando a las computadoras VPC
red.conectar_aristas("Access_Switch1", "VPC1")
red.conectar_aristas("Access_Switch1", "VPC3")
red.conectar_aristas("Access_Switch2", "VPC4")
red.conectar_aristas("Access_Switch3", "VPC5")
red.conectar_aristas("Access_Switch3", "VPC6")
red.conectar_aristas("Access_Switch4", "VPC7")
red.conectar_aristas("Access_Switch4", "VPC8")

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