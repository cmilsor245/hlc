"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 06/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: concatenación de strings con variables de tres formas diferentes: sin usar "format", usando "format" y usando "f"
"""

# TODO: (WSL command to execute) -> python3 ./02-tipos_de_datos/ej1/main.py

""" ------------- """

nombre_asociado = "Jesse Pinkman";
numero_asociado = 399058;

""" ---------------------------------------- """

# method 1
print("Estimado/a " + nombre_asociado + ", su número de asociado es: " + str(numero_asociado)); # hace falta convertir a string la variable "numero_asociado"

# method 2
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado, numero_asociado));

# method 3
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}");