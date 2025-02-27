from modulo1.clase1 import Persona
from modulo2.clase1 import Animal

"""
# Crear una instancia de la clase Persona
persona1 = Persona("Michele", 31)

# Llamar al método saludar y mostrar el resultado
print(persona1.saludar())  # Esto imprimirá: Hola, soy Michele y tengo 31 años.

# Ejecutar: python src/main.py
"""

# Crear un objeto
animal1 = Animal("Tom", 6, "Gato", "Raton")

# Usar print() → Llama a __str__
print(animal1)

# Usar repr() → Llama a __repr__
print(repr(animal1))