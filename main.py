import pygame
from entity import Entity
from keys import keys
from color import green

pygame.init()


DISPLAY = pygame.Surface((200, 300))
CLOCK = pygame.time.Clock()
FPS = 60

# 

pygame.display.set_caption("Hopper")
WIN = pygame.display.set_mode((600, 800))

def x_button():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def loop():
    clock  = pygame.time.Clock()

    char = Entity(green, (20, 60))

    while True:
        pygame.draw.rect(WIN, char.color, char.rect)

        x_button()

        key = pygame.key.get_pressed()
        if key[keys['escape']]:
            return 'quit'

        pygame.display.flip()
        clock.tick(FPS)

def main():
    #for da game loopers
    loop()


if __name__ == "__main__":
    main()
