from AbstractClass.Animal import Animal

class Bird(Animal):
    def __init__(self, name, age, species, diet, wing_span):
        super().__init__(name, age, species, diet) # Se tiene que pasar solo una vez con todos los param.
        self.wing_span = wing_span

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        return f"El animal con nombre: {self.name} tiene {self.age} años, es de la especie {self.species} y come solo {self.diet}, Tiene una envergadura de {self.wing_span} metros."

    # Sobrescribimos el metodo abstracto de la clase madre
    def make_sound(self):
        return "SOUND OF BIRD"
