"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 09/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: basics about tuples
"""

# TODO: (WSL command to execute) -> python3 ./04-arrays_y_mas/tuplas/main.py

""" ------------- """

# las tuplas son como los arrays, pero inmutables
tupla = (1, 2, 3, 4);

""" ---------------------------- """

# muestra el tipo de la variable "tupla"
print(type(tupla));

""" ---------------------------- """

# muestra el segundo elemento de la tupla
print(tupla[1]);

""" ---------------------------- """

# esta línea genera un error, ya que la tupla es inmutable
tupla [1] = 5;