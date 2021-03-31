import random


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)


def rand_color():
    return (
        round((random.randrange(0, 255) + 255) / 2),
        round((random.randrange(0, 255) + 255) / 2),
        round((random.randrange(0, 255) + 255) / 2),
    )
