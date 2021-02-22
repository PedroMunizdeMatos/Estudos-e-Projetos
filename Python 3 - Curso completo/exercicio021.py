# faça um programa que abra e reproduza o áudio de um arquivo mp3.
# rever pygame posteriormente (atualmente não funcional)

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
