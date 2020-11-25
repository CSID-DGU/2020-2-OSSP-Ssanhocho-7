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

pygame.init()

'''定义一些必要的参数(몇가지 주요배개변수 )'''
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
HEIGHT=606
WIDTH=606
img =pygame.image.load('resources/images/pacman.png')

start_image=pygame.image.load('resources/images/starticon.png')
start_image_size=start_image.get_rect().size
start_image_width=start_image_size[0]
start_image_height=start_image_size[1]
start_x_po=(WIDTH/2)-(start_image_width/2)
start_y_po=(HEIGHT/1.5)-(start_image_height/2)

yongFont = pygame.font.Font( None,50)

easytitle=yongFont.render("EASY",True,WHITE)
easy_size=easytitle.get_rect().size
easy_size_width=easy_size[0]
easy_size_height=easy_size[1]
easy_x_po=(WIDTH/3)-(easy_size_width/2)
easy_y_po=(HEIGHT/3)-(easy_size_height/2)

hardtitle=yongFont.render("HARD",True,WHITE)
hard_size=hardtitle.get_rect().size
hard_size_width=hard_size[0]
hard_size_height=hard_size[1]
hard_x_po=(WIDTH/1.5)-(hard_size_width/2)
hard_y_po=(HEIGHT/3)-(hard_size_height/2)


'''开始某一关游戏(특정레벨시 )'''
def start_scr(screen):
	screen.blit(easytitle,(easy_x_po,easy_y_po))
	screen.blit(hardtitle,(hard_x_po,hard_y_po))
	screen.blit(start_image,(start_x_po,start_y_po))
	pygame.display.flip()
	screen.fill(BLACK)


def pause_scr(screen):
	yongFont = pygame.font.Font( None,50)
	yongtitle5=yongFont.render("PRESS ESC KEY => START",True,WHITE)
	yongtitle6=yongFont.render("PRESS R KEY => RESTART",True,WHITE)
	#Rect생성
	yongRect5=yongtitle5.get_rect()
	yongRect6=yongtitle6.get_rect()
   #yongRect.centerx=round(WIDTH/2)
	yongRect5.centerx=round(WIDTH/2)
	yongRect5.centery=round(HEIGHT/3)
	yongRect6.centerx=round(WIDTH/2)
	yongRect6.centery=round(HEIGHT/1.5)
	pygame.display.flip()
	screen.fill(BLACK)
	screen.blit(yongtitle5,yongRect5)
	screen.blit(yongtitle6,yongRect6)

def restart_screen(screen):
	runn=True
	while runn:
		pause_scr(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					for hero in hero_sprites:
						hero.changeSpeed([-1, 0])
						hero.is_move = True
				elif event.key == pygame.K_RIGHT:
					for hero in hero_sprites:
						hero.changeSpeed([1, 0])
						hero.is_move = True
				elif event.key == pygame.K_UP:
					for hero in hero_sprites:
						hero.changeSpeed([0, -1])
						hero.is_move = True
				elif event.key == pygame.K_DOWN:
					for hero in hero_sprites:
						hero.changeSpeed([0, 1])
						hero.is_move = True
				elif event.key == pygame.K_ESCAPE:
						runn=False
				elif event.key == pygame.K_a:
						sys.exit()
						pygame.quit()
				elif event.key == pygame.K_r:
						main(initialize())

def startLevelGame(level, screen, font):
	clock = pygame.time.Clock()
	SCORE = 0
	wall_sprites = level.setupWalls(SKYBLUE)
	gate_sprites = level.setupGate(WHITE)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites = level.setupFood(YELLOW, WHITE)
	is_clearance = False
	is_true=False
	easytitle=yongFont.render("EASY",True,WHITE)
	clicked_easytitle=yongFont.render("EASY",True,PURPLE)
	easy_size=easytitle.get_rect().size
	easy_size_width=easy_size[0]
	easy_size_height=easy_size[1]
	easy_x_po=(WIDTH/3)-(easy_size_width/2)
	easy_y_po=(HEIGHT/3)-(easy_size_height/2)

	hardtitle=yongFont.render("HARD",True,WHITE)
	hard_size=hardtitle.get_rect().size
	hard_size_width=hard_size[0]
	hard_size_height=hard_size[1]
	hard_x_po=(WIDTH/1.5)-(hard_size_width/2)
	hard_y_po=(HEIGHT/3)-(hard_size_height/2)
	while True:
		screen.blit(easytitle,(easy_x_po,easy_y_po))
		screen.blit(hardtitle,(hard_x_po,hard_y_po))
		screen.blit(start_image,(start_x_po,start_y_po))
		pygame.display.flip()
		screen.fill(BLACK)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.MOUSEMOTION:
				if pygame.mouse.get_pos()[0] >= easy_x_po and pygame.mouse.get_pos()[0] <= easy_x_po+easy_size_width and pygame.mouse.get_pos()[1] >= easy_y_po and pygame.mouse.get_pos()[1] <= easy_y_po+easy_size_height:
					easytitle=yongFont.render("EASY",True,RED)
				elif pygame.mouse.get_pos()[0] >= hard_x_po and pygame.mouse.get_pos()[0] <= hard_x_po+hard_size_width and pygame.mouse.get_pos()[1] >= hard_y_po and pygame.mouse.get_pos()[1] <= hard_y_po+hard_size_height:
					hardtitle=yongFont.render("HARD",True,RED)
				else:
					easytitle=yongFont.render("EASY",True,WHITE)
					hardtitle=yongFont.render("HARD",True,WHITE)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pos()[0] >= easy_x_po and pygame.mouse.get_pos()[0] <= easy_x_po+easy_size_width and pygame.mouse.get_pos()[1] >= easy_y_po and pygame.mouse.get_pos()[1] <= easy_y_po+easy_size_height:
					level.NUMLEVELS=1
					screen.fill(BLACK)
					screen.blit(clicked_easytitle,(easy_x_po,easy_y_po))
					main(initialize())
				if pygame.mouse.get_pos()[0] >= hard_x_po and pygame.mouse.get_pos()[0] <= hard_x_po+hard_size_width and pygame.mouse.get_pos()[1] >= hard_y_po and pygame.mouse.get_pos()[1] <= hard_y_po+hard_size_height:
					level.NUMLEVELS=2
					hardtitle=yongFont.render("HARD",True,RED)
					main1(initialize())
				if pygame.mouse.get_pos()[0] >= start_x_po and pygame.mouse.get_pos()[0] <= start_x_po+start_image_width and pygame.mouse.get_pos()[1] >= start_y_po and pygame.mouse.get_pos()[1] <= start_y_po+start_image_height:
					ff=True
					while ff:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit(-1)
								pygame.quit()
							if event.type == pygame.KEYDOWN:
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
					#일시정지 기능 만드는 중 11/11 창dy
								elif event.key == pygame.K_a:
										sys.exit()
										pygame.quit()
								elif event.key == pygame.K_ESCAPE:
										#여기 제시작
									 	restart_screen(screen)
								elif event.type == pygame.QUIT:
									sys.exit()
									pygame.quit()

							if event.type == pygame.KEYUP:
								if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
									hero.is_move != ff
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
							# 幽灵随机运动(效果不好且有BUG) 유령 무작위 이(나쁜효과 및버그)
							'''
							res = ghost.update(wall_sprites, None)
							while not res:
								ghost.changeSpeed(ghost.randomDirection())
								res = ghost.update(wall_sprites, None)
							'''
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
						if len(food_sprites) == 0:
							is_clearance = True
							break
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
	screen = pygame.display.set_mode([WIDTH, HEIGHT])
	pygame.display.set_caption('Pacman-微信公众号Charles的皮卡丘')
	return screen


'''主函数(주요기)'''
def main(screen):
	'''pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)'''
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
	'''pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)'''
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
