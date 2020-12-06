import pygame
from Sprites import *
import random
MODE='randomMode'

# 초기화면 크기 = 606, 606
WIDTH = 606
HEIGHT = 606
WIDTH_e = 577
HEIGHT_e = 306
WIDTH_h = 606
HEIGHT_h = 606

class Level1():
	MODE='EASY'
	def __init__(self):
		self.info = 'level1'
	'''벽 만들기'''
	def setupWalls(self, wall_color):
		self.wall_sprites = pygame.sprite.Group()
		wall_positions = [[0, 0, 6, 306], # 맨 왼쪽
						  [0, 0, 576, 6], # 맨 위쪽
						  [0, 300, 576, 6], # 맨 아래쪽
						  [570, 0, 6, 306], # 맨 오른쪽
						  [150, 0, 6, 66], # 맨 위 왼쪽 |
						  [420, 0, 6, 66], # 맨 위 오른쪽 |
						  [210, 60, 154, 6], # ghost zone 위 가운데 -----
						  [60, 60, 36, 6], [60, 60, 6, 66], # 맨 위 왼쪽 ㄱ자 좌우반전한것
						  [480, 60, 36, 6], [510, 60, 6, 66], # 맨 위 오른쪽 ㄱ자 좌우반전한것
						  [120, 120, 36, 6], [420, 120, 36, 6], [120, 180, 36, 6], [420, 180, 36, 6], # 조그마한 - 4개
						  [60, 240, 36, 6], [60, 180, 6, 66], # 아래 왼쪽 L자
						  [480, 240, 36, 6], [510, 180, 6, 66], # 아래 오른쪽 L자 좌우반전한것
						  [150, 240, 6, 66], # 맨 아래 왼쪽 |
						  [420, 240, 6, 66], # 맨 아래 오른쪽 |
						  [210, 240, 154, 6], # ghost zone 아래 가운데 -----
						  [210, 120, 36, 6], # ghost zone start
						  [210, 120, 6, 66],
						  [210, 180, 154, 6],
						  [330, 120, 36, 6],
						  [360, 120, 6, 66], # ghost zone fin
						  ]
		for wall_position in wall_positions:
			wall = Wall(*wall_position, wall_color)
			self.wall_sprites.add(wall)
		return self.wall_sprites


	# EASY version ghost zone 문 만들기
	def setupGate(self, gate_color):
		global HEIGHT_e, WIDTH_e
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(WIDTH_e // 2, HEIGHT_e // 2, 84, 2, gate_color))
		return self.gate_sprites

	# EASY version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path):
		self.hero_sprites = pygame.sprite.Group()
		self.ghost_sprites = pygame.sprite.Group()
		self.hero_sprites.add(Player(WIDTH_e // 2, HEIGHT_e // 2 + 47, hero_image_path)) #439
		for each in ghost_images_path:
			role_name = each.split('/')[-1].split('.')[0]
			if role_name == 'Blinky': # 빨간색
				player = Player(257, 140, each)
				player.is_move = True
				player.tracks = [[0, -0.5, 4], [0.5, 0, 9], [0, 0.5, 11], [0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 11], [0, 0.5, 3],
								 [0.5, 0, 15], [0, -0.5, 15], [0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3],
								 [0, -0.5, 3], [-0.5, 0, 7], [0, -0.5, 3], [0.5, 0, 15], [0, 0.5, 15], [-0.5, 0, 3], [0, 0.5, 3],
								 [-0.5, 0, 3], [0, -0.5, 7], [-0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 11], [0, -0.5, 7], [0.5, 0, 5]]

				self.ghost_sprites.add(player)
			elif role_name == 'Clyde':
				player = Player(289, 140, each)
				player.is_move = True
				player.tracks = [[-1, 0, 2], [0, -0.5, 4], [0.5, 0, 5], [0, 0.5, 7], [-0.5, 0, 11], [0, -0.5, 7],
								 [-0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 7], [0, 0.5, 15], [0.5, 0, 15], [0, -0.5, 3],
								 [-0.5, 0, 11], [0, -0.5, 7], [0.5, 0, 3], [0, -0.5, 11], [0.5, 0, 9]]
				self.ghost_sprites.add(player)
			elif role_name == 'Inky':
				player = Player(225, 140, each)
				player.is_move = True
				player.tracks = [[1, 0, 2], [0, -0.5, 4], [0.5, 0, 10], [0, 0.5, 7], [0.5, 0, 3], [0, -0.5, 3],
								 [0.5, 0, 3], [0, -0.5, 15], [-0.5, 0, 15], [0, 0.5, 3], [0.5, 0, 15], [0, 0.5, 11],
								 [-0.5, 0, 3], [0, -0.5, 7], [-0.5, 0, 11], [0, 0.5, 3], [-0.5, 0, 11], [0, 0.5, 7],
								 [-0.5, 0, 3], [0, -0.5, 3], [-0.5, 0, 3], [0, -0.5, 15], [0.5, 0, 15], [0, 0.5, 3],
								 [-0.5, 0, 15], [0, 0.5, 11], [0.5, 0, 3], [0, -0.5, 11], [0.5, 0, 11], [0, 0.5, 3], [0.5, 0, 1]]
				self.ghost_sprites.add(player)
			elif role_name == 'Pinky':
				player = Player(319, 140, each)
				player.is_move = True
				player.tracks = [[0, -1, 4], [0.5, 0, 9], [0, 0.5, 11], [-0.5, 0, 23], [0, 0.5, 7], [0.5, 0, 3],
								 [0, -0.5, 3], [0.5, 0, 19], [0, 0.5, 3], [0.5, 0, 3], [0, 0.5, 3], [0.5, 0, 3],
								 [0, -0.5, 15], [-0.5, 0, 7], [0, 0.5, 3], [-0.5, 0, 19], [0, -0.5, 11], [0.5, 0, 9]]
				self.ghost_sprites.add(player)
		return self.hero_sprites, self.ghost_sprites


	# 아이템 만들기 (동전)
	def setupFood(self, food_color, bg_color):
		self.food_sprites = pygame.sprite.Group()
		for row in range(19):
			for col in range(19):
				if (row == 7 or row == 8) and (col == 8 or col == 9 or col == 10):
					continue
				else:
					food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
					is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
					if is_collide:
						continue
					is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
					if is_collide:
						continue
					self.food_sprites.add(food)
		return self.food_sprites

	# EASY version setupFood
	def setupFood(self, food_color, bg_color):
		self.food_sprites = pygame.sprite.Group() # 그룹 객체
		for row in range(9):
			for col in range(18):
				if (row == 3 or row == 4) and (col == 7 or col == 8 or col == 9 or col == 10):
					continue
				else:
					if ((row == 1 or row == 8) and (col == 0 or col == 18)) or ((row == 2 or row == 5) and (col == 0 or col == 3 or col == 15)):
						food = Food(30*col+23, 30*row+23, 10, 10, food_color, bg_color)

					else:
						food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
				is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
				if is_collide:
					continue
				is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
				if is_collide:
					continue
				self.food_sprites.add(food)
		return self.food_sprites

class Level2():
	MODE = 'HARD'
	def __init__(self):
		self.info = 'level2'
	'''벽 만들기'''
	def setupWalls(self, wall_color):
		self.wall_sprites = pygame.sprite.Group()
		wall_positions = [[0, 0, 6, 600], # 외벽
						  [0, 0, 600, 6],
						  [0, 600, 606, 6],
						  [600, 0, 6, 606],
						  [210, 240, 66, 6], # ghost zone start
						  [210, 240, 6, 66],
						  [210, 300, 184, 6],
						  [330, 240, 66, 6],
						  [390, 240, 6, 66], # ghost zone fin
						  [240, 0, 6, 66], # 맨 위 왼쪽 |
						  [360, 0, 6, 66], # 맨 위 오른쪽 |
						  [60, 60, 124, 6], [60, 60, 6, 36], # 맨 위 왼쪽 ㄱ자 좌우반전한것
						  [420, 60, 124, 6], [540, 60, 6, 36], # 맨 위 오른쪽 ㄱ자 좌우반전한것
						  [300, 60, 6, 66], # 맨 위 두번째 가운데 |
						  [180, 120, 66, 6], # 맨 위 두번째 왼쪽  -
						  [360, 120, 66, 6],  # 맨 위 두번째 오른쪽  -
						  [0, 150, 66, 6], # 맨 왼쪽 외벽쪽 -
						  [540, 150, 66, 6], # 맨 오른쪽 외벽쪽 -
						  [120, 120, 6, 66], [120, 180, 36, 6], # 맨 위 왼쪽 L자
						  [480, 120, 6, 66], [450, 180, 36, 6], # 맨 위 오른쪽 L자 좌우반전
						  [210, 180, 184, 6], # ghost zone 위 가운데 -----
						  [60, 210, 6, 36], [60, 240, 36, 6], # ghost zone 왼쪽 조그만 ㄴ자
						  [540, 210, 6, 36], [510, 240, 36, 6], # ghost zone 왼쪽 조그만 ㄴ자
						  [150, 240, 6, 66], [120, 300, 36, 6], # 맨 위 왼쪽 L자
						  [450, 240, 6, 66], [450, 300, 36, 6], # 맨 위 오른쪽 L자 좌우반전
						  [60, 300, 6, 66], [60, 360, 36, 6], # 맨 위 왼쪽 L자
						  [540, 300, 6, 66], [510, 360, 36, 6], # 맨 위 오른쪽 L자 좌우반전
						  [150, 360, 6, 66], [150, 360, 96, 6], # 맨 위 왼쪽 L자
						  [360, 360, 96, 6], [450, 360, 6, 66], # 맨 위 오른쪽 L자 좌우반전
						  [300, 360, 6, 66], [210, 420, 184, 6], # 밑에서 두번째 ㅗ자
						  [300, 480, 6, 66], [210, 540, 184, 6], # 맨 밑 ㅗ 자
						  [0, 420, 36, 6], # 맨 왼쪽 외벽쪽 -
						  [570, 420, 36, 6], # 맨 오른쪽 외벽쪽 -
						  [90, 420, 6, 66], [60, 480, 36, 6], # 맨 위 왼쪽 L자
						  [510, 420, 6, 66], [510, 480, 36, 6], # 맨 위 오른쪽 L자 좌우반전
						  [60, 540, 36, 6], # 맨 아래 왼쪽  -
						  [510, 540, 36, 6], # 맨 아래 오른쪽  -
						  [150, 480, 6, 120], [150, 480, 96, 6], # 맨 아래 ㅗ자 감싸는 박스 왼쪽
						  [360, 480, 96, 6], [450, 480, 6, 120] # 맨 아래 ㅗ자 감싸는 박스 오른쪽
						  ]

		for wall_position in wall_positions:
			wall = Wall(*wall_position, wall_color)
			self.wall_sprites.add(wall)
		return self.wall_sprites


	# HARD version ghost zone 문 만들기
	def setupGate(self, gate_color):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(276, 242, 54, 2, gate_color))
		return self.gate_sprites

	# HARD version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path):
		self.hero_sprites = pygame.sprite.Group()
		self.ghost_sprites = pygame.sprite.Group()
		self.hero_sprites.add(Player(WIDTH_h // 2, HEIGHT_h - 49, hero_image_path))
		for each in ghost_images_path:
			role_name = each.split('/')[-1].split('.')[0]
			if role_name == 'Blinky':
				player = Player(285, 259, each)
				player.is_move = True
				player.tracks = [[0, -0.5, 4], [0.5, 0, 9], [0, 0.5, 11], [0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 11], [0, 0.5, 3],
								 [0.5, 0, 15], [0, -0.5, 15], [0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3],
								 [0, -0.5, 3], [-0.5, 0, 7], [0, -0.5, 3], [0.5, 0, 15], [0, 0.5, 15], [-0.5, 0, 3], [0, 0.5, 3],
								 [-0.5, 0, 3], [0, -0.5, 7], [-0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 11], [0, -0.5, 7], [0.5, 0, 5]]

				self.ghost_sprites.add(player)
			'''elif role_name == 'Clyde':
				player = Player(319, 259, each)
				player.is_move = True
				player.tracks = [[-1, 0, 2], [0, -0.5, 4], [0.5, 0, 5], [0, 0.5, 7], [-0.5, 0, 11], [0, -0.5, 7],
								 [-0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 7], [0, 0.5, 15], [0.5, 0, 15], [0, -0.5, 3],
								 [-0.5, 0, 11], [0, -0.5, 7], [0.5, 0, 3], [0, -0.5, 11], [0.5, 0, 9]]
				self.ghost_sprites.add(player)
			elif role_name == 'Inky':
				player = Player(255, 259, each)
				player.is_move = True
				player.tracks = [[1, 0, 2], [0, -0.5, 4], [0.5, 0, 10], [0, 0.5, 7], [0.5, 0, 3], [0, -0.5, 3],
								 [0.5, 0, 3], [0, -0.5, 15], [-0.5, 0, 15], [0, 0.5, 3], [0.5, 0, 15], [0, 0.5, 11],
								 [-0.5, 0, 3], [0, -0.5, 7], [-0.5, 0, 11], [0, 0.5, 3], [-0.5, 0, 11], [0, 0.5, 7],
								 [-0.5, 0, 3], [0, -0.5, 3], [-0.5, 0, 3], [0, -0.5, 15], [0.5, 0, 15], [0, 0.5, 3],
								 [-0.5, 0, 15], [0, 0.5, 11], [0.5, 0, 3], [0, -0.5, 11], [0.5, 0, 11], [0, 0.5, 3], [0.5, 0, 1]]
				self.ghost_sprites.add(player)
			elif role_name == 'Pinky':
				player = Player(349, 259, each)
				player.is_move = True
				player.tracks = [[0, -1, 4], [0.5, 0, 9], [0, 0.5, 11], [-0.5, 0, 23], [0, 0.5, 7], [0.5, 0, 3],
								 [0, -0.5, 3], [0.5, 0, 19], [0, 0.5, 3], [0.5, 0, 3], [0, 0.5, 3], [0.5, 0, 3],
								 [0, -0.5, 15], [-0.5, 0, 7], [0, 0.5, 3], [-0.5, 0, 19], [0, -0.5, 11], [0.5, 0, 9]]
				self.ghost_sprites.add(player)'''
		return self.hero_sprites, self.ghost_sprites

	# 아이템 만들기 (동전)
	def setupFood(self, food_color, bg_color):
		self.food_sprites = pygame.sprite.Group()
		for row in range(19):
			for col in range(19):
				if (row == 7 or row == 8) and (col == 8 or col == 9 or col == 10):
					continue
				else:
					food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
					is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
					if is_collide:
						continue
					is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
					if is_collide:
						continue
					self.food_sprites.add(food)
		return self.food_sprites
#pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]
	# HARD version setupFood
	def setupFood(self, food_color, bg_color):
		self.food_sprites = pygame.sprite.Group()
		for row in range(19):
			for col in range(19):
				if (row == 7 or row == 8) and (col == 7 or col == 8 or col == 9 or col == 10 or col == 11):
					continue
				else:
					if ((row == 1 or row == 14) and (col == 0 or col == 18)) or ((row == 2 or row == 10) and (col == 0 or col == 3 or col == 10)):
						food = Food(30*col+23, 30*row+23, 20, 20, food_color, bg_color)
					else:
						food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
				is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
				if is_collide:
					continue
				is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
				if is_collide:
					continue
				self.food_sprites.add(food)
		return self.food_sprites
