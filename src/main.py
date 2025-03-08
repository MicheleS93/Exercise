from AbstractClass.Animal import Animal
from SubClass.Bird import Bird

"""# Crear un objeto
animal1 = Animal("Tom", 6, "Gato", "Raton")

# Usar print() → Llama a __str__
print(animal1)"""

bird_1 = Bird("Águila", 5, "Aquila chrysaetos", "Carnívoro", 2.3)
print(bird_1)  # Output: El animal con nombre: Águila tiene 5 años, es de la especie Aquila chrysaetos y come solo Carnívoro. Tiene una envergadura de 2.3 metros.
print(bird_1.make_sound())  # Output: SOUND OF BIRD