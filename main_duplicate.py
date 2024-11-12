import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(pygame.image.load('spaceship.png'))

running=True
while running:
    screen.blit(pygame.image.load('background.png'), (0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()