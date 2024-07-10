

import pygame
from pygame.sprite import AbstractGroup 


class Wall(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, x:int, y:int, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

        self.image = pygame.Surface((width,height))
        self.image.fill((133,245,70))
         
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        