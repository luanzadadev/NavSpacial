from meteor import Meteor
from random import randint
from settings import *

class MeteorGenerator():
	def __init__(self, caminho_do_meteoro, group_do_meteoro):
		self.caminho_do_meteoro = caminho_do_meteoro
		self.group_do_meteoro = group_do_meteoro

		self.tempo_maximo_entre_os_meteoros = 0.6
		self.tempo_atual_entre_os_meteoros = 0


	def gerador_timer(self, delta_time):
		self.tempo_atual_entre_os_meteoros -= delta_time

		if self.tempo_atual_entre_os_meteoros <= 0:
			Meteor(
				posicao_inicial = (randint(100, LARGURA_DA_JANELA - 100), -50),
				caminho = self.caminho_do_meteoro,
				groups = self.group_do_meteoro
				)
			self.tempo_atual_entre_os_meteoros = self.tempo_maximo_entre_os_meteoros


	def update(self, delta_time):
		self.gerador_timer(delta_time)