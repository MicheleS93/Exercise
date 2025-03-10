from AbstractClass.Animal import Animal

# TODO desconozco como te has configurado el entorno, el import no debería ser así ?
#from src.AbstractClass.Animal import Animal


class Mammal(Animal): # Mammifero
    def __init__(self, name: str, age: int, species: str, diet: str, fur_color: str):
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
        # TODO aquí deberias usar el self, de lo contrario el metodo lo marcaríamos como static.
        # En este caso, dado que cada animal tiene "en teoría" un "make_sound" propio algo así sería suficiente:
        # print(f"{self.name} the {self.species} roars or growls!")
        return "SOUND OF MAMMAL"
