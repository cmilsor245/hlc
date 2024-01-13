"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 06/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: ejercicios sobre strings
"""

# TODO: (WSL command to execute) -> python3 ./03-manipulando-strings/ej3/main.py

""" ------------- """

# imprime el siguiente texto en mayúsculas utilizando la función adecuada
frase = "Especialmente en las comunidades electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

print(frase.upper());

""" ----------------------------- """

# muestra la siguiente lista de strings en uno sólo separados por espacios
lista_palabras = ["La", "legibilidad", "cuenta."];

print(" ".join(lista_palabras));

""" ----------------------------- """

"""
  reemplaza en la siguiente frase: "Si la implementación es difícil de explicar, puede que sea una mala idea." ->
  - "difícil" -> "fácil"
  - "mala" -> "buena"
"""
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea.";

print(frase.replace("difícil", "fácil").replace("mala", "buena"));

""" ----------------------------------------------------------------------------------- """

# propiedades de los strings
# inmutabilidad
nombre = "Juan";

# nombre[0] = "K"; - esta línea genera un error

""" ----------------------------- """

# concatenación
print(nombre*10); # se muestra el string 10 veces

""" ----------------------------- """

# alternativa para el salto de línea
poema = """El Sol de la caliente llanura vinariega
quemó su piel, mas guarda frescura de bodega
su corazón. Devota""";

print(poema);

""" ----------------------------- """

# "in" y "not in"
print("Sol" in poema); # devuelve "true" si se encuentra en la variable

print("cielo" not in poema); # devuelve "true" si no se encuentra en la variable

""" ----------------------------- """

# longitud de un string
print(len(poema));