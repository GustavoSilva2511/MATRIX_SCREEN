from sys import exit
from pygame import QUIT
from time import sleep
from baguncinha import *

pygame.init()

font = pygame.font.SysFont("Bodoni", font_size, False, False)

while True:
    screen.fill(black)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    for j in range(len(obj)):
        for i in range(20):
            text = font.render(obj[j].list_alf[randint(0, len(obj[j].list_alf) - 1)], False, (i*7, 255, i*7))
            text.set_alpha((i * 10))
            screen.blit(text, (obj[j].x, obj[j].y + i * (font_size-5)))

    for i in obj:
        i.updade()

    pygame.display.flip()
    sleep(speed_loop)


