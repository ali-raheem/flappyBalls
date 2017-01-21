#!/usr/bin/python
import pygame
from pygame.locals import *
from random import randint
from time import sleep

class flappyBalls():
	def __init__(self):
		pygame.init()
		self.screenH = 800
		self.screenW = 640
		self.screen = pygame.display.set_mode((self.screenW, self.screenH))
		self.splash = pygame.image.load("images/splash.png")
		self.gameover = pygame.image.load("images/gameover.png")
		self.bg = pygame.image.load("images/background.png")
		self.pipeu = pygame.image.load("images/pipeu.png")
		self.piped = pygame.image.load("images/piped.png")
		self.bird = pygame.image.load("images/bird.png")
		self.pipeH = 512
		self.pipeW = 128
		self.birdR = 32
		self.birdH = 64
		self.scoreFont = pygame.font.SysFont("monospace", 32)
		
	def showSplash(self):
		self.screen.blit(self.splash, (0,0))
		pygame.display.flip()
		sleep(3)
		
	def showGameover(self):
		self.screen.blit(self.gameover, (0,0))
		pygame.display.flip()
		sleep(3)
		
	def newpipe(self):
		self.pipeX = self.screenW
		self.pipeY = randint(self.screenH-self.pipeH, self.screenH)
		self.pipeGap = randint(3*self.birdH, 5*self.birdH)
		
	def play(self):
		self.birdX = self.screenW/2 - self.birdR 
		self.birdY = self.screenH/2 - self.birdR
		self.score = 0
		self.newpipe()

		done = False
		while not done:
			self.pipeX -= 2
			if(self.pipeX + self.pipeW < 0):
				self.newpipe()
				self.score += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_UP] != 0:
				self.birdY -= 10
			self.birdY += 3
			if(self.birdY <= 0):
				done = True
			if(self.birdY >= self.screenH - self.birdR):
				done = True

			if (self.birdY+self.birdH > self.pipeY) and \
			   (self.birdY < self.pipeY+self.pipeH) and \
			   (self.birdX+self.birdH > self.pipeX) and \
			   (self.birdX< self.pipeX+self.pipeW):
				done = 1

			pipeY2 = self.pipeY - 512 - self.pipeGap
			if (self.birdY+self.birdH > pipeY2) and \
			   (self.birdY < pipeY2+self.pipeH) and \
			   (self.birdX+self.birdH > self.pipeX) and \
			   (self.birdX< self.pipeX+self.pipeW):
				done = 1
	
			self.screen.blit(self.bg, (0,0))
			self.screen.blit(self.pipeu, (self.pipeX, self.pipeY))
			self.screen.blit(self.piped, (self.pipeX, self.pipeY - 512 - self.pipeGap))
			self.screen.blit(self.bird, (self.birdX, self.birdY))
			scoreText = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
			self.screen.blit(scoreText, (self.screenW-50, 50))
			pygame.display.flip()

if __name__ == "__main__":
	game = flappyBalls()
	game.showSplash()
	while True:
		game.play()
		game.showGameover()

