import pygame
import Levels
from Sprites import *

is_fever = False

class Fever():
    def __init__(self):
        self.is_fever = False

    def feverTime(self,hero_sprites,ghost_sprites):
        pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, True)

'''def feverTime():
    global BALLS
    for i in range(2):
        BALLS.append(Block((200, 242, 0), Rect(300, 400, 20, 20), 10))
    for BALL in BALLS:
        BALL.speed = 10

        pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, True):'''
