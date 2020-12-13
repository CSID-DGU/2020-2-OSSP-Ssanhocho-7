import pygame
import Levels
from Sprites import *

is_fever = False

<<<<<<< HEAD
class Fever():
=======

class Fever():
    global fever_score
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
    def __init__(self):
        self.is_fever = False

    def feverTime(self,hero_sprites,ghost_sprites):
<<<<<<< HEAD
        pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, True)
=======
        pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False)

        return True
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
