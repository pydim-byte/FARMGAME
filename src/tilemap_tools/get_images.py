import pygame


def get_images(name,count):
    images = []
    for i in range(count):
        img = pygame.image.load(f'assets/images/{name}/{i}.png').convert_alpha()
        images.append(img)
    return images 