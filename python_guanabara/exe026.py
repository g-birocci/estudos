import pygame

# Inicializar o pygame
pygame.init()

# Carregar e reproduzir música
pygame.mixer.music.load("C:/Users/gabri/Documents/estudos/python_guanabara/exe026.mp3")  # Certifique-se de que o arquivo "exe026.mp3" esteja no mesmo diretório
pygame.mixer.music.play()

# Manter o programa rodando para que a música possa ser ouvida
while pygame.mixer.music.get_busy():  # Verifica se a música ainda está tocando
    pygame.time.Clock().tick(10)  # Aguarda um curto intervalo
