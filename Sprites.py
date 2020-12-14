'''
Function:
	定义一些精灵类
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import random
import pygame
import Fever

width = 606
height = 606

'''墙类'''
class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y


'''食物类'''
class Food(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color, bg_color, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(bg_color)
		self.image.set_colorkey(bg_color)
		pygame.draw.ellipse(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y
		self.width=width
		self.height=height

'''角色类'''
class Player(pygame.sprite.Sprite):

	def __init__(self, x, y,role_image_path):
		pygame.sprite.Sprite.__init__(self)
		self.role_name = role_image_path.split('/')[-1].split('.')[0]
		self.base_image = pygame.image.load(role_image_path).convert_alpha()
		self.small_img = pygame.transform.scale(self.base_image,(int(width/19.55),int(height/19.55)))
		self.fever_img = pygame.image.load('resources/images/fever.png').convert()
		self.g_base= pygame.image.load('resources/images/ghostfever.png').convert()
		self.g_fever_img =pygame.transform.scale(self.g_base,(int(width/19.55),int(height/19.55)))
		self.image = self.small_img.copy()
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y
		self.prev_x = x
		self.prev_y = y
		self.base_speed = [30, 30]
		self.speed = [0, 0]
		self.is_move = True
		self.tracks = []
		self.tracks_loc = [0, 0]
		fever = Fever.Fever()
	'''改变速度方向'''
	def pchangeSpeed(self,isFeverTime,direction):

		#direction[idx] idx =0 -> x idx=1 -> y
		if isFeverTime:
			if direction[0] < 0:
				self.image = pygame.transform.flip(self.fever_img, True, False)
			elif direction[0] > 0:
				self.image = self.fever_img.copy()
			elif direction[1] < 0:
				self.image = pygame.transform.rotate(self.fever_img, 90) #90도 회전
			elif direction[1] > 0:
				self.image = pygame.transform.rotate(self.fever_img, -90)
		else:
			if direction[0] < 0:
				self.image = pygame.transform.flip(self.small_img, True, False)
			elif direction[0] > 0:
				self.image = self.small_img.copy()
			elif direction[1] < 0:
				self.image = pygame.transform.rotate(self.small_img, 90)
			elif direction[1] > 0:
				self.image = pygame.transform.rotate(self.small_img, -90)
		self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
		return self.speed

	def gchangeSpeed(self,isFeverTime,hero_sprites,ghost_sprites,direction):
		fever = Fever.Fever()
		if isFeverTime==True and fever.feverTime(hero_sprites,ghost_sprites):
			if direction[0] < 0:
				self.image = pygame.transform.flip(self.g_fever_img, True, False)
			elif direction[0] > 0:
				self.image = self.g_fever_img.copy()
			elif direction[1] < 0:
				self.image = pygame.transform.rotate(self.g_fever_img, 90)
			elif direction[1] > 0:
				self.image = pygame.transform.rotate(self.g_fever_img, -90)
		else:
			if direction[0] < 0:
				self.image = pygame.transform.flip(self.small_img, True, False)
			elif direction[0] > 0:
				self.image = self.small_img.copy()
			elif direction[1] < 0:
				self.image = pygame.transform.rotate(self.small_img, 90)
			elif direction[1] > 0:
				self.image = pygame.transform.rotate(self.small_img, -90)

		self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
		return self.speed

	def update(self, wall_sprites, gate_sprites):
		if not self.is_move:
			return False
		x_prev = self.rect.left
		y_prev = self.rect.top

		self.rect.left += self.speed[0]
		self.rect.top += self.speed[1]
		is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
		if is_collide:
			self.rect.left = x_prev
			self.rect.top = y_prev
		if gate_sprites is not None:
			if not is_collide:
				is_collide = pygame.sprite.spritecollide(self, gate_sprites, False)

		return True
