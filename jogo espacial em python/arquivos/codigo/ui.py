import pygame

class UI(pygame.sprite.Sprite):
	def __init__(self, posicao_do_texto, janela, game_manager):
		super().__init__()

		
		self.posicao_do_texto = posicao_do_texto
		self.janela = janela
		self.game_manager = game_manager

		
		self.font = pygame.font.Font(None, 75)


	def mostrar_pontuacao(self):
		text_surf = self.font.render(str(self.game_manager.pontuacao), True, (255, 255, 255))
		text_rect = text_surf.get_rect(center = self.posicao_do_texto)

		self.janela.blit(text_surf, text_rect)

	def mostrar_texto_de_game_over(self):

		
		text_surf_01 = self.font.render('GAME OVER', True, (255, 255, 255))
		text_rect_01 = text_surf_01.get_rect(center = (640, 320))

		
		text_surf_02 = self.font.render(f'Pontuação: {self.game_manager.pontuacao}', True, (255, 255, 255))
		text_rect_02 = text_surf_02.get_rect(center = (640, 380))

		
		font_do_credito = pygame.font.Font(None, 50)

		text_surf_03 = font_do_credito.render('Desenvolvido por LuanZada - v2.0 - 19/08/2024', True, (255, 255, 255))
		text_rect_03 = text_surf_03.get_rect(center = (640, 680))

		self.janela.blit(text_surf_01, text_rect_01)
		self.janela.blit(text_surf_02, text_rect_02)
		self.janela.blit(text_surf_03, text_rect_03)
