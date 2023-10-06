"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 06/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: programa que calcula las comisiones (13%) de un total introducido por teclado
"""

# TODO: (WSL command to execute) -> python3 ./02-tipos_de_datos/ej2/main.py

""" ------------- """

nombre = input("Por favor, dime tu nombre: ") or "Christian"; # el "or" sirve como placeholder, si no se introduce un nombre, se utiliza el valor por defecto
ventas_totales = input("Por favor, dime tus ventas totales del mes: ");

ventas_totales = float(ventas_totales);
comisiones = round(ventas_totales * 0.13, 2);

print(f"Hola {nombre}, tus comisiones son: {comisiones}");