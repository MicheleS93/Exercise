from AbstractClass.Animal import Animal
from SubClass.Bird import Bird
from SubClass.Mammal import Mammal
from SubClass.Reptile import Reptile
from Zoo.Zoo import Zoo

# ------------------------------------------------------------------------------
# 1. Classes and Inheritance:

"""bird = Bird("Águila", 5, "Aquila chrysaetos", "Carnívoro", 2.3)
print(bird) 
print(bird.make_sound())

print()

mammal = Mammal("León", 7, "Panthera leo", "Carnívoro", "Dorado")
print(mammal)  
print(mammal.make_sound()) 

print()

reptile = Reptile("Cobra", 4, "Naja naja", "Carnívoro", "Lisas")
print(reptile)  
print(reptile.make_sound())

print()"""

# ------------------------------------------------------------------------------
# 2. Data Management:

zoo = Zoo("Michele adventure")
print(zoo)

print()

# ------------------------------------------------------------------------------
# 3. Funcionality: Add, Remove, etc:

#zoo.add_animal()

#zoo.remove_animal()

#zoo.list_animals()

#zoo.make_all_animals_sound()

#zoo.find_animals_by_species()

#zoo.list_animals_by_type()

# TODO recuerda que las funciones deberían seguir esta estructura
'''
# Example Usage
zoo = ZooManagementSystem()
zoo.add_animal("Lion", 5, "Panthera leo", "Carnivore", "Mammal", fur_color="Golden")
zoo.add_animal("Eagle", 3, "Aquila chrysaetos", "Carnivore", "Bird", wing_span=2.1)
zoo.add_animal("Python", 2, "Python regius", "Carnivore", "Reptile", scale_type="Smooth")

print("\nList of all animals:")
zoo.list_animals()

print("\nAnimals making sounds:")
zoo.make_all_animals_sound()

print("\nFinding animals by species 'Panthera leo':")
zoo.find_animals_by_species("Panthera leo")

print("\nListing all mammals:")
zoo.list_animals_by_type("Mammal")

print("\nRemoving 'Eagle':")
zoo.remove_animal("Eagle")

print("\nList of all animals after removal:")
zoo.list_animals()
'''