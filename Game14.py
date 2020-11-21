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
RUNNING, PAUSE = 0, 1
state = RUNNING
pause_text = "일시정지"


#11/11
'''INTRO = [["게임 시작", 0],
         ["제어", 0],
         ["게임에대해", 0],
         ["순위표", 0],
         ["exit", 0]]'''
'''
class StartScreen:
    #시작 인터페이스 표시를 담당하는 클래스
    def __init__(self):
        global all_sprites, INTRO
        # 고스트 이동속도
        #self.v = 6
        #화면에 게임 이름 이미지 및 위치로드
        image = load_image('start_screen.png')
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = WIDTH // 2 - image.get_width() // 2
        sprite.rect.y = 0
        all_sprites.add(sprite)

    def print_text(self):
        #시작 창의 텍스트 표
        for i in range(len(INTRO)):
            if INTRO[i][1] == 0:
                color = pygame.Color("white")
            else:
                color = pygame.Color("yellow")
            font = pygame.font.Font(FULLNAME, 50)
            text = font.render(INTRO[i][0], 1, (color))
            start_x = WIDTH // 2 - text.get_width() // 2
            start_y = HEIGHT // 2 - text.get_height() // 2 - 50
            text_x = start_x
            text_y = start_y + i * 60
            screen.blit(text, (text_x, text_y))'''


'''开始某一关游戏(특정레벨시 )'''
def startLevelGame(level, screen, font):
	clock = pygame.time.Clock()
	SCORE = 0
	wall_sprites = level.setupWalls(SKYBLUE)
	gate_sprites = level.setupGate(WHITE)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites = level.setupFood(YELLOW, WHITE)
	is_clearance = False
	while True:
		yongFont = pygame.font.Font( None,50)
		yongtitle=yongFont.render("PRESS E KEY => EASYMODE START",True,WHITE)
		yongtitle2=yongFont.render("PRESS S KEY => start",True,WHITE)
		yongtitle3=yongFont.render("PRESS H KEY => HARDMODE START",True,WHITE)
		#Rect생성
		yongRect=yongtitle.get_rect()
		yongRect2=yongtitle2.get_rect()
		yongRect3=yongtitle3.get_rect()
		#yongRect.centerx=round(WIDTH/2)
		yongRect.centerx=round(WIDTH/2)
		yongRect.centery=round(HEIGHT/3)

		yongRect2.centerx=round(WIDTH/2)
		yongRect2.centery=round(HEIGHT/1.5)

		yongRect3.centerx=round(WIDTH/2)
		yongRect3.centery=round(HEIGHT/6)

		pygame.display.flip()
		screen.fill(BLACK)
		screen.blit(yongtitle,yongRect)
		screen.blit(yongtitle2,yongRect2)
		screen.blit(yongtitle3,yongRect3)
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
										runn=True
										#여기 제시작
										while runn:
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
							main(initialize())
					else:
						main(initialize())
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
	Levels.NUMLEVELS=1
	font_small = pygame.font.Font(FONTPATH, 18)
	font_big = pygame.font.Font(FONTPATH, 24)
	#for num_level in range(1, Levels.NUMLEVELS+1):
	if Levels.NUMLEVELS == 1:
		level = Levels.Level1()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.NUMLEVELS == 1:
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)


def main1(screen):
	'''pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)'''
	pygame.font.init()
	Levels.NUMLEVELS=2
	font_small = pygame.font.Font(FONTPATH, 18)
	font_big = pygame.font.Font(FONTPATH, 24)

	if Levels.NUMLEVELS == 2:
		level = Levels.Level2()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.NUMLEVELS == 2:
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)

'''test'''

if __name__ == '__main__':
		main(initialize())
