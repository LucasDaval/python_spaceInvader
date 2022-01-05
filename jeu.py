import pygame
import threading
import math
import time

from random import randrange

from Joueur import joueur
from Vecteurs import vecteurs
from Ennemis import ennemis

# ecran = pygame.display.set_mod((0,0), pygame.FULLSCREEN)
ecran = pygame.display.set_mode((500,500))
pygame.display.set_caption("Space Invader 3000")

ennemies = []

distance = 30
points = 0

initPlayer = joueur()

timeToGenerateEnemy = randrange(4, 6)

clock = pygame.time.Clock()
pygame.init()
initTimer = pygame.time.get_ticks()
font = pygame.font.SysFont("comicsansms", 22)

# Ajout de l'image de fond
image = pygame.image.load("backg.jpg")

newEnnemy = True
loop = True
play = True

# while play:

while loop:

    # On initialise l'écran de jeu
    ecran.blit(image, (-40,-40))
    ecran.blit(font.render(f"Points : {points}", True, (250, 250, 250)), (4, 4))

    # On initialise le cercle du perso

    # Initialisation des ennemis en fonction du temps
    seconds=(pygame.time.get_ticks()-initTimer)/1000

    # Ne s'exécute qu'une seule fois
    if points != 0:
        if points%5 == 0 and newEnnemy:
            e = ennemis(1, initPlayer.Y, 30)
            ennemies.append(e)
            newEnnemy = False
    if points >5:
        timeToGenerateEnemy = randrange(1, 3)

    if seconds>timeToGenerateEnemy:
        e = ennemis(2, initPlayer.Y, 30)
        if points > 25:
            e2 = ennemis(2, initPlayer.Y, 100)
            ennemies.append(e2)
        ennemies.append(e)
        initTimer = pygame.time.get_ticks()

    for e in ennemies:
        e.update(pygame.time.get_ticks(), 2)
        if points > 5:
            e.update(pygame.time.get_ticks(), 2.5)
        if points > 15:
            e.update(pygame.time.get_ticks(), 3)
        
        e.draw(ecran)

        # Détection des collisions avec ennemis
        if math.sqrt((initPlayer.X - e.X )**2 + (initPlayer.Y - e.Y)**2) < distance :
            loop = False

        if e.X < 0:
            ennemies.remove(e)
            points += 1
        
    # Ajout des evennements au cliques sur une touche par user
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            initPlayer.update(event)
            if event.key == pygame.K_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False

    initPlayer.draw(ecran)
    pygame.display.flip()
    clock.tick(60)


ecran.blit(font.render("Vous avez perdu à {points} points !", True, (250, 250, 250)), (200, 200))
ecran.blit(font.render("Pour rejouer, appuyer sur R", True, (250, 250, 250)), (220, 180))
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            loop = True
    if event.type == pygame.QUIT:
        play = False


pygame.quit()