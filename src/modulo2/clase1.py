class Animal:

    # Atributos de clase
    status = "vivo"
    reino = "Animalia"
    vertebrado = True

    def __init__(self, name, age, species, diet):
        # Atributos de instancia (características que puede tener un objeto)
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet

    # Definir cómo se representa un objeto en forma de texto (Representación oficial)
    def __repr__(self):
        return f"Animal('{self.name}', {self.age}, {self.species}, {self.diet})" 

    # Definir cómo se representa un objeto en forma de texto (Representación amigable)
    def __str__(self):
        return f"El animal con nombre: {self.name} tiene {self.age} años, es de la especie {self.species} y come solo {self.diet}" 

    # ---------------------------------------------------------------------------------------------------------------------------------
    
    def comer(self):
        pass