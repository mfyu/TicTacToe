import sys, pygame

pygame.init()

black = 0,0,0

screen = pygame.display.set_mode((300,300))
screen.fill(black)

while 1:
    for event in pygame.event.get():
    	if (event.type == pygame.QUIT):
    		sys.exit()
    #draw board
    pygame.draw.line(screen, (250,250,250), (100, 0), (100, 300), 2)
    pygame.draw.line(screen, (250,250,250), (200, 0), (200, 300), 2)
    pygame.draw.line(screen, (250,250,250), (0, 100), (300, 100), 2)
    pygame.draw.line(screen, (250,250,250), (0, 200), (300, 200), 2)
    pygame.display.update()