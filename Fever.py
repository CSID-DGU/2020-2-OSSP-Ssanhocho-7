import pygame
import Levels
from Sprites import *

is_fever = False

class Fever():
    def __init__(self):
        self.is_fever = False

    def feverTime(self,hero_sprites,ghost_sprites):
        pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, True)
