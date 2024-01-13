"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 08/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: basics about dictionaries
"""

# TODO: (WSL command to execute) -> python3 ./04-arrays_y_mas/diccionarios/main.py

""" ------------- """

empty_dic = {};

rae = {
  "bifronte": "De dos frentes o dos caras",
  "anarcoide": "Que tiende al desorden",
  "montuvio": "Campesino de la costa"
};
""" --------------------------- """

# se muestran todas las keys con sus respectivos valores
print(rae);

""" --------------------------- """

# se muestra el valor de la key "bifronte"
print(rae["bifronte"]);

""" --------------------------- """

# se muestran únicamente las keys
print(rae.keys());

""" --------------------------- """

# se muestran únicamente los valores
print(rae.values());

""" --------------------------- """

# se muestra cada key con su valor separado de los demás items
print(rae.items());