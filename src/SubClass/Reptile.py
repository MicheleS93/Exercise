from AbstractClass.Animal import Animal

class Reptile(Animal):
    def __init__(self, scale_type):
        self.scale_type = scale_type

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        return f"El animal con nombre: {self.name} tiene {self.age} años, es de la especie {self.species} y come solo {self.diet}, con extra: {self.scale_type}"

    # sobrescribimos el metodo abstracto de la clase madre
    def make_sound(self):
        return "SOUND OF REPTILE"

