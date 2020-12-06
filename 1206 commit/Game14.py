import os
import sys
import pygame
import Levels
from pygame.locals import *

pygame.init()

'''주요 매개변수'''
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
FONTPATH = os.path.join(os.getcwd(), 'resources/font/Firenight-Regular.OTF')
HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), 'resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), 'resources/images/Pinky.png')

NUMLEVELS = 0

# 초기화면 크기 = 606, 606
WIDTH = 606
HEIGHT = 606
WIDTH_e = 577
HEIGHT_e = 306
ratio_e = 577 / 306
WIDTH_h = 606
HEIGHT_h = 606
ratio_h = 1

SCORE = 0

sFont = pygame.font.Font('resources/font/Firenight-Regular.OTF', 50)

music_on = True


'''开始某一关游戏(특정레벨시 )'''
def startLevelGame(level, screen, font):
	global music_on
	global WIDTH_h, WIDTH_e, HEIGHT_e, HEIGHT_h
	global NUMLEVELS, SCORE
	clock = pygame.time.Clock()
	wall_sprites = level.setupWalls(SKYBLUE)
	gate_sprites = level.setupGate(RED)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites = level.setupFood(YELLOW, WHITE)
	is_clearance = False


	while True:
		for event in pygame.event.get():
			if event.type == pygame.VIDEOEXPOSE:
				pygame.display.update((0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]))
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
					if music_on:
						pygame.mixer.music.pause()
						music_on = False
					else:
						pygame.mixer.music.unpause()
						music_on = True
				if event.key == pygame.K_h:
					#level.NUMLEVELS=2
					NUMLEVELS = 2
					main1(initialize(NUMLEVELS))
				if event.key == pygame.K_e:
					#level.NUMLEVELS = 1
					NUMLEVELS = 1
					main(initialize(NUMLEVELS))
					window_width, window_height = pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]
					print(window_width, window_height)
					print(WIDTH_e, HEIGHT_e)
				if event.key == pygame.K_s:
					ff = True
					while ff:
						for event in pygame.event.get():
							if event.type == pygame.VIDEORESIZE:
								#pygame.display.update((0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]))
								screen = pygame.display.set_mode(event.dict["size"], RESIZABLE)
								#window_width, window_height = pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]
								window_width, window_height = event.dict["size"]
								print(window_width, window_height)
								#print(WIDTH_e, HEIGHT_e)
								print(window_width - WIDTH_e)
								'''for food in food_sprites:
									#food.width = food.width + 1#3*(window_width / WIDTH_e)
									#food.height = food.height + 1#3*(window_height / HEIGHT_e)
									#food.image = pygame.transform.scale(food.image, (food.width * int(window_width / WIDTH_e), food.height * int(window_height / HEIGHT_e)))
									screen.blit(pygame.transform.scale(food.image, event.dict['size']), (0, 0))
									pygame.display.update()'''
								for hero in hero_sprites:
									hero.image = pygame.transform.scale(hero.base_image, (hero.width * int(window_width / WIDTH_e), hero.width * int(window_height / HEIGHT_e)))
									hero.base_image = hero.image
									pygame.display.update()
								for ghost in ghost_sprites:
									ghost.image = pygame.transform.scale(ghost.base_image, (ghost.width * int(window_width / WIDTH_e), ghost.width * int(window_height / HEIGHT_e)))
									ghost.base_image = ghost.image
									pygame.display.update()
								for wall in wall_sprites:
									#wall.kill()
									if wall.width == 6:
										wall.height = wall.height + (window_height - HEIGHT_e)
										if wall.rect.top == 0 or wall.rect.left == 0: continue
										else:
											wall.height = wall.height + 30#(window_height - HEIGHT_e)
											wall.rect.top = wall.rect.top + (window_height - HEIGHT_e)
											wall.rect.left = wall.rect.left + (window_width - WIDTH_e)

									elif wall.height == 6:
										wall.width = wall.width + (window_width - WIDTH_e)
										if wall.rect.top == 0 or wall.rect.left == 0: continue
											#wall.rect.width = window_width
											#wall.rect.height = window_height
										else:
											wall.rect.top = wall.rect.top + (window_height - HEIGHT_e)
											wall.rect.left = wall.rect.left + (window_width - WIDTH_e)
									wall_sprites.add(wall)
									pygame.display.update()
							if event.type == pygame.QUIT:
								sys.exit(-1)
								pygame.quit()

							# 음악 일시정지
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_m:
									if music_on:
										pygame.mixer.music.pause()
										music_on = False
									else:
										pygame.mixer.music.unpause()
										music_on = True
							# 방향키
								if event.key == pygame.K_LEFT:
									for hero in hero_sprites:
										hero.changeSpeed([-1, 0])
										hero.is_move = ff
								elif event.key == pygame.K_RIGHT:
									for hero in hero_sprites:
										hero.changeSpeed([1, 0])
										hero.is_move = ff
								elif event.key == pygame.K_UP:
									for hero in hero_sprites:
										hero.changeSpeed([0, -1])
										hero.is_move = ff
								elif event.key == pygame.K_DOWN:
									for hero in hero_sprites:
										hero.changeSpeed([0, 1])
										hero.is_move = ff
								elif event.type == pygame.QUIT:
									sys.exit()
									pygame.quit()
						screen.fill(BLACK)

						for hero in hero_sprites:
							hero.update(wall_sprites, None)
						hero_sprites.draw(screen)
						for hero in hero_sprites:
							food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
						for food in food_eaten:
							if food.width == 10:
								SCORE += 50
							else:
								SCORE += 10
						#SCORE += 10 * len(food_eaten)
						wall_sprites.draw(screen)
						gate_sprites.draw(screen)
						food_sprites.draw(screen)
						for ghost in ghost_sprites:
							# 指定幽灵运动路径(유령 경로이 )
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
							ghost.update(wall_sprites, gate_sprites)
						ghost_sprites.draw(screen)
						score_text = font.render("Score: %s" % SCORE, True, RED)
						screen.blit(score_text, [10, 10])
						if len(food_sprites) == 0:
							#is_clearance = True
							main1(initialize(NUMLEVELS))
							continue
							#break
						if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
							is_clearance = False
							SCORE = 0
							break
						pygame.display.flip()
						clock.tick(10)
					return is_clearance




'''显示文字텍스트 이름?'''
def showText(screen, font, is_clearance, flag=False):
	clock = pygame.time.Clock()
	if not is_clearance: msg = 'Game Over!'
	# msg = 'Game Over!' if not is_clearance else 'Congratulations, you won!'
	positions = [[235, 233], [65, 303], [170, 333]] #if not is_clearance #else [[145, 233], [65, 303], [170, 333]]
	surface = pygame.Surface((400, 200))
	surface.set_alpha(10)#투명
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
							main1(initialize(NUMLEVELS))
					else:
						main1(initialize(NUMLEVELS))
				elif event.key == pygame.K_ESCAPE:
					sys.exit()
					pygame.quit()

				elif event.key == pygame.K_a:
					sys.exit()
					pygame.quit()



		for idx, (text, position) in enumerate(zip(texts, positions)):
			screen.blit(text, position)
		pygame.display.flip()
		clock.tick(10)


'''初始化(초기)'''
def initialize(numlevels):
	global WIDTH_h, WIDTH_e, HEIGHT_e, HEIGHT_h
	print("def initialize임")
	pygame.init()
	icon_image = pygame.image.load(ICONPATH)
	pygame.display.set_icon(icon_image)
	if numlevels == 1:
		screen = pygame.display.set_mode([WIDTH_e, HEIGHT_e], pygame.RESIZABLE)
	elif numlevels == 2:
		screen = pygame.display.set_mode([WIDTH_h, HEIGHT_h], pygame.RESIZABLE)
	else:
		screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
	pygame.display.set_caption('Pacman-微信公众号Charles的皮卡丘')
	prev_size = screen.get_size()
	print(prev_size)
	return screen


'''主函数(주요기)'''
def main(screen):
	print("def main임")
	pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)
	pygame.font.init()
	Levels.MODE='EASY'
	font_small = pygame.font.Font(FONTPATH, 18)
	font_big = pygame.font.Font(FONTPATH, 24)
	#for num_level in range(1, Levels.NUMLEVELS+1):
	if Levels.MODE=='EASY':
		level = Levels.Level1()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.MODE=='EASY':
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)


def main1(screen):
	pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)
	pygame.font.init()
	Levels.MODE='HARD'
	font_small = pygame.font.Font(FONTPATH, 18)
	font_big = pygame.font.Font(FONTPATH, 24)

	if Levels.MODE== 'HARD':
		level = Levels.Level2()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.MODE== 'HARD':
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)

'''test'''

if __name__ == '__main__':
		main(initialize(NUMLEVELS))
		# initialize 한 다음에 main 수행
