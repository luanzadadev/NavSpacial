import pygame

class Laser(pygame.sprite.Sprite):
	def __init__(self, posicao_inicial, caminho, game_manager, group_do_meteoro, groups):
		super().__init__(groups)

		
		self.image = pygame.image.load('arquivos/graficos/laser-do-jogador.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = posicao_inicial)

		
		self.posicao = pygame.math.Vector2(self.rect.center)
		self.direcao = pygame.math.Vector2(0, -1)
		self.velocidade = 500

		
		self.group_do_meteoro = group_do_meteoro

		
		self.game_manager = game_manager

		
		self.som_de_explosao = pygame.mixer.Sound('arquivos/sons/som_de_explosao.ogg')
		self.som_de_explosao.set_volume(0.8)


	def mover(self, delta_time):
		self.posicao += self.direcao * self.velocidade * delta_time
		self.rect.center = self.posicao


	def colisao(self):
		for sprite in self.group_do_meteoro.sprites():
			if sprite.rect.colliderect(self.rect):
				self.game_manager.aumentar_pontuacao()
				self.som_de_explosao.play()
				sprite.kill()
				self.kill()


	def quando_fora_da_tela(self):
		if self.rect.bottom < 0:
			self.kill()


	def update(self, delta_time):
		self.mover(delta_time)

		self.colisao()

		self.quando_fora_da_tela()