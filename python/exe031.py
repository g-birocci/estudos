import random

# Lista de palavras
palavra = ["java", "webdeveloper", "programador", "tecnologia"]

# Desenho inicial
def drawing():
    print(" _                                             ")                                            
    print("| |                                            ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|")
    print("                    __/ |                      ")
    print("                   |___/                       ")

# Seleção de palavra aleatória
def palavra_random():
    return random.choice(palavra)

# Criação da palavra sublinhada
def palavra_sublinhada(choice):
    return list("_" * len(choice))

# Atualização do progresso da palavra
def forca_andamento(choice, guess, match):
    current_state = False
    for index, search in enumerate(choice):
        if match == search:
            guess[index] = search
            current_state = True
    palavra_forca = "".join(guess)
    return current_state, palavra_forca

# Controle de vidas
def lives(vidas):
    estados = [
        """
YOU LOSE!
  +---+    
  |   |    
  O   |    
 /|\\  |    
 / \\  |    
      |    
===========""",
        """
  +---+  
  |   |  
  O   |  
 /|\\  |  
 /    |  
      |  
=========""",
        """
  +---+  
  |   |  
  O   |  
 /|\\  |  
      |  
      |  
=========""",
        """
  +---+  
  |   |  
  O   |  
      |  
      |  
      |  
=========""",
        """
  +---+  
  |   |  
      |  
      |  
      |  
      |  
=========""",
    ]
    print(estados[6 - vidas])

# Jogar
def jogar():
    drawing()
    lives_quantity = 6
    choice = palavra_random()
    guess = palavra_sublinhada(choice)
    
    while True:
        print(f"\nPalavra: {' '.join(guess)}")
        letter = input("Escolha uma letra e tente adivinhar a palavra: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Por favor, insira apenas uma letra!")
            continue
        
        if letter in guess:
            print("Você já adivinhou essa letra. Tente outra.")
            continue
        
        current_state, palavra_forca = forca_andamento(choice, guess, letter)
        
        if current_state:
            print(f"\nMuito bem! A letra '{letter}' está na palavra secreta!")
        else:
            print(f"\nErrou! A letra '{letter}' não está na palavra secreta.")
            lives_quantity -= 1
            lives(lives_quantity)
            if lives_quantity == 0:
                print(f"\nVocê perdeu! A palavra secreta era: {choice}")
                break
        
        if "_" not in guess:
            print(f"\nParabéns! Você adivinhou a palavra: {choice}")
            break

# Iniciar o jogo
jogar()
