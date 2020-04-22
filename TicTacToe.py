from sys import exit
from os import environ
import pygame, math, sys

SCREENSIZE = (300, 370)

environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
white = (255,255,255)
black = (0,0,0)
pygame.font.init()
fnt = pygame.font.SysFont("Arial", 18)



class TicTacToe:
	def __init__(self):
		self.statusLabel = "connecting"
		self.playersLabel = "0 players"
		self.turn = 0
		self.board = [[None, None, None],[None, None, None],[None, None, None]]
		self.gameOver = False
		self.draw = False
		self.drawNewBoard()
		
	
	def Events(self):
		for event in pygame.event.get():
			pygame.display.update()
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.gameOver is False:
					self.Click(event)
				else:
					self.newGame()
					
	
	def Turn(self, data):

		print("turn")
		row = data['row']
		col = data['col']
		print(data)
		white = (255,255,250)

		x = col*100+50
		y = row*100+50
		#check if board position is empty
		if (row<3 and col<3):
			if (self.board[row][col] is None):
				if ((self.turn == 2 or self.turn==0) and int(data['id'])%2==0):
					
					
					pygame.draw.circle(screen, white, (x,y), 30,2)
					self.board[row][col] = 'O'
					self.turn = 1
					print(self.turn)
				elif((self.turn == 1 or self.turn==0) and int(data['id'])%2!=0):
					
					
					pygame.draw.line(screen, white, (x-25,y-25), (x+25,y+25), 2)
					pygame.draw.line(screen, white, (x+25,y-25), (x-25,y+25), 2)
					self.board[row][col] = 'X'
					self.turn = 2
					print(self.turn)

			self.checkWin()
			if self.gameOver:
				pygame.draw.rect(screen, black, [0, 310, 300, 330])
				if (self.draw):
					txt = "Draw" 
				elif (self.turn == 2):
					txt = "X Wins!"
				else:
					txt = "O Wins!"
				text = fnt.render(txt, True, (0,250,0))
				screen.blit(text, (90,310))
				text = fnt.render("Click to play again", True, (0,250,0))
				screen.blit(text, (80,335))
				pygame.display.update()
			else:
				pygame.draw.rect(screen, black, [0, 310, 300, 330])
				if (self.turn == 1):
					txt = "X's Turn"
				else:
					txt = "O's Turn"
				
				text = fnt.render(txt, True, white)
				screen.blit(text, (90,310))
				pygame.display.update()

	def checkWin(self):
	
		for row in range (0,3):
			#row win
			if ((self.board[row][0] == self.board[row][1] == self.board[row][2]) and self.board[row][0] is not None):
				pygame.draw.line(screen, (0,250,0), (0, row*100+50), (300, row*100+50), 2)
				if (self.board[row][0]=='X'):
					print("X win")
					
				else:
					print("O win")
					
				self.gameOver = True
				return True
		for col in range (0,3):
			#col win
			if ((self.board[0][col] == self.board[1][col] == self.board[2][col]) and self.board[0][col] is not None):
				pygame.draw.line(screen, (0,250,0), (col*100+50,0), (col*100+50,300), 2)
				if (self.board[0][col]=='X'):
					print("X win")
					
				else:
					print("O win")
					
				self.gameOver = True
				return True

		#diagonal wins
		if ((self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] is not None):
			pygame.draw.line(screen, (0,250,0), (0,0), (300,300), 2)
			if (self.board[0][0]=='X'):
				print("X win")
				
			else:
				print("O win")
				
			self.gameOver = True
			return True
		if ((self.board[2][0] == self.board[1][1] == self.board[0][2]) and self.board[2][0] is not None):
			pygame.draw.line(screen, (0,250,0), (0,300), (300,0), 2)
			if (self.board[2][0]=='X'):
				print("X win")
				
			else:
				print("O win")
				
			self.gameOver = True
			return True
		#draw
		if (self.board[0][0] is not None and self.board[0][1] is not None and self.board[0][2] is not None and 
			self.board[1][0] is not None and self.board[1][1] is not None and self.board[1][2] is not None and 
			self.board[2][0] is not None and self.board[2][1] is not None and self.board[2][2]):
			print("draw")
			self.draw = True
			self.gameOver = True
			return True

	def drawNewBoard(self):
		self.turn = 0
		self.gameOver = False
		self.draw = False
		self.board = [[None, None, None],
				 [None, None, None],
				 [None, None, None]]
		screen.fill(black)
		pygame.draw.line(screen, (250,250,250), (100, 0), (100, 300), 2)
		pygame.draw.line(screen, (250,250,250), (200, 0), (200, 300), 2)
		pygame.draw.line(screen, (250,250,250), (0, 100), (300, 100), 2)
		pygame.draw.line(screen, (250,250,250), (0, 200), (300, 200), 2)
		text = fnt.render("X's Turn", True, white)
		#screen.blit(text, (90,310))
		pygame.display.update()
