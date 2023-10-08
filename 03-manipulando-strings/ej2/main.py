"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 06/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: "slicing" strings
"""

# TODO: (WSL command to execute) -> python3 ./03-manipulando-strings/ej2/main.py

""" ------------- """

saludo = "Hola_Mundo";

# slice 1
print(saludo[2:6]); # empieza por la posición 2 (incluida) y termina por la posición 6 (excluida)

# slice 2
print(saludo[3::3]); # empieza por la posición 3 (incluida) y termina por el final (no especificado), de 3 en 3

# slice 3
print(saludo[::-1]); # empieza por el final y termina por el principio

""" --------------------------- """

# extrae la primera palabra de la siguiente frase utilizando "slicing" y la muestra por pantalla: "Controlar la complejidad es la esencia de la programación"
frase = "Controlar la complejidad es la esencia de la programación";

print(frase[0:8]);

""" --------------------------- """

# toma cada tercer caracter empezando desde el noveno hasta el final de la frase e imprime el resultado: "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana";

print(frase[8::]);

""" -------------------------- """

# invierte la posición de todos los caracteres de ls siguientes frase y muestra el resultado por pantalla: "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza";

print(frase[::-1]);