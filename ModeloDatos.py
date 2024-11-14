import requests
from character import Character

#Creamos la lista donde vamos a almacenar todos los personajes que tiene la api
Listacharacters=[]


#Creamos la primera Función de nuestro menu
def CargarPersonajes():
    global Listacharacters
    try:
        response = requests.get('https://rickandmortyapi.com/api/character')
        #Esto mira el estado de la consulta 
        response.raise_for_status()  
        data = response.json()
        
        # Crear una lista de personajes
        for char in data['results']:
            personaje = Character(
            id=char['id'],
            name=char['name'],
            status=char['status'],
            species=char['species'],
            type=char['type'],
            gender=char['gender'],
            origin=char['origin']['name'],  # Extraemos solo el nombre del origen
            location=char['location']['name'],  # Extraemos solo el nombre de la ubicación
            image=char['image'],
            episode=char['episode']
            )
            Listacharacters.append(personaje)
        #Devuelve un mensaje positivo si se ha podido cargar bien los personajes
        return ("!!!!!Personajes cargados con exito!!!!!!") 
    
    except requests.exceptions.RequestException as e:
        #Si por el contrario no ha funcionado devolveremos un mensaje de error
        print("Error al cargar personajes:", e)

def eliminarpersonaje():
    NombrePersonaje=str(input("Nombre del personaje a eliminar"))
    for charac in Listacharacters:
        if charac.name==NombrePersonaje:
            Listacharacters.remove(charac)
            return("Personaje eliminado")
            
    return ("Personaje no encontrado \nRevisa la lista de personajes")

def añadapersonaje():
    nuevo_id = int(input("Dame el ID: "))
    nuevo_name = str(input("Dame el nombre: "))
    for charac in Listacharacters:
        if charac.name==nuevo_name:
            return("Ya existe ese personaje")
    
    nuevo_status = str(input("Dame el estado: "))
    nuevo_species = str(input("Dame la especie: "))
    nuevo_type = str(input("Dame el tipo: "))
    nuevo_gender = str(input("Dame el género: "))
    nuevo_origin = str(input("Dame el origen: "))
    nuevo_location = str(input("Dame la ubicación: "))
    nuevo_image = str(input("Dame la URL de la imagen: "))
    nuevo_episode = str(input("Dame el episodio (o una lista de episodios): "))

    personaje = Character(
            id=nuevo_id,
            name=nuevo_name,
            status=nuevo_status,
            species=nuevo_species,
            type=nuevo_type,
            gender=nuevo_gender,
            origin=nuevo_origin,  # Extraemos solo el nombre del origen
            location=nuevo_location,  # Extraemos solo el nombre de la ubicación
            image=nuevo_image,
            episode=nuevo_episode
            )
    Listacharacters.append(personaje)
    

def BuscarPersonaje(NombrePersonaje):
    for charac in Listacharacters:
        if charac.name==NombrePersonaje:
            return charac.get_info()
            
    return ("Personaje no encontrado \nRevisa la lista de personaje")
    
def VerPersonajesSimple():
    salida = ""
    for charac in Listacharacters:
        salida += charac.get_infoesne() + "\n"
    return salida

def VerPersonajesCompleto():
    salida = ""
    for charac in Listacharacters:
        salida += charac.get_info() + "\n"
    return salida

def verDatos(opcioninfo):
    if opcioninfo==1:
        #Información esencial de los datos
        return VerPersonajesSimple()
    else:
        return VerPersonajesCompleto()
    
