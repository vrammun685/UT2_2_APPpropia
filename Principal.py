#Aqui usaremos los datos del modelo que han cargado 
from ModeloMenu import menu, menuInfo, menu_Añadir_Eliminar
from ModeloDatos import *

def main():
    opcion=menu()
    while opcion >= 1 and opcion<=6:
        if opcion==1:
            #Cargar personages
            print("Opcion 1 elegida")
            print(CargarPersonajes())
            
        elif opcion==2:
            #Crear Personaje o eliminarlo
            print("Opcion 2 elegida")
            opcion=menu_Añadir_Eliminar()
            if opcion==1:
                añadapersonaje()
            else:
                eliminarpersonaje()
            
        elif opcion==3:
            #Buscar un personaje 
            print("Opcion 3 elegida")
            nombre=str(input("Dame el nombre de el personaje que quieras buscar: "))
            print(BuscarPersonaje(nombre))
            
        elif opcion==4:
            #Ver lista de personajes
            print("Opcion 4 elegida")
            opcioninfo=menuInfo()
            print(verDatos(opcioninfo))
        elif opcion==5:
            #Ver lista de personajes
            print("Opcion 5 elegida")
            print(verVivos())
        else:
            #Salir
            print("Opcion 6 elegida")
            print("Saliendo del programa. . .")
            exit()
        opcion=menu()





main()