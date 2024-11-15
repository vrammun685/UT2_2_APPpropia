# Menu Principal
def muestramenu():
    print("----Menu Proyecto RickyMorty----")
    print("1. Cargar un personaje")
    print("2. Crear o eliminar un personaje")
    print("3. Buscar un Personaje")
    print("4. Ver lista de personajes")
    print("4. Ver lista de personajes vivos")
    print("6. Salir del Programa")

def pedir_opcion_menu_principal():
    while True:
        try:
            opcion = int(input("Elige una opción del menú: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción errónea. Elija un número del 1 al 6.")
                muestramenu()
        except ValueError:
            print("Por favor, introduce un número válido del menú (1-6).")

def menu():
    muestramenu()
    return pedir_opcion_menu_principal()
# Menu Principal


# Menu de Añadir y Eliminar
def Muestra_Menu_Añadir_Eliminar():
    print("----Menu de añadir o eliminar Personajes----")
    print("1. Añadir un personaje")
    print("2. Eliminar un personaje")

def pedir_opcion_menu_añadir_eliminar():
    while True:
        try:
            opcion = int(input("Elige una opción (1 para añadir, 2 para eliminar): "))
            if opcion == 1 or opcion == 2:
                return opcion
            else:
                print("Opción errónea. Por favor, elija 1 o 2.")
                Muestra_Menu_Añadir_Eliminar()
        except ValueError:
            print("Por favor, introduce un número válido (1 o 2).")

def menu_Añadir_Eliminar():
    Muestra_Menu_Añadir_Eliminar()
    return pedir_opcion_menu_añadir_eliminar()
# Menu de Añadir y Eliminar

# Menu de Ver Personajes
def menuVerPersonajes():
    print("----Menu de información de Personajes----")
    print("1. Ver información importante de los personajes")
    print("2. Ver toda la información de los personajes")

def pedir_opcion_menu_info():
    while True:
        try:
            opcion = int(input("Elige una opción (1 o 2): "))
            if 1 <= opcion <= 2:
                return opcion
            else:
                print("Opción errónea. Por favor, elija 1 o 2.")
                menuVerPersonajes()
        except ValueError:
            print("Por favor, introduce un número válido (1 o 2).")

def menuInfo():
    menuVerPersonajes()
    return pedir_opcion_menu_info()

