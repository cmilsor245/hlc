"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 06/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: operaciones con índices de strings
"""

# TODO: (WSL command to execute) -> python3 ./03-manipulando-strings/ej1/main.py

""" ------------- """

# encuentra y muestra por pantalla qué caracter ocupa la quinta posición dentro de la palabra "ordenador"
print("ordenador"[4]);

""" -------------------------- """

# encuentra y muestra por pantalla el índice de la primera aparición de la palabra "práctica" en la frase "En teoría, la teoría y la práctica son lo mismo. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son lo mismo. En la práctica, no lo son.";

print(frase.index("práctica"));

# alternativa
print(frase.index("práctica", 0, len(frase)));

""" -------------------------- """

# encuentra y muestra por pantalla el índice de la última aparición de la palabra "práctica" en la frase "En teoría, la teoría y la práctica son lo mismo. En la práctica, no lo son."
print(frase.rindex("práctica"));