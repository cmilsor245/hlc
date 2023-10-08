"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 08/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: basics about arrays
"""

# TODO: (WSL command to execute) -> python3 ./04-arrays_y_mas/arrays/main.py

""" ------------- """

lista1 = [4, "hola", True];
lista2 = [1, 2, 3];

""" -------------------------------------- """

# longitud de un arrays
print(lista1);

""" ---------------------------- """

# tipo de un array
print(type(lista1));

""" ---------------------------- """

# elementos de un array
print(lista1[0]);
print(lista1[0:]);
print(lista1[2:]);
print(lista1[1:2]);

""" ---------------------------- """

# concatenación de arrays
print(lista1 + lista2);

""" ---------------------------- """

# reemplazo de un elemento
lista2[2] = 4;

print(lista2);

""" ---------------------------- """

# añadir elementos al final
lista2.append(5);

print(lista2);

""" ---------------------------- """

# elimina el último elemento
lista2.pop();

print(lista2);

""" ---------------------------- """

# elimina el elemento indicado
lista2.pop(1);

print(lista2);

""" ---------------------------- """

# ordena los elementos
lista2.sort();

print(lista2);

""" ---------------------------- """

# ordena los elementos al revés
lista2.reverse();

print(lista2);