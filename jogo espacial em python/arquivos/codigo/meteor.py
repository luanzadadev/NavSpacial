import pygame
from settings import *

class Meteor(pygame.sprite.Sprite):
	def __init__(self, posicao_inicial, caminho, groups):
		super().__init__(groups)

		
		self.image = pygame.image.load(caminho).convert_alpha()
		self.rect = self.image.get_rect(center = posicao_inicial)

		
		self.posicao = pygame.math.Vector2(self.rect.center)
		self.direcao = pygame.math.Vector2(0, 1)
		self.velocidade = 300


	def mover(self, delta_time):
		self.posicao += self.direcao * self.velocidade * delta_time
		self.rect.center = self.posicao


	def quando_fora_da_tela(self):
		if self.rect.top > ALTURA_DA_JANELA:
			self.kill()

	def update(self, delta_time):
		self.mover(delta_time)
		self.quando_fora_da_tela()