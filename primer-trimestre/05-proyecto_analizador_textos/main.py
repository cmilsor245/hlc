"""
  @file: main.py
  @author: Christian Millán Soria
  @created: 09/10/2023
  @license: MIT
  @contact: christiaanmillaan1313@gmail.com
  @info: analizador de texto
"""

# TODO: (WSL command to execute) -> python3 ./05-proyecto_analizador_textos/main.py

""" ------------- """

# función para contar la cantidad de veces que una letra aparece en el texto
def contar_letras(letra, texto):
  return texto.count(letra)

""" -------------------------------------- """

# función para contar la cantidad de palabras en el texto
def contar_palabras(texto):
  palabras = texto.split() # separar el texto en palabras separadas por espacios y almacenarlas en un array
  return len(palabras)

""" -------------------------------------- """

# función para encontrar la letra inicial y final en el texto
# función para encontrar la letra inicial y final en el texto
def encontrar_letras_inicio_fin(texto):
  # Quita espacios en blanco del texto
  texto = texto.strip()
  
  # si el texto no está vacío, encuentra la letra inicial y final
  if texto:
    letra_inicial = texto[0]  # encuentra la letra inicial
    letra_final = texto[-1]  # encuentra la letra final
    return letra_inicial, letra_final

  # si el texto está vacío, devuelve None para ambas letras
  else:
    letra_inicial = None  # no hay letra inicial
    letra_final = None  # no hay letra final
    return letra_inicial, letra_final

""" -------------------------------------- """

# función para invertir el texto
def invertir_texto(texto):
  # invierte el texto usando slicing
  texto_invertido = texto[::-1]
  return texto_invertido

""" -------------------------------------- """

# función para buscar una palabra en el texto usando un diccionario
def buscar_palabra(texto, palabra):
  palabras = texto.split()
  palabra = palabra.lower()  # convertir la palabra a minúsculas para una búsqueda insensible a mayúsculas
  return palabra in [p.lower() for p in palabras]

""" ----------------------------------------------------------------- """

# ingreso de texto
texto = input("Ingresa un texto a elección: ")
texto = texto.lower()  # convertir el texto a minúsculas

""" ------------------------------- """

# ingreso de letras
letra1 = input("Ingresa la primera letra: ").lower()
letra2 = input("Ingresa la segunda letra: ").lower()
letra3 = input("Ingresa la tercera letra: ").lower()

""" ------------------------------- """

# contar la cantidad de letras
cantidad_letra1 = contar_letras(letra1, texto)
cantidad_letra2 = contar_letras(letra2, texto)
cantidad_letra3 = contar_letras(letra3, texto)

print("\nCANTIDAD DE LETRAS")
print(f'Hemos encontrado la letra \'{letra1}\' repetida {cantidad_letra1} veces')
print(f'Hemos encontrado la letra \'{letra2}\' repetida {cantidad_letra2} veces')
print(f'Hemos encontrado la letra \'{letra3}\' repetida {cantidad_letra3} veces')

""" ------------------------------- """

# contar la cantidad de palabras
cantidad_palabras = contar_palabras(texto)
print("\nCANTIDAD DE PALABRAS")
print(f'Hemos encontrado {cantidad_palabras} palabras en tu texto')

""" ------------------------------- """

# encontrar la letra inicial y final
letra_inicial, letra_final = encontrar_letras_inicio_fin(texto)
print("\nLETRAS DE INICIO Y DE FIN")
print(f'La letra inicial es \'{letra_inicial}\' y la letra final es \'{letra_final}\'')

""" ------------------------------- """

# invertir el texto
texto_invertido = invertir_texto(texto)
print("\nTEXTO INVERTIDO")
print(f'Si ordenamos tu texto al revés va a decir: \'{texto_invertido}\'')

""" ------------------------------- """

# buscar la palabra "Python" en el texto
palabra_a_buscar = "Python"
encontrada = buscar_palabra(texto, palabra_a_buscar)
print(f'\nBUSCANDO LA PALABRA {palabra_a_buscar.upper()}')
if encontrada:
  print(f'La palabra \'{palabra_a_buscar}\' se encuentra en el texto')
else:
  print(f'La palabra \'{palabra_a_buscar}\' no se encuentra en el texto')