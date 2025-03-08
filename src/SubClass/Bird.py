from AbstractClass.Animal import Animal

class Bird(Animal):
    def __init__(self, name, age, species, diet, wing_span):
        super().__init__(name, age, species, diet) # Se tiene que pasar solo una vez con todos los param.
        self.wing_span = wing_span # aberturas alas, attributo unico en birds

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        return (
            f"El animal con nombre: {self.name} tiene {self.age} años, "
            f"es de la especie {self.species} y come solo {self.diet}, "
            f"tiene una envergadura de {self.wing_span} metros."
        )
     
    # Sobrescribimos el metodo abstracto de la clase madre
    # QST - Estoy obligado??
    def make_sound(self):
        return "SOUND OF BIRD"