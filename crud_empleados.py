import os
import json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)
    
def menu_general():
    os.system("cls")
    print("1. Crear empleados")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Listar empleado")
    print("5. Salir")

def selecionar_opcion(max_opcion):
    opcion = 0 
    try:
        opcion = int(input("Seleccione una opcion "))   
    except:
        pass
    if opcion < 1 or opcion > max_opcion:
        input("Opcion invalida seleccione nuevamente ")
    else:
        return opcion
    

def iniciar_programa():
    while True:
        opcion = selecionar_opcion(5)

        if opcion == 1:
            print("1. Crear empleados")
        elif opcion == 2:
            print("2. Actualizar empleado")
        elif opcion == 3:
            print("3. Eliminar empleado")
        elif opcion == 4:
            print("4. Listar empleado")
        elif opcion == 5:
            print("5. Salir")            
        


        empleados = cargar_json('empleados.json')
        print(empleados)
    
iniciar_programa()

