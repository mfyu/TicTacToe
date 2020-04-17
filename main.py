import sys, pygame, math

def drawNewBoard(screen):
	global board, playerTurn, gameOver
	playerTurn = 1
	gameOver = False
	board = [[None, None, None],
			 [None, None, None],
			 [None, None, None]]
	screen.fill(black)
	pygame.draw.line(screen, (250,250,250), (100, 0), (100, 300), 2)
	pygame.draw.line(screen, (250,250,250), (200, 0), (200, 300), 2)
	pygame.draw.line(screen, (250,250,250), (0, 100), (300, 100), 2)
	pygame.draw.line(screen, (250,250,250), (0, 200), (300, 200), 2)
	font = pygame.font.SysFont("Arial", 18)
	text = font.render("Player 1 Turn (X)", True, white)
	screen.blit(text, (90,310))


def drawMove(screen, col, row, xo):
	x = col*100+50
	y = row*100+50
	if (xo == 'O'):
		pygame.draw.circle(screen, white, (x,y), 30,2)
		board[row][col] = 'O'
	elif (xo == 'X'):
	    pygame.draw.line(screen, white, (x-25,y-25), (x+25,y+25), 2)
	    pygame.draw.line(screen, white, (x+25,y-25), (x-25,y+25), 2)
	    board[row][col] = 'X'



def playerMove(screen):
	global playerTurn
	if (pygame.mouse.get_pressed() == (1,0,0)):
		pos = pygame.mouse.get_pos() 
		col = math.floor(pos[0]/100)
		row = math.floor(pos[1]/100)
		
		if (playerTurn==1):
			drawMove(screen, col, row, 'X')
			font = pygame.font.SysFont("Arial", 18)
			text = font.render("Player 2 Turn (O)", True, white)
			pygame.draw.rect(screen, black, [0, 310, 300, 330])
			screen.blit(text, (90,310))
			playerTurn = 2
		else:
			drawMove(screen, col, row, 'O')
			font = pygame.font.SysFont("Arial", 18)
			text = font.render("Player 1 Turn (X)", True, white)
			pygame.draw.rect(screen, black, [0, 310, 300, 330])
			screen.blit(text, (90,310))
			playerTurn = 1

def p1win(screen):
	font = pygame.font.SysFont("Arial", 22)
	text = font.render("Player 1 Wins!", True, (0,250,0))
	pygame.draw.rect(screen, black, [0, 310, 300, 330])
	screen.blit(text, (90,300))
	font = pygame.font.SysFont("Arial", 18)
	text = font.render("Click to play again", True, (0,250,0))
	screen.blit(text, (90,325))

def p2win(screen):
	font = pygame.font.SysFont("Arial", 22)
	text = font.render("Player 2 Wins!", True, (0,250,0))
	pygame.draw.rect(screen, black, [0, 310, 300, 330])
	screen.blit(text, (90,300))
	font = pygame.font.SysFont("Arial", 18)
	text = font.render("Click to play again", True, (0,250,0))
	screen.blit(text, (90,325))

def draw(screen):
	font = pygame.font.SysFont("Arial", 22)
	text = font.render("Draw", True, (0,250,0))
	pygame.draw.rect(screen, black, [0, 310, 300, 330])
	screen.blit(text, (130,300))
	font = pygame.font.SysFont("Arial", 18)
	text = font.render("Click to play again", True, (0,250,0))
	screen.blit(text, (90,325))

def checkWin(screen):
	global board, gameOver
	for row in range (0,3):
		#row win
		if ((board[row][0] == board[row][1] == board[row][2]) and board[row][0] is not None):
			pygame.draw.line(screen, (0,250,0), (0, row*100+50), (300, row*100+50), 2)
			if (board[row][0]=='X'):
				p1win(screen)
			else:
				p2win(screen)
			gameOver = True
	for col in range (0,3):
		#col win
		if ((board[0][col] == board[1][col] == board[2][col]) and board[0][col] is not None):
			pygame.draw.line(screen, (0,250,0), (col*100+50,0), (col*100+50,300), 2)
			if (board[0][col]=='X'):
				p1win(screen)
			else:
				p2win(screen)
			gameOver = True

	#diagonal wins
	if ((board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not None):
		pygame.draw.line(screen, (0,250,0), (0,0), (300,300), 2)
		if (board[0][0]=='X'):
			p1win(screen)
		else:
			p2win(screen)
		gameOver = True
	if ((board[2][0] == board[1][1] == board[0][2]) and board[2][0] is not None):
		pygame.draw.line(screen, (0,250,0), (0,300), (300,0), 2)
		if (board[2][0]=='X'):
			p1win(screen)
		else:
			p2win(screen)
		gameOver = True
	#draw
	if (board[0][0] is not None and board[0][1] is not None and board[0][2] is not None and board[1][0] is not None and board[1][1] is not None and
		board[1][2] is not None and board[2][0] is not None and board[2][1] is not None and board[2][2]):
		draw(screen)
		gameOver = True
				
#start game
pygame.init()
global board, playerTurn, gameOver
black = 0,0,0
white = 255,255,255
playerTurn = 1
gameOver = False
board = [[None, None, None],
		 [None, None, None],
		 [None, None, None]]
screen = pygame.display.set_mode((300,350))
drawNewBoard(screen)


while 1:
    for event in pygame.event.get():
    	pygame.display.update()
    	if (event.type == pygame.QUIT):
    		sys.exit()
    	
    	elif (event.type is pygame.MOUSEBUTTONDOWN):
    		if (gameOver):
    			drawNewBoard(screen)
    		else:
    			playerMove(screen)
    			checkWin(screen)


    		




   



    