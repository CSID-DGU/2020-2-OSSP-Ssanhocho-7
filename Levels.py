import pygame
from Sprites import *
import random
import Game14
<<<<<<< .merge_file_a08528

MODE= 'randomMode'


'''
setupWalls 원리
- width/70 : 벽의 두께 (+- width/70 : 위치 조절하려고 두께만큼 더하거나 뺌)
- 원래 맵 사진에서 벽 위치의 비율에 따라 적절한 수를 곱함
- [x, y, width, height]

setupGate, setupFood
- 화면에 표시되는 Gate와 Food의 비율을 계산하여 적절한 비율을 곱함
'''
=======
MODE='randomMode'
wall_width=Game14.screen_size[0]/65
map_height=Game14.screen_size[1]
[0, 0, 6, 306]

'''가로 576
6=wall_width1
세로306
150은 width*0.25
66은 height*0.12
210은 가로/2.9
154는 width/3.8
60은 0.1width
36은 width/14
480dms width*0.83
510dms width*0.9'''

>>>>>>> .merge_file_a11456

# 좌표개 x축이랑 거리 y축이랑 거리

class Level1():
	MODE='EASY'
	def __init__(self):
		self.info = 'level1'
	'''벽 만들기'''
	def setupWalls(self, wall_color,width,height):
		self.wall_sprites = pygame.sprite.Group()
		wall_positions = [[0, 0, width/70, height], # 맨 왼쪽
<<<<<<< .merge_file_a08528
	                    [0, 0, width, width/70], # 맨 위쪽
	                    [0, height-width/70, width, width/70], # 맨 아래쪽
	                    [width-width/70, 0, width/6, height], # 맨 오른쪽
	                    [width/4+width/70, 0, width/70, height/5+width/70], # 맨 위 왼쪽 |
	                    [width*3/4, 0, width/70, height/5+width/70], # 맨 위 오른쪽 |체크
	                    [width/3 + width/20, height/5, width/4, width/70], # ghost zone 위 가운데 -----
	                    [width*2/19, height/5, width/18+width/70, width/70], [width*2/19, height/5, width/70, height*2/9], # 맨 위 왼쪽 ㄱ자 좌우반전한것
	                    [width*16/19, height/5, width/18+width/70, width/70], [width*17/19+4, height/5, width/70, height*2/9], # 맨 위 오른쪽 ㄱ자 좌우반전한것
	                    [width*4/19, height*2/5+width/70, width/18+width/70, width/70], [width*3/4, height*2/5+width/70, width/18+width/70, width/70], [width*4/19, height*3/5+5, width/18+width/70, width/70], [width*3/4, height*3/5+5, width/18+width/70, width/70], # 조그마한 - 4개
	                    [width*2/19, height*4/5+5, width/18+width/70, width/70], [width*2/19, height*3/5, width/70, height*2/9], # 아래 왼쪽 L자
	                    [width*16/19, height*4/5+5, width/18+width/70, width/70], [width*17/19+4, height*3/5, width/70, height*2/9], # 아래 오른쪽 L자 좌우반전한것
	                    [width/4+width/70, height*4/5-width/70 , width/70, height/5+width/70], # 맨 아래 왼쪽 |
	                    [width*3/4, height*4/5-width/70, width/70, height/5+width/70], # 맨 아래 오른쪽 |
	                    [width/3 + width/20, height*4/5+width/70, width/4, width/70], # ghost zone 아래 가운데 -----
	                    [width/3 + width/20, height*2/5, width/18+width/70, width/70], # ghost zone start 가로
	                    [width/3 + width/20, height*2/5, width/70, height*2/9], #세로
	                    [width/3 + width/20, height*3/5+5, width/4, width/70], #가로
	                    [width*11/19-5, height*2/5, width/18+width/70, width/70], #가로
	                    [width*12/19, height*2/5+5, width/70, height/5+width/70], # ghost zone fin 세로
	                    ]
=======
						  [0, 0, width, width/70], # 맨 위쪽
						  [0, height-width/70, width, width/65], # 맨 아래쪽
						  [width-width/70, 0, width/6, height], # 맨 오른쪽
						  [width*0.25, 0, width/70, height*0.12], # 맨 위 왼쪽 |
						  [width-width*0.25, 0, width/70, height*0.12], # 맨 위 오른쪽 |체크
						  [width/2.9, height*0.12-width/70, width/3.8, width/70], # ghost zone 위 가운데 -----
						  [width*0.1, width*0.1, width/14, width/70], [width*0.1, width*0.1, width/70, height*0.12], # 맨 위 왼쪽 ㄱ자 좌우반전한것
						  [width*0.83, width*0.1, width/14, width/70], [width*0.9, width*0.1, width/70, height*0.12], # 맨 위 오른쪽 ㄱ자 좌우반전한것
						  [width*0.2, width*0.2, width/14, width/70], [width/1.45, width*0.2, width/14, width/70], [width*0.2, width*0.3, width/14, width/70], [width/1.45, width*0.3, width/14, width/70], # 조그마한 - 4개
						  [width*0.1, width*0.415, width/14, width/70], [width*0.1, width*0.3, width/70, height*0.12], # 아래 왼쪽 L자
						  [width*0.83, width*0.415, width/14, width/70], [width*0.9, width*0.3, width/70, height*0.13], # 아래 오른쪽 L자 좌우반전한것
						  [width*0.25, width*0.415, width/70, height*0.12], # 맨 아래 왼쪽 |
						  [420, 240, 6, 66], # 맨 아래 오른쪽 |
						  [210, 240, 154, 6], # ghost zone 아래 가운데 -----
						  [210, 120, 36, 6], # ghost zone start
						  [210, 120, 6, 66],
						  [210, 180, 154, 6],
						  [330, 120, 36, 6],
						  [360, 120, 6, 66], # ghost zone fin
						  ]
>>>>>>> .merge_file_a11456
		for wall_position in wall_positions:
			wall = Wall(*wall_position, wall_color)
			self.wall_sprites.add(wall)
		return self.wall_sprites

	# EASY version ghost zone 문 만들기
<<<<<<< .merge_file_a08528
	def setupGate(self, gate_color, width, height):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(width/3 + width*2/18, height*2/5, width*2/18+width/70, 2, gate_color))
		return self.gate_sprites

	# EASY version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path,width,height):
		self.hero_sprites = pygame.sprite.Group()
		self.ghost_sprites = pygame.sprite.Group()
		self.hero_sprites.add(Player(width/2, height*6/9, hero_image_path)) #439
		for each in ghost_images_path:
			# 유령 이동경로 setup
=======
	def setupGate(self, gate_color):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(246, 122, 84, 2, gate_color))
		return self.gate_sprites

	# EASY version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path):
		self.hero_sprites = pygame.sprite.Group()
		self.ghost_sprites = pygame.sprite.Group()
		self.hero_sprites.add(Player(287, 200, hero_image_path)) #439
		for each in ghost_images_path:
>>>>>>> .merge_file_a11456
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

<<<<<<< .merge_file_a08528

	# EASY version setupFood
	def setupFood(self, food_color, bg_color, width, height):
		self.food_sprites = pygame.sprite.Group()
		# EASY : 가로 18개, 세로 9개 아이템 생성
		# --> ROW = 9, COL = 18
=======
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
					is_collide = pygame.sprite	.spritecollide(food, self.hero_sprites, False)
					if is_collide:
						continue
					self.food_sprites.add(food)
		return self.food_sprites


	# EASY version setupFood
	def setupFood(self, food_color, bg_color):
		self.food_sprites = pygame.sprite.Group()
>>>>>>> .merge_file_a11456
		for row in range(9):
			for col in range(18):
				if (row == 3 or row == 4) and (col == 7 or col == 8 or col == 9 or col == 10):
					continue
				else:
					if ((row == 1 or row == 8) and (col == 0 or col == 18)) or ((row == 2 or row == 5) and (col == 0 or col == 3 or col == 15)):
<<<<<<< .merge_file_a08528
						food = Food(width/19*col+width/19, height/10*row+height/10, width/30, width/30, food_color, bg_color)
					else:
						food = Food(width/19*col+width/19, height/10*row+height/10, width/50, width/50, food_color, bg_color)
=======
						food = Food(30*col+23, 30*row+23, 20, 20, food_color, bg_color)
					else:
						food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
>>>>>>> .merge_file_a11456
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
<<<<<<< .merge_file_a08528
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
=======
	def setupWalls(self, wall_color):
		self.wall_sprites = pygame.sprite.Group()
		wall_positions = [[0, 0,6, 600], # 외벽
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
>>>>>>> .merge_file_a11456
						  ]

		for wall_position in wall_positions:
			wall = Wall(*wall_position, wall_color)
			self.wall_sprites.add(wall)
		return self.wall_sprites

	# HARD version ghost zone 문 만들기
<<<<<<< .merge_file_a08528
	def setupGate(self, gate_color, width, height):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(width*9/20+2, height*8/19-width/70, width*2/20, 2, gate_color))
		return self.gate_sprites

	# HARD version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path,width,height):
=======
	def setupGate(self, gate_color):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(276, 242, 54, 2, gate_color))
		return self.gate_sprites

	# HARD version 캐릭터 구축
	def setupPlayers(self, hero_image_path, ghost_images_path):
>>>>>>> .merge_file_a11456
		self.hero_sprites = pygame.sprite.Group()
		self.ghost_sprites = pygame.sprite.Group()
		self.hero_sprites.add(Player(287, 439, hero_image_path))
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
			elif role_name == 'Clyde':
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
				self.ghost_sprites.add(player)
		return self.hero_sprites, self.ghost_sprites

<<<<<<< .merge_file_a08528

	# HARD version setupFood
	def setupFood(self, food_color, bg_color, width, height):
=======
	# 아이템 만들기 (동전)
	def setupFood(self, food_color, bg_color):
>>>>>>> .merge_file_a11456
		self.food_sprites = pygame.sprite.Group()
		# HARD : 가로 19개, 세로 19개 아이템 생성
		# --> ROW = 19, COL = 19
		for row in range(19):
			for col in range(19):
				if (row == 7 or row == 8) and (col == 7 or col == 8 or col == 9 or col == 10 or col == 11):
					continue
				else:
<<<<<<< .merge_file_a08528
					if ((row == 1 or row == 14) and (col == 0 or col == 18)) or ((row == 2 or row == 10) and (col == 0 or col == 3 or col == 10)):
						food = Food(width/20*col+width/19, height/20*row+height/19, width/40, width/40, food_color, bg_color)
					else:
						food = Food(width/20*col+width/19, height/20*row+height/19, width/80, width/80, food_color, bg_color)
=======
					food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
					is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
					if is_collide:
						continue
					is_collide = pygame.sprite	.spritecollide(food, self.hero_sprites, False)
					if is_collide:
						continue
					self.food_sprites.add(food)
		return self.food_sprites

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
>>>>>>> .merge_file_a11456
				is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
				if is_collide:
					continue
				is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
				if is_collide:
					continue
				self.food_sprites.add(food)
		return self.food_sprites
