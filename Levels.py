import pygame
from Sprites import *
import random
import Game14

MODE= 'randomMode'

ghost_move_range=0.5

'''
setupWalls 원리
- width/70 : 벽의 두께 (+- width/70 : 위치 조절하려고 두께만큼 더하거나 뺌)
- 원래 맵 사진에서 벽 위치의 비율에 따라 적절한 수를 곱함
- [x, y, width, height]

setupGate, setupFood
- 화면에 표시되는 Gate와 Food의 비율을 계산하여 적절한 비율을 곱함
'''

# 좌표개 x축이랑 거리 y축이랑 거리

class Level1():
	MODE='EASY'
	def __init__(self):
		self.info = 'level1'
	'''벽 만들기'''
	def setupWalls(self, wall_color,width,height):
		self.wall_sprites = pygame.sprite.Group()
		wall_positions = [[0, 0, width/70, height], # 맨 왼쪽
	                    [0, 0, width, width/70], # 맨 위쪽
	                    [0, height-width/70, width, width/70], # 맨 아래쪽
	                    [width-width/110, 0, width/6, height], # 맨 오른쪽
	                    [width/4+width/70, 0, width/70, height/7+width/70], # 맨 위 왼쪽 | #x나누는수가 커지면 왼쪽으로 감,y,
	                    [width*ghost_move_range*6/4, 0, width/70, height/7+width/70], # 맨 위 오른쪽 |
	                    [width/3 + width/20, height/6.5, width/4, width/70], # ghost zone 위 가운데 -----
						[width/5+width/70, height*2/7.7, width/70, height/7],[width/5+width/70, height*2/7.7, width/2+width/12, height/70],
						[width*14/19+width/17,height*2/7.7,width/70,height/7],#ghostzone 바로 위 뚜껑 모양
	                    [width*2/19, height/6.5, width/18+width/70, width/70], [width*2/19, height/6.5, width/70, height*2/8], # 맨 위 왼쪽 ㄱ자 좌우반전한것
	                    [width*16/19, height/6.5, width/18+width/70, width/70], [width*17/19+4, height/6.5, width/70, height*2/8], # 맨 위 오른쪽ㄱ자
	                    [width*2/19, height/1.18, width/18+width/70, width/70], [width*2/19, height*3/5, width/70, height*2/8], # 아래 왼쪽 L자
	                    [width*16/19+2, height/1.18, width/18+width/70, width/70], [width*17/19+4, height*3/5, width/70, height*2/8], # 아래 오른쪽 L자 좌우반전한것
	                    [width/4+width/70, height/1.18 , width/70, height/7], # 맨 아래 왼쪽 |
	                    [width*3/4, height/1.18, width/70, height/7], # 맨 아래 오른쪽 |
	                    [width/3 + width/20, height/1.18, width/4, width/70], # ghost zone 아래 가운데 -----
	                    [width/3.2, height*2/5.5, width/18+width/50, width/70], # ghost zone start 위 가로
	                    [width/3.2, height*2/5.5, width/70, height*2/8], #세로
	                    [width/3.2, height*2/5.5+height*2/8, width/4+width/7.1, width/70], #가로
	                    [width*12/19, height*2/5.5, width/18+width/70, width/70], #ghost zone 위 가로
	                    [width/1.45, height*2/5.5, width/70, height*2/8], # ghost zone fin 세로
						[width/5+width/70, height/1.65, width/70, height/7.1],[width/5+width/70, height/1.34, width/2+width/10.25, height/70],
						[width*14/19+width/17,height/1.65,width/70,height/7.1]#ghostzone 바로 위 뚜껑 모양
	                    ]
		for wall_position in wall_positions:
			wall = Wall(*wall_position, wall_color)
			self.wall_sprites.add(wall)
		return self.wall_sprites

	# EASY version ghost zone 문 만들기
	def setupGate(self, gate_color, width, height):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(width/2.6, height*2/5.5, width/4, 2, gate_color)) #2는 화이트입니다, width/2 등 상수로 나눈것은 screen화면에 대한 비율을 밎추기위함입니다

		return self.gate_sprites

	# EASY version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path,width,height):
		hero_init_x = width/2
		hero_init_y = height*6/9
		self.hero_sprites = pygame.sprite.Group()
		self.ghost_sprites = pygame.sprite.Group()
		self.hero_sprites.add(Player(hero_init_x, hero_init_y , hero_image_path)) #width/2 등 상수로 나눈것은 screen화면에 대한 비율을 밎추기위함입니다
		for each in ghost_images_path:
			# 유령 이동경로 setup
			role_name = each.split('/')[-1].split('.')[0]
			# Player(x, y, image_path) : x, y = 유령 초기 위치 좌표
			if role_name == 'Blinky': # 빨간색
				player = Player(width/2, height/3, each)#width/2 등 상수로 나눈것은 screen화면에 대한 비율을 밎추기위함입니다
				player.is_move = True
				player.tracks = [[0, -ghost_move_range, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*18], [0, ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*14], [-ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*6],
								 [ghost_move_range, 0, ghost_move_range*30], [0, -ghost_move_range, ghost_move_range*30], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [-ghost_move_range, 0, ghost_move_range*6],
								 [0, -ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*14], [0, -ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*30], [-ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*6],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*14], [-ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*14], [-ghost_move_range, 0, ghost_move_range*22], [0, -ghost_move_range, ghost_move_range*14], [ghost_move_range, 0, ghost_move_range*10]]

				self.ghost_sprites.add(player)
			elif role_name == 'Clyde':
				player = Player(width/2, height/3, each)#width/2 등 상수로 나눈것은 screen화면에 대한 비율을 밎추기위함입니다
				player.is_move = True
				player.tracks = [[-ghost_move_range*2, 0, ghost_move_range*4], [0, -ghost_move_range, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*10], [0, ghost_move_range, ghost_move_range*14], [-ghost_move_range, 0, ghost_move_range*22], [0, -ghost_move_range, ghost_move_range*14],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*14], [-ghost_move_range, 0, ghost_move_range*14], [0, ghost_move_range, ghost_move_range*30], [ghost_move_range, 0, ghost_move_range*30], [0, -ghost_move_range, ghost_move_range*6],
								 [-ghost_move_range, 0, ghost_move_range*22], [0, -ghost_move_range, ghost_move_range*14], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*18]]
				self.ghost_sprites.add(player)
			elif role_name == 'Inky':
				player = Player(width/2, height/3, each)#width/2 등 상수로 나눈것은 screen화면에 대한 비율을 밎추기위함입니다
				player.is_move = True
				player.tracks = [[ghost_move_range*2, 0, ghost_move_range*4], [0, -ghost_move_range, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*20], [0, ghost_move_range, ghost_move_range*14], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*6],
								 [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*30], [-ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*22],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*14], [-ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*14],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*30], [ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*6],
								 [-ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*2]]
				self.ghost_sprites.add(player)
			elif role_name == 'Pinky':
				player = Player(width/2, height/3, each)#width/2 등 상수로 나눈것은 screen화면에 대한 비율을 밎추기위함입니다
				player.is_move = True
				player.tracks = [[0, -ghost_move_range*2, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*18], [0, ghost_move_range, ghost_move_range*22], [-ghost_move_range, 0, ghost_move_range*46], [0, ghost_move_range, ghost_move_range*14], [ghost_move_range, 0, ghost_move_range*6],
								 [0, -ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*38], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*6],
								 [0, -ghost_move_range, ghost_move_range*30], [-ghost_move_range, 0, ghost_move_range*14], [0, ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*38], [0, -ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*18]]
				self.ghost_sprites.add(player)
		return self.hero_sprites, self.ghost_sprites


	# EASY version setupFood
	def setupFood(self, food_color, bg_color, width, height):
		self.food_sprites = pygame.sprite.Group()
		# EASY : 가로 18개, 세로 9개 아이템 생성
		# --> ROW = 9, COL = 18
		for row in range(9):
			for col in range(18):
				if (row == 3 or row == 4) and (col ==6 or col == 7 or col == 8 or col == 9 or col == 10 or col ==11 or col==12):
					continue
				else:
					if ((row == 1 or row == 8) and (col == 0 or col == 18)) or ((row == 2 or row == 5) and (col == 0 or col == 3 or col == 15)):
						# 큰 아이템 객체 생성
						food = Food(width/19*col+width/19, height/10*row+height/10, width/30, width/30, food_color, bg_color)
					else:
						# 작은 아이템 객체 생성
						food = Food(width/19*col+width/19, height/10*row+height/10, width/50, width/50, food_color, bg_color)
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
	def setupWalls(self, wall_color,width,height):
		self.wall_sprites = pygame.sprite.Group()
		wall_positions = [[0, 0, width/70, height], # 외벽
						  [0, 0, width, width/70],
						  [0, height-width/70, width, width/70],
						  [width-width/70, 0, width/70, height],
						  [width*7/20, height*8/19-width/70, width*2/19, width/70], # ghost zone start 가로
						  [width*7/20, height*8/19-width/70, width/70, height*2/19+width/70], #세로
						  [width*7/20, height*10/19-width/70, width*6/19-width/70, width/70], # 가로
						  [width*11/20, height*8/19-width/70, width*2/19, width/70], #가로
						  [width*13/20, height*8/19-width/70, width/70, height*2/19+width/70], # ghost zone fin 세로
						  [width*8/20, 0, width/70, height*2/19+width/70], # 맨 위 왼쪽 |
						  [width*12/20, 0, width/70, height*2/19+width/70], # 맨 위 오른쪽 |
						  [width*2/20, height*2/19, width*4/19, width/70], [width*2/20, height*2/19, width/70, height/19+width/70], # 맨 위 왼쪽 ㄱ자 좌우반전한것
						  [width*14/20, height*2/19, width*4/19, width/70], [width*18/20, height*2/19, width/70, height/19+width/70], # 맨 위 오른쪽 ㄱ자 좌우반전한것
						  [width*10/20, height*2/19, width/70, height*2/19+width/70], # 맨 위 두번째 가운데 |
						  [width*6/20, height*4/19, width*2/19, width/70], # 맨 위 두번째 왼쪽  -
						  [width*12/20, height*4/19, width*2/19, width/70],  # 맨 위 두번째 오른쪽  -
						  [0, height*5/19-width/70, width*2/19, width/70], # 맨 왼쪽 외벽쪽 -
						  [width*18/20, height*5/19-width/70, width*2/19-width/70, width/70], # 맨 오른쪽 외벽쪽 -
						  [width*4/20, height*4/19-width/70, width/70, height*2/19+width/70], [width*4/20, height*6/19-width/70, width/19+width/70, width/70], # 맨 위 왼쪽 L자
						  [width*16/20, height*4/19-width/70, width/70, height*2/19+width/70], [width*15/20, height*6/19-width/70, width/19, width/70], # 맨 위 오른쪽 L자 좌우반전
						  [width*7/20, height*6/19-width/70, width*6/19, width/70], # ghost zone 위 가운데 -----
						  [width*2/20, height*7/19-width/70, width/70, height/19+width/70], [width*2/20, height*8/19-width/70, width/19+width/70, width/70], # ghost zone 왼쪽 조그만 ㄴ자
						  [width*18/20, height*7/19-width/70, width/70, height/19+width/70], [width*17/20, height*8/19-width/70, width/19, width/70], # ghost zone 오른쪽 조그만 ㄴ자
						  [width*5/20, height*8/19-width/70, width/70, height*2/19+width/70], [width*4/20, height*10/19-width/70, height/19, width/70], # ghost zone 바로 왼쪽 L자 좌우반전
						  [width*15/20, height*8/19-width/70, width/70, height*2/19+width/70], [width*15/20, height*10/19-width/70, height/19+width/70, width/70], # ghost zone 바로 오른쪽 L자 좌우반전
						  [width*2/20, height*10/19-width/70, width/70, height*2/19], [width*2/20, height*12/19-width*2/70, width/19+width/70, width/70], # L자
						  [width*18/20, height*10/19-width/70, width/70, height*2/19], [width*17/20, height*12/19-width*2/70, width/19, width/70], # L자 좌우반전
						  [width*5/20, height*12/19-width*2/70, width/70, height*2/19+width/70], [width*5/20, height*12/19-width*2/70, width*3/19, width/70], # ㅗ자 감싸는 wall 왼쪽
						  [width*15/20, height*12/19-width*2/70, width/70, height*2/19+width/70], [width*12/20, height*12/19-width*2/70, width*3/19, width/70], # ㅗ자 감싸는 wall 오른쪽
						  [width*10/20, height*12/19-width*2/70, width/70, height*2/19+width/70], [width*7/20, height*14/19-width*2/70, width*6/19, width/70], # 밑에서 두번째 ㅗ자
						  [width*10/20, height*16/19-width*3/70, width/70, height*2/19+width/70], [width*7/20, height*18/19-width*3/70, width*6/19, width/70], # 맨 밑 ㅗ 자
						  [0, height*14/19-width*2/70, width/19+width/70, width/70], # 맨 왼쪽 외벽쪽 -
						  [width*19/20, height*14/19-width*2/70, width/19, width/70], # 맨 오른쪽 외벽쪽 -
						  [width*3/20, height*14/19-width*2/70, width/70, height*2/19], [width*2/20, height*16/19-width*3/70, width/19, width/70], # L자
						  [width*17/20, height*14/19-width*2/70, width/70, height*2/19], [width*17/20, height*16/19-width*3/70, width/19+width/70, width/70], # L자 좌우반전
						  [width*2/20, height*18/19-width*3/70, width/19+width/70, width/70], # 맨 아래 왼쪽  -
						  [width*17/20, height*18/19-width*3/70, width/19+width/70, width/70], # 맨 아래 오른쪽  -
						  [width*5/20, height*16/19-width*3/70, width/70, height*4/19+width/70], [width*5/20, height*16/19-width*3/70, width*3/19, width/70], # ㅗ자 감싸는 wall 왼쪽
						  [width*15/20, height*16/19-width*3/70, width/70, height*4/19+width/70], [width*12/20, height*16/19-width*3/70, width*3/19, width/70], # 맨 아래 ㅗ자 감싸는 박스 오른쪽
						  ]

		for wall_position in wall_positions:
			wall = Wall(*wall_position, wall_color)
			self.wall_sprites.add(wall)
		return self.wall_sprites

	# HARD version ghost zone 문 만들기
	def setupGate(self, gate_color, width, height):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(width*9/20+2, height*8/19-width/70, width*2/20, 2, gate_color))
		return self.gate_sprites

	# HARD version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path,width,height):
		self.hero_sprites = pygame.sprite.Group()
		self.ghost_sprites = pygame.sprite.Group()
		self.hero_sprites.add(Player(width/2, height*14/19, hero_image_path))
		for each in ghost_images_path:
			role_name = each.split('/')[-1].split('.')[0]
			if role_name == 'Blinky':
				player = Player(285, 259, each)
				player.is_move = True
				player.tracks = [[0, -ghost_move_range, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*18], [0, ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*10], [-ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*6],
								 [ghost_move_range, 0, ghost_move_range*30], [0, -ghost_move_range, ghost_move_range*30], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [-ghost_move_range, 0, ghost_move_range*6],
								 [0, -ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*10], [0, -ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*30], [-ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*6],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*10], [-ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*10], [-ghost_move_range, 0, ghost_move_range*22], [0, -ghost_move_range, ghost_move_range*10], [ghost_move_range, 0, ghost_move_range*10]]

				self.ghost_sprites.add(player)
			elif role_name == 'Clyde':
				player = Player(319, 259, each)
				player.is_move = True
				player.tracks = [[-ghost_move_range*2, 0, ghost_move_range*4], [0, -ghost_move_range, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*10], [0, ghost_move_range, ghost_move_range*10], [-ghost_move_range, 0, ghost_move_range*22], [0, -ghost_move_range, ghost_move_range*10],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*10], [-ghost_move_range, 0, ghost_move_range*10], [0, ghost_move_range, ghost_move_range*30], [ghost_move_range, 0, ghost_move_range*30], [0, -ghost_move_range, ghost_move_range*6],
								 [-ghost_move_range, 0, ghost_move_range*22], [0, -ghost_move_range, ghost_move_range*10], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*18]]
				self.ghost_sprites.add(player)
			elif role_name == 'Inky':
				player = Player(255, 259, each)
				player.is_move = True
				player.tracks = [[ghost_move_range*2, 0, ghost_move_range*4], [0, -ghost_move_range, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*20], [0, ghost_move_range, ghost_move_range*10], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*6],
								 [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*30], [-ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*22],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*10], [-ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*10],
								 [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*30], [ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*6],
								 [-ghost_move_range, 0, ghost_move_range*30], [0, ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*6], [0, -ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*22], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, 1]]
				self.ghost_sprites.add(player)
			elif role_name == 'Pinky':
				player = Player(349, 259, each)
				player.is_move = True
				player.tracks = [[0, -ghost_move_range*2, ghost_move_range*8], [ghost_move_range, 0, ghost_move_range*18], [0, ghost_move_range, ghost_move_range*22], [-ghost_move_range, 0, ghost_move_range*46], [0, ghost_move_range, ghost_move_range*10], [ghost_move_range, 0, ghost_move_range*6],
								 [0, -ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*38], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*6], [0, ghost_move_range, ghost_move_range*6], [ghost_move_range, 0, ghost_move_range*6],
								 [0, -ghost_move_range, ghost_move_range*30], [-ghost_move_range, 0, ghost_move_range*10], [0, ghost_move_range, ghost_move_range*6], [-ghost_move_range, 0, ghost_move_range*38], [0, -ghost_move_range, ghost_move_range*22], [ghost_move_range, 0, ghost_move_range*18]]
				self.ghost_sprites.add(player)
		return self.hero_sprites, self.ghost_sprites


	# HARD version setupFood
	def setupFood(self, food_color, bg_color, width, height):
		self.food_sprites = pygame.sprite.Group()
		# HARD : 가로 19개, 세로 19개 아이템 생성
		# --> ROW = 19, COL = 19
		for row in range(19):
			for col in range(19):
				if (row == 7 or row == 8) and (col == 7 or col == 8 or col == 9 or col == 10 or col == 11):
					continue
				else:
					if ((row == 1 or row == 14) and (col == 0 or col == 18)) or ((row == 2 or row == 10) and (col == 0 or col == 3 or col == 10)):
						# 큰 아이템 객체 생성
						food = Food(width/20*col+width/19, height/20*row+height/19, width/40, width/40, food_color, bg_color)
					else:
						# 작은 아이템 객체 생성
						food = Food(width/20*col+width/19, height/20*row+height/19, width/80, width/80, food_color, bg_color)
				is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
				if is_collide:
					continue
				is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
				if is_collide:
					continue
				self.food_sprites.add(food)
		return self.food_sprites
