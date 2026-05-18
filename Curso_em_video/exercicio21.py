import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Curso_em_video/musica/musica1.mp3")
pygame.mixer.music.play()

input("Pressione Enter para sair")