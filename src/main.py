from AbstractClass.Animal import Animal
from SubClass.Bird import Bird
from SubClass.Mammal import Mammal
from SubClass.Reptile import Reptile
import time  
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