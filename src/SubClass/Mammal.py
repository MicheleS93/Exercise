from AbstractClass.Animal import Animal

class Mammal(Animal):
    def __init__(self, name, age, species, diet, fur_color):
        super().__init__(name) # QST - es necesario super()?
        super().__init__(age)
        super().__init__(species)
        super().__init__(diet)
        self.fur_color = fur_color

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        return f"El animal con nombre: {self.name} tiene {self.age} años, es de la especie {self.species} y come solo {self.diet}, con extra: {self.fur_color}"

    # sobrescribimos el metodo abstracto de la clase madre
    def make_sound(self):
        return "SOUND OF MAMMAL"
