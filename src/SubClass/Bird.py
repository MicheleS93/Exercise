# TODO comprobar si el import es correcto

from AbstractClass.Animal import Animal


class Bird(Animal):
    def __init__(self, name: str, age: int, species: str, diet: str, wing_span: float):
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
    # QST - Estoy obligado??  si, por que en la clase Animal lo hemos marcado como metodo abstracto, toda subclase debe
    # implementar los metodos abstractos del padre. Pycharm deberia quejarse sino lo haces.
    def make_sound(self):
        # TODO ver notas en la clase mammal
        return "SOUND OF BIRD"