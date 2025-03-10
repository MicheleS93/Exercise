# Abstract classes 
    # cannot be instantiated on its own and is designed to be a blueprint for other classes.
    # allow us to define methods that must be implemented by subclasses.
    # ensuring a consistent interface while still allowing the subclasses to provide specific implementations.

from abc import ABC, abstractmethod


class Animal(ABC): # QST - es necesario ABC? -> si, de esta forma convertimos la clase
                   # en clas abstracta, sino sería una clase normal

    # Atributos de clase
    status = "vivo"
    reino = "Animalia"
    vertebrado = True

    def __init__(self, name: str, age: int, species: str, diet: str):
        # Atributos de instancia (características que puede tener un objeto)
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        # TODO intenta no mezclar idiomas ;)
        return f"El animal con nombre: {self.name} tiene {self.age} años, es de la especie {self.species} y come solo {self.diet}"

    # Metodo abstracto
    @abstractmethod # Decorador para crear un metodo abstracto
    def make_sound(self):
        pass
    # Obligarà las clases hijas a utilizarlo!
    # TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'
