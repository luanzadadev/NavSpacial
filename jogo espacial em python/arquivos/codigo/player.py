import pygame
from laser import Laser
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, posicao_inicial, caminho, game_manager, group_do_laser, group_do_meteoro, groups):
		super().__init__(groups)

		
		self.image = pygame.image.load(caminho).convert_alpha()
		self.rect = self.image.get_rect(center = posicao_inicial)

		
		self.posicao = pygame.math.Vector2(self.rect.center)
		self.direcao = pygame.math.Vector2()
		self.velocidade = 400

		
		self.group_do_laser = group_do_laser
		self.pode_atirar = True
		self.tempo_maximo_entre_os_lasers = 0.2
		self.tempo_atual_dos_lasers = 0

	
		self.group_do_meteoro = group_do_meteoro
		self.game_over = False

		
		self.game_manager = game_manager

		
		self.som_do_laser = pygame.mixer.Sound('arquivos/sons/som_do_laser.aiff')
		self.som_do_laser.set_volume(0.3)

	def laser_timer(self, delta_time):
		if not self.pode_atirar:
			self.tempo_atual_dos_lasers -= delta_time

			if self.tempo_atual_dos_lasers <= 0:
				self.tempo_atual_dos_lasers = self.tempo_maximo_entre_os_lasers
				self.pode_atirar = True


	def input(self):
		keys = pygame.key.get_pressed()

		
		if keys[pygame.K_UP]:
			self.direcao.y = -1
		elif keys[pygame.K_DOWN]:
			self.direcao.y = 1
		else:
			self.direcao.y = 0

		
		if keys[pygame.K_LEFT]:
			self.direcao.x = -1
		elif keys[pygame.K_RIGHT]:
			self.direcao.x = 1
		else:
			self.direcao.x = 0

		
		if keys[pygame.K_SPACE] and self.pode_atirar:
			laser = Laser(self.rect.midtop, self.som_do_laser , self.game_manager, self.group_do_meteoro, self.group_do_laser)
			self.som_do_laser.play()
			self.pode_atirar = False


	def movimento(self, delta_time):

		
		if self.direcao.magnitude() != 0:
			self.direcao = self.direcao.normalize()

		
		self.posicao.x += self.direcao.x * self.velocidade * delta_time
		self.rect.centerx = self.posicao.x

		
		self.posicao.y += self.direcao.y * self.velocidade * delta_time
		self.rect.centery = self.posicao.y


	def limitar_movimento(self):

		
		if self.rect.left <= 10:
			self.posicao.x = 10 + self.rect.width * 0.5
			self.rect.left = 10

		
		if self.rect.right >= LARGURA_DA_JANELA - 10:
			self.posicao.x = (LARGURA_DA_JANELA - 10) - self.rect.width * 0.5
			self.rect.right = LARGURA_DA_JANELA - 10

		
		if self.rect.top <= 10:
			self.posicao.y = 10 + self.rect.height * 0.5
			self.rect.top = 10

		
		if self.rect.bottom > ALTURA_DA_JANELA - 10:
			self.posicao.y = (ALTURA_DA_JANELA - 10) - self.rect.height * 0.5
			self.rect.bottom = ALTURA_DA_JANELA - 10


	def colisao(self):
		for sprite in self.group_do_meteoro.sprites():
			if sprite.rect.colliderect(self.rect):
				self.game_over = True


	def update(self, delta_time):
		self.laser_timer(delta_time)

		self.input()
		self.movimento(delta_time)
		self.limitar_movimento()

		self.colisao()
