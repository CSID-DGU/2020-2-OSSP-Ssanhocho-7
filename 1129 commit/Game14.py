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


from PIL import Image
i = Image.open('resources/images/map_easy.png')

width, height = i.size

HEIGHT = height + 30
WIDTH = width + 30

img = pygame.image.load('resources/images/pacman.png')

sFont = pygame.font.Font('resources/font/Firenight-Regular.OTF', 50)

music_on = True

def music_pause():
	if event.key == pygame.K_m:
		if music_on:
			pygame.mixer.music.pause()
			music_on = False
		else:
			pygame.mixer.music.unpause()
			music_on = True




'''开始某一关游戏(특정레벨시 )'''
def startLevelGame(level, screen, font):
	global music_on
	clock = pygame.time.Clock()
	SCORE = 0
	wall_sprites = level.setupMap() # 원래 setupWalls(SKYBLUE)
	gate_sprites = level.setupGate(RED)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites = level.setupFood(YELLOW, WHITE) # 원래 setupFood(YELLOW, WHITE)
	is_clearance = False


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_h:
					level.NUMLEVELS=2
					main1(initialize())
				if event.key == pygame.K_e:
					level.NUMLEVELS=1
					main(initialize())
				if event.key == pygame.K_s:
					ff=True
					while ff:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit(-1)
								pygame.quit()
							'''elif event.type == VIDEORESIZE:
								screen = pygame.display.set_mode(event.dict["size"], HWSURFACE | DOUBLEBUF | RESIZABLE)
								screen.blit(pygame.transform.scale(map, event.dict["size"]), (0, 0))
								pygame.display.flip()'''
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

							#if event.type == pygame.KEYUP:
								#if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
									#hero.is_move != ff
						screen.fill(BLACK)

						for hero in hero_sprites:
							hero.update(wall_sprites, gate_sprites)
						hero_sprites.draw(screen)
						for hero in hero_sprites:
							food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
						SCORE += len(food_eaten)
						wall_sprites.draw(screen)
						#gate_sprites.draw(screen)
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
							ghost.update(wall_sprites, None)
						ghost_sprites.draw(screen)
						score_text = font.render("Score: %s" % SCORE, True, RED)
						screen.blit(score_text, [10, 10])
						'''if len(food_sprites) == 0:
							is_clearance = False #True
							break'''
						if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
							is_clearance = False
							break
						pygame.display.flip()
						clock.tick(10)


					return is_clearance




'''显示文字텍스트 이름?'''
def showText(screen, font, is_clearance, flag=False):
	clock = pygame.time.Clock()
	msg = 'Game Over!' if not is_clearance else 'Congratulations, you won!'
	positions = [[235, 233], [65, 303], [170, 333]] if not is_clearance else [[145, 233], [65, 303], [170, 333]]
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
							main1(initialize())
					else:
						main1(initialize())
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
def initialize():
	pygame.init()
	icon_image = pygame.image.load(ICONPATH)
	pygame.display.set_icon(icon_image)
	screen = pygame.display.set_mode([WIDTH, HEIGHT], RESIZABLE)
	pygame.display.set_caption('Pacman-微信公众号Charles的皮卡丘')
	return screen


'''主函数(주요기)'''
def main(screen):
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
		main(initialize())
