import pygame
import Levels
from Sprites import *

is_fever = False


class Fever():
    global fever_score
    def __init__(self):
        self.is_fever = False

    def feverTime(self,hero_sprites,ghost_sprites):
        pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False)

        return True
