from AbstractClass.Animal import Animal
from SubClass.Bird import Bird
from SubClass.Mammal import Mammal
from SubClass.Reptile import Reptile

bird = Bird("Águila", 5, "Aquila chrysaetos", "Carnívoro", 2.3)
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
