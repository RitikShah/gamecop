import pygame
from collections import namedtuple


class Entity(pygame.sprite.Sprite):
    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.size = namedtuple('size', 'width height')(*size)
        self.image = pygame.Surface([self.size.width, self.size.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
