import pygame
#comando nescessario para iniciar a biblioteca pygame
pygame.init()
#arquivo que vai tocar -> play no arquivo
pygame.mixer.music.load("Curso_em_video/musica/musica1.mp3")
pygame.mixer.music.play()
#para encerrar antes a música
input("Pressione Enter para sair")