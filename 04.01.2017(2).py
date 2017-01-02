import pygame.sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
mi_imagen=pygame.image.load("ball.gif")
posX=200
posY=100
velocidad=5
Blanco=(255,255,255)
derecha=true

while true:
    ventana.fill(Blanco)
    ventana.blit(mi_imagen,(posX,posY))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==K_LEFT:
               posX-=velocidad
            elif event.key==K_RIGHT:
                pos+=velocidad
        elif event.type==pygame.KEYUP:
            if event.key==K_LEFT:
                print ("Teclaizquierda")
            elif event.key==K_RIGHT:
                print ("tecla derecha")
                
