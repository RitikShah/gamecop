import pygame
from collections import namedtuple


LIMIT_X =  600
LIMIT_Y =  800

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.size = namedtuple('size', 'width height')(*size)
        self.image = pygame.Surface([self.size.width, self.size.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        '''This bit [velocity] is hard coded; idk why'''
        self.velocity = 2   

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.rect.x - self.velocity > 0: # move left spaceshit to the left; a pressed
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.rect.x + self.velocity < LIMIT_X - self.size.width: # move left spaceshit to the right; d pressed
            self.rect.x += self.velocity
        if keys_pressed[pygame.K_w] and self.rect.y - self.velocity > 0: # move left spaceshit up; w pressed
            self.rect.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.rect.y + self.velocity < LIMIT_Y - self.size.height: # move left spaceshit down; s pressed
            self.rect.y += self.velocity
