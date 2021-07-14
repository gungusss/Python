import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
icon = pygame.image.load('KetDonk.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("NICE")

playerimg = pygame.image.load('character.png')
playerX = 400
playerY = 200

def player():
    screen.blit(playerimg,(playerX,playerY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30,30,30))
    player()
    pygame.display.update()

