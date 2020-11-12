'''
Function:
	吃豆豆小游戏
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import os
import sys
import pygame
import Levels


'''定义一些必要的参数'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
SKYBLUE = (0, 191, 255)
BGMPATH = os.path.join(os.getcwd(), 'resources/sounds/bg.mp3')
ICONPATH = os.path.join(os.getcwd(), 'resources/images/icon.png')
FONTPATH = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')
HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), 'resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), 'resources/images/Pinky.png')

pacman_orig = pygame.image.load('resources/images/pacman.png')

# pacman
pacman_right = pygame.transform.rotate(pacman_orig, 0)
pacman_left = pygame.transform.rotate(pacman_orig, 180)
pacman_up = pygame.transform.rotate(pacman_orig, 90)
pacman_down = pygame.transform.rotate(pacman_orig, 270)
obj_x = 287
obj_y = 439

# Pacman movement
MOVE_UP = 1
MOVE_DOWN = 2
MOVE_RIGHT = 3
MOVE_LEFT = 4
next_move = 0
change_x = 0
change_y = 0


'''开始某一关游戏'''
def startLevelGame(level, screen, font):
	# Pacman movement
	MOVE_UP = 1
	MOVE_DOWN = 2
	MOVE_RIGHT = 3
	MOVE_LEFT = 4
	next_move = 0
	change_x = 0
	change_y = 0

	clock = pygame.time.Clock()
	SCORE = 0
	wall_sprites = level.setupWalls(SKYBLUE)
	gate_sprites = level.setupGate(WHITE)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites = level.setupFood(YELLOW, WHITE)
	is_clearance = False
	#for hero in hero_sprites:
		#pacman_right = hero.changeSpeed([1,0])
		#pacman_left = hero.changeSpeed([-1,0])
		#pacman_up = hero.changeSpeed([0,-1])
		#pacman_down = hero.changeSpeed([0,1])
	obj_x = 287
	obj_y = 439

	KeepGoing = True
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					for hero in hero_sprites:
						hero.changeSpeed([-1, 0])
						hero.is_move = True
						change_x=-1
						change_y=0
						print(change_x,change_y)
						#change_x = -1
						#change_y = 0
						#next_move = 0
					#if pygame.sprite.spritecollide(hero, wall_sprites, False):
						#next_move = MOVE_LEFT
					#for hero in hero_sprites:
						#hero.changeSpeed([-1,0])
						#hero.is_move = True
				elif event.key == pygame.K_RIGHT:
					for hero in hero_sprites:
						hero.changeSpeed([1, 0])
						hero.is_move = True
						change_x=1
						change_y=0
						print(change_x,change_y)
				elif event.key == pygame.K_UP:
					for hero in hero_sprites:
						hero.changeSpeed([0, -1])
						hero.is_move = True
						change_x=0
						change_y=-1
						print(change_x,change_y)
				elif event.key == pygame.K_DOWN:
					for hero in hero_sprites:
						hero.changeSpeed([0, 1])
						hero.is_move = True
						change_x=0
						change_y=1
						print(change_x,change_y)
			#if event.type == pygame.KEYUP:
				#if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
					#hero.is_move = False
					#KeepGoing = False
				#if event.key == pygame.K_LEFT:
					#for hero in hero_sprites:
						#hero.changeSpeed([-1
						#hero.is_move = True
		#if next_move > 0:
			#if next_move == MOVE_UP and MAZE_ARR[obj_y-1][obj_x] != '#':
				#change_x = 0
				#change_y = -1
			#if next_move == MOVE_DOWN and obj_x-1 != level.setupWalls.wall_positions() and (obj_y) != level.setupWalls(SKYBLUE):
				#change_x = 0
				#change_y = 1
			#if next_move == MOVE_LEFT and obj_x-1 != level.setupWalls.wall_positions() and (obj_y) != level.setupWalls(SKYBLUE):
				#change_x = -1
				#change_y = 0
			#elif next_move == MOVE_RIGHT and MAZE_ARR[obj_y][obj_x+1] != '#':
				#change_x = 1
				#change_y = 0
		#if MAZE_ARR[obj_y+change_y][obj_x+change_x] == '#':
			#change_x = 0
			#change_y = 0
		#elif MAZE_ARR[obj_y+change_y][obj_x+change_x] == '@':
		   # MAZE_ARR[obj_y+change_y][obj_x+change_x] = ' '
		   # score += 1
		   # if score == target_score:
		     #   keepGoing = False
		if change_x == 1 and change_y==0: #right
			for hero in hero_sprites:
				hero.changeSpeed([1,0])
		elif change_x == -1 and change_y==0: #left
			for hero in hero_sprites:
				hero.changeSpeed([-1,0])
		elif change_x==0 and change_y == -1: #up
			for hero in hero_sprites:
				hero.changeSpeed([0,-1])
		elif change_x==0 and change_y == 1: #down
			for hero in hero_sprites:
				hero.changeSpeed([0,1])
		obj_x += change_x
		obj_y += change_y
		print(obj_x,obj_y)

		screen.fill(BLACK)
		for hero in hero_sprites:
			hero.update(wall_sprites, gate_sprites)
		hero_sprites.draw(screen)
		for hero in hero_sprites:
			food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
		SCORE += len(food_eaten)
		wall_sprites.draw(screen)
		gate_sprites.draw(screen)
		food_sprites.draw(screen)
		for ghost in ghost_sprites:
			# 幽灵随机运动(效果不好且有BUG)
			'''
			res = ghost.update(wall_sprites, None)
			while not res:
				ghost.changeSpeed(ghost.randomDirection())
				res = ghost.update(wall_sprites, None)
			'''
			# 指定幽灵运动路径
			if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
				ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
				ghost.tracks_loc[1] += 1
			else:
				if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
					ghost.tracks_loc[0] += 1
				elif ghost.role_name == 'Clyde':
					ghost.tracks_loc[0] = 2
				else:
					ghost.tracks_loc[0] = 0
				ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
				ghost.tracks_loc[1] = 0
			if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
				ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
			else:
				if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
					loc0 = ghost.tracks_loc[0] + 1
				elif ghost.role_name == 'Clyde':
					loc0 = 2
				else:
					loc0 = 0
				ghost.changeSpeed(ghost.tracks[loc0][0: 2])
			ghost.update(wall_sprites, None)
		ghost_sprites.draw(screen)
		score_text = font.render("Score: %s" % SCORE, True, RED)
		screen.blit(score_text, [10, 10])
		if len(food_sprites) == 0:
			is_clearance = True
			break
		if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
			is_clearance = False
			break
		pygame.display.flip()
		clock.tick(10)
	return is_clearance


'''显示文字'''
def showText(screen, font, is_clearance, flag=False):
	clock = pygame.time.Clock()
	msg = 'Game Over!' if not is_clearance else 'Congratulations, you won!'
	positions = [[235, 233], [65, 303], [170, 333]] if not is_clearance else [[145, 233], [65, 303], [170, 333]]
	surface = pygame.Surface((400, 200))
	surface.set_alpha(10)
	surface.fill((128, 128, 128))
	screen.blit(surface, (100, 200))
	texts = [font.render(msg, True, WHITE),
			 font.render('Press ENTER to continue or play again.', True, WHITE),
			 font.render('Press ESCAPE to quit.', True, WHITE)]
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if is_clearance:
						if not flag:
							return
						else:
							main(initialize())
					else:
						main(initialize())
				elif event.key == pygame.K_ESCAPE:
					sys.exit()
					pygame.quit()
		for idx, (text, position) in enumerate(zip(texts, positions)):
			screen.blit(text, position)
		pygame.display.flip()
		clock.tick(10)


'''初始化'''
def initialize():
	pygame.init()
	icon_image = pygame.image.load(ICONPATH)
	pygame.display.set_icon(icon_image)
	screen = pygame.display.set_mode([606, 606])
	pygame.display.set_caption('Pacman-微信公众号Charles的皮卡丘')
	return screen


'''主函数'''
def main(screen):
	pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)
	pygame.font.init()
	font_small = pygame.font.Font(FONTPATH, 18)
	font_big = pygame.font.Font(FONTPATH, 24)
	for num_level in range(1, Levels.NUMLEVELS+1):
		if num_level == 1:
			level = Levels.Level1()
			is_clearance = startLevelGame(level, screen, font_small)
			if num_level == Levels.NUMLEVELS:
				showText(screen, font_big, is_clearance, True)
			else:
				showText(screen, font_big, is_clearance)


'''test'''
if __name__ == '__main__':
	main(initialize())
