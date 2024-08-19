class GameManager():
	def __init__(self):
		self.pontuacao = 0


	def aumentar_pontuacao(self):
		self.pontuacao += 1
		print(self.pontuacao)