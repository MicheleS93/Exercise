from AbstractClass.Animal import Animal

class Mammal(Animal): # Mammifero
    def __init__(self, name, age, species, diet, fur_color):
        super().__init__(name, age, species, diet) # Se tiene que pasar solo una vez con todos los param.
        self.fur_color = fur_color # color pelo

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        return (
            f"El animal con nombre: {self.name} tiene {self.age} años, "
            f"es de la especie {self.species} y come solo {self.diet}, "
            f"y tiene el pelaje de color {self.fur_color}"
        )

    # sobrescribimos el metodo abstracto de la clase madre
    def make_sound(self):
        return "SOUND OF MAMMAL"
