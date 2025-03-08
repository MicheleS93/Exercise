from AbstractClass.Animal import Animal

class Reptile(Animal):
    def __init__(self, name, age, species, diet, scale_type):
        super().__init__(name, age, species, diet) # Se tiene que pasar solo una vez con todos los param.r
        self.scale_type = scale_type # tipo di squame

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        return (
            f"El animal con nombre: {self.name} tiene {self.age} años, "
            f"es de la especie {self.species} y come solo {self.diet}, "
            f"y tiene escamas de tipo {self.scale_type}"
        )

    # sobrescribimos el metodo abstracto de la clase madre
    def make_sound(self):
        return "SOUND OF REPTILE"

