from ctypes import sizeof
import random
from select import select


def choose_secret(file):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    f = open(file, mode="rt", encoding="utf-8")
    palabras = f.read()
    palabras = palabras.upper()
    palabras = palabras.split("\n")
    return random.choice(palabras)

secret = choose_secret("palabras_reduced.txt")
print(secret)
    
def compare_words(word, secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position = []
    same_letter = []
    for i in range(len(word)):
      if word[i] == secret[i]:
        same_position.append(i)
      else:
        for j in range(len(word)):
          if(word[i] == secret[j]):
            same_letter.append(i)
          
    return (same_position, same_letter)
  
tupla = compare_words("CAMPO","CREMA")
print(tupla)

def print_word(word,same_letter_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    auxWord = ["-","-","-","-","-"]
    for i in range(len(same_letter_position)):
      auxWord[same_letter_position[i]] = word[same_letter_position[i]].upper()
    for i in range(len(same_letter)):
      auxWord[same_letter[i]] = word[same_letter[i]].lower()
    
    transformed = ""      
    for i in range(len(auxWord)):
      transformed += auxWord[i]
    return transformed
  
print_word('CAMPO',tupla[0],tupla[1])
    
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    f = open(filename, mode="rt", encoding="utf-8")
    palabras = f.read()
    palabras = palabras.upper()
    palabras = palabras.split("\n")
    for i in range(len(palabras)):
        if len(palabras[i]) > 5:
          palabras.pop(i)
  
    for i in range(len(palabras)):
        if "Á" in palabras[i] or "É" in palabras[i] or "Í" in palabras[i] or "Ó" in palabras[i] or "Ú" in palabras[i]:
          palabras.pop(i)
    selected = []
    
    for i in range(15):
      randomWord = random.choice(palabras)
      if randomWord in selected:
          nothing = "nothing"
      else:
        selected.append(randomWord)
        
    return (selected, random.choice(selected))
    
choose_secret_advanced("palabras_extended.txt")


def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    print("Write a word of 5 letters: ")
    word = input()
    for i in range(selected):
      if selected[i] != word:
        print("Not in list")
        check_valid_word(selected)
      else:
        return word

if __name__ == "__main__":
    secret=choose_secret("palabras_reduced.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words()
        resultado=print_word()
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
