import json 
import os
from datetime import datetime

# TODO ver imports
from SubClass.Bird import Bird
from SubClass.Mammal import Mammal
from SubClass.Reptile import Reptile


class Zoo:

    # Attributos
    def __init__(self, name):
        self.name = name.replace(" ", "_").lower()  # Nome del file senza spazi
        self.file_path = f"data/{self.name}.json"  # Percorso unico per ogni zoo

        # TODO qué ocurre si el fichero está vacío ?
        self.animals = self.load_from_json()  # Carica gli animali

    def __str__(self):
        return (
                    f"Bienvenido al Zoo: {self.name}!! \n"
                    f"Actualmente contamos con {len(self.animals)} animal/es."
                )
    
    # Metodos

    def load_from_json(self):
        """Cargar animales desde JSON por el nombre del Zoo"""
        if not os.path.exists("data"):
            os.makedirs("data")

        # TODO entiendo que vacias la lista ?
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)  # Lista vuota per nuovi zoo

        # TODO esto debería ir antes de la escritura, de lo contrario el json estará vacío
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save_to_json(self, animals=None):
        """Salva gli animali nel file JSON. Se non vengono passati, usa quelli attuali."""
        if animals is None:
            animals = self.animals  # Se non passiamo una lista, usa self.animals

        # TODO antes de pasar a escribir al json, la clase animal debe serializarse
        with open(self.file_path, "w") as f:
            json.dump(animals, f, indent=4)

    def add_animal(self):
        # TODO add animal debería recibir como parametros  name: str, age: int, species: str, diet: str, animal_type: str, **kwargs
        # Solo puede pertenecer a uno de los tipos: reptil, bird o mammal (lista de opciones)
        # En funcion del tipo pedimos los datos especificos!
        # Verificamos si el nombre asignado es unico. Si no lo es pedimos que lo cambien

        # TODO crear un menu que permita leer animales me parece muy acertado, sin embargo mejor añadir esa lógica en
        # TODO una función aparte y que esa función te devuelva el animal inicializado, ie: read_animal() -> animal

        print("En esta funcionalidad puedes anadir animales al zoo. Te voy a pedir algunos datos..")
        
        # ----------------------------
        # Datos Generales

        # Gestion Type
        tipo = -1
        while tipo not in ["1", "2", "3"]: # controlar si el tipo no es correcto...
            print("Es posible anadir un animal que pertenece a uno de estos tipos:\n1-Bird \n2-Mammal \n3-Reptile")
            tipo = input("Indicar la opcion (1-3): ")        
        
        # Gestion Name
        lista_nombres_animales = []
        for items in self.animals:
            lista_nombres_animales.append(items["name"])

        while True:
            name = input("Animal Name: ")
            if name in lista_nombres_animales:
                print("Lo sentimos, este nombre ya está en uso. Introducir otro.")
            else:
                break     
        
        # Gestion Age, species, diet (Sin controles..)
        age = int(input("Age: "))
        species = input("Species: ")
        diet = input("Diet: ")
        
        # ----------------------------
        # Datos Extras

        # Condicional para pedir datos extra en funcion de tipo
        # Lo ideal no seria hacerlo con condicionales por cada tipo, deberia ser dinamico por si cambia o se anaden otros...

        tipo_clase = {"1": "Bird", "2": "Mammal", "3": "Reptile"}[tipo]

        # TODO aqui puedes usar la sentencia match
        if tipo_clase == "Bird":
            extra_attr = input("Introduce la envergadura del ala en metros: ")
            attr_name = "wing_span"
        elif tipo_clase == "Mammal":
            extra_attr = input("Introduce el color del pelaje: ")
            attr_name = "fur_color"
        elif tipo_clase == "Reptile":
            extra_attr = input("Introduce el tipo de escamas: ")
            attr_name = "scale_type"

        # Guardamos la fecha de alta del animal
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ----------------------------
        # Guardamos datos en json madre

        # Creamos diccionario de animal nuevo
        new_animal = {
            "date": fecha,
            "type": tipo_clase,
            "name": name,
            "age": age,
            "species": species,
            "diet": diet,
            attr_name: extra_attr 
        }

        # Anadimos item a json de zoo
        # TODO animals debería seguir esta estructura self.animals: Dict[str, Animal] = {}
        # TODO fíjate que no has usado ninguna clase bird, mammal reptile
        # TODO puedes hacer algo así
        '''
        animal_classes = {"Mammal": Mammal, "Bird": Bird, "Reptile": Reptile}
        if animal_type not in animal_classes:
            print(f"Error: Unknown animal type '{animal_type}'.")
            return
        
        self.animals[name] = animal_classes[animal_type](name, age, species, diet, **kwargs)
        '''
        self.animals.append(new_animal)

        # TODO esto lo puedes meter como decorador, quedará más elegante
        self.save_to_json()

        # Avisamos usuario que todo ok
        print(f"En Animal {name}, del tipo {tipo_clase} se ha anadido correctamente al zoo {self.name}!! \nFecha Alta: {fecha}")
       
    def remove_animal(self):
        # TODO remove_animal debe recibir como párametro el nombre del animal a borrar
        # dado un nombre del animal, lo busco en el json y elimino el item
        print("En esta funcionalidad puedes eliminar animales del zoo por su Nombre!")
        name_to_remove = input("🔍 Introducir nombre animal a eliminar: ")

        # TODO este for se debe convertir en un if, recuerda que estas usando un diccionario :)
        for animal in self.animals:
            # TODO cuidado con el acceso al atributo -> animal.name
            if animal["name"] == name_to_remove:
                fecha_remove = datetime.now()
                fecha_alta = datetime.strptime(animal["date"], "%Y-%m-%d %H:%M:%S")
                delta = fecha_remove - fecha_alta

                print("Este animal he entrado en nuestro zoo en la fecha",animal["date"])
                print("Ha estado aqui por:",delta,"horas")
                # Eliminar el animal de la lista
                self.animals.remove(animal)

                # TODO decorador
                self.save_to_json() 
                print(f"{name_to_remove} ha sido eliminado del zoo.")

                return
        # TODO añade el nombre en el mensaje
        print("Lo siento el nombre del animal no existe en nuestro zoo!!")

    def list_animals(self):
        # imprimo todos los animales presentes en el json con los detalles

        # TODO es probable que quieras dar formato a la salida para que no te imprima el par key-value
        for animal in self.animals:
            print(animal)

    def make_all_animals_sound(self):
        # por cada animal presente en el json llamo la funcion make sound

        print("En esta funcionalidad muestra los sonidos de cada animal por su tipo")
        for animal in self.animals:
            # TODO cuidado con los accesos, animal es un objeto con atributo name -> animal.name
            name = animal["name"]
            age = animal["age"]
            species= animal["species"]
            diet = animal["diet"]
            # TODO en realidad no te hace falta saber el tipo de animal
            # TODO tu for debería tener dos líneas de código ;)
            if animal["type"]== "Mammal":
                # Creo instancia animal
                mammal = Mammal(name, age, species, diet, animal["fur_color"])
                # Activo metodo para make sound
                print(mammal) 
                print(mammal.make_sound())

            elif animal["type"]== "Reptile":
                # Creo instancia animal
                reptile = Reptile(name, age, species, diet, animal["scale_type"])
                # Activo metodo para make sound
                print(reptile) 
                print(reptile.make_sound())


            elif animal["type"]== "Bird":
                bird = Bird(name, age, species, diet, animal["wing_span"])
                print(bird) 
                print(bird.make_sound())

    def find_animals_by_species(self):
        # TODO esta función debería recibir como parámetro la especie
        # por cada animal presente en el json filtro segun el parametro species

        print("En esta funcionalidad muestra los animales por specie!")
        specie_filter = input("🔍 Introducir specie a analizar: ")

        for animal in self.animals:
            # TODO cuidado con el acceso a los atributos -> animal.species
            if animal["species"]== specie_filter:
                print(animal)
            # TODO qué ocurre si no lo encuentra ?

    def list_animals_by_type(self):
        # TODO esta función debería recibir como parámetro el tipo
        # por cada tipo de animal presente en el json imprimo el contenido 

        grouped_animals = {"Bird": [], "Mammal": [], "Reptile": []}

        # Agrupar los animales por tipo
        for animal in self.animals:
            # TODO cuidado con el acceso
            grouped_animals[animal["type"]].append(animal)

        # Mostrar cada tipo de animal solo si hay datos
        for key, value in grouped_animals.items():
            if value:  # Si la lista no está vacía, mostramos los animales
                print(f"\n{key}s ({len(value)} total)")
                for animal in value:
                    print(f"   - {animal['name']} ({animal['species']}, {animal['age']} años, Dieta: {animal['diet']})")