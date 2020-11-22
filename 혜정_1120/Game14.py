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
import Fever


'''定义一些必要的参数'''
#색 지정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
SKYBLUE = (0, 191, 255)

#path 지정
BGMPATH = os.path.join(os.getcwd(), 'resources/sounds/bg.mp3')
ICONPATH = os.path.join(os.getcwd(), 'resources/images/icon.png')
FONTPATH = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')
HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), 'resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), 'resources/images/Pinky.png')
#좌표 설정
pack_x = 287
pack_y = 439
MOVE_LEFT=[-0.5,0]
MOVE_RIGHT=[0.5,0]
MOVE_UP=[0,-0.5]
MOVE_DOWN=[0,0.5]
INFO = [10, 10]

#초기값지정
MODE = Levels.NUMLEVELS
SCORE_INIT=0
SCORE_MUL=10
LIFE_INIT=3

'''开始某一关游戏'''
def startLevelGame(level, screen, font):
	#변수 불러오기
	global MODE
	global SCORE_INIT
	global LIFE_INIT
	global pack_x
	global pack_y

	#좌표 표시
	change_x = 0
	change_y = 0

	#시간표시
	clock = pygame.time.Clock()

	#그룹지정
	wall_sprites = level.setupWalls(SKYBLUE)
	gate_sprites = level.setupGate(WHITE)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites = level.setupFood(YELLOW, WHITE)

	#초기화
	is_clearance = False
	Fever = False   # 피버 off
	SCORE = SCORE_INIT
	LIFE = LIFE_INIT

	while True:
		'''if SCORE % 1000 == 0:
			fever=True #1000점 달성 피버'''
		#키보드 입력(게임 진행)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					print("왼쪽 키")
					for hero in hero_sprites:
						change_x=-0.5
						change_y=0
						hero.changeSpeed(MOVE_LEFT)
						hero.is_move = True
						print(change_x,change_y)

				elif event.key == pygame.K_RIGHT:
					print("오른쪽 키 ")
					for hero in hero_sprites:
						hero.changeSpeed(MOVE_RIGHT)
						hero.is_move = True
						change_x=0.5
						change_y=0
						print(change_x,change_y)

				elif event.key == pygame.K_UP:
					print("위쪽 키")
					for hero in hero_sprites:
						hero.changeSpeed(MOVE_UP)
						hero.is_move = True
						change_x=0
						change_y=-0.5
						print(change_x,change_y)

				elif event.key == pygame.K_DOWN:
					print("아래쪽 키")
					for hero in hero_sprites:
						hero.changeSpeed(MOVE_DOWN)
						hero.is_move = True
						change_x=0
						change_y=0.5
						print(change_x,change_y)

			if event.type == pygame.KEYUP:
				if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
					hero.is_move = True
					print("키업 상태")

		pack_x += change_x
		pack_y += change_y
		print(pack_x,pack_y)

		#스크린 그리기
		screen.fill(BLACK)
		for hero in hero_sprites:
			hero.update(wall_sprites, gate_sprites)

		hero_sprites.draw(screen)
		for hero in hero_sprites:
			food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
			food_big = pygame.sprite.spritecollide(hero , food_sprites_big,True)
		SCORE = SCORE + (SCORE_MUL*len(food_eaten)) +(50*len(food_big))
		wall_sprites.draw(screen)
		gate_sprites.draw(screen)
		food_sprites.draw(screen)

		for ghost in ghost_sprites:

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

		#상단바 그리기
		score_text = font.render("Score: %s    %s Mode    LIFE : %s" % (SCORE,MODE,LIFE), True, RED)
		screen.blit(score_text, INFO)

		#피버&모드
		if len(food_sprites) == 0:
			if MODE < 2:
				MODE += 1
			elif MODE >= 2:
				MODE = 1
				SCORE=0
			is_clearance = True
			break

		if SCORE>=500 and SCORE<=800:
			if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, True):
				is_clearance = True
		if pygame.sprite.groupcollide(hero_sprites, ghost_sprites,True, False):
			LIFE = LIFE -1
			is_clearance = False
			print("남은 목숨은 ?!?!?!?!?!" , LIFE)
			if LIFE<=0:
				SCORE = INIT
				MODE = 1
				LIFE=3
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
	pygame.display.set_caption('OSSP Ssanhocho pacman')
	level = Levels.Level2()
	return screen


'''主函数'''
def main(screen):
	pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)
	pygame.font.init()
	font_small = pygame.font.Font(FONTPATH, 18)
	font_big = pygame.font.Font(FONTPATH, 24)
	#for num_level in range(1, Levels.NUMLEVELS+1):

	if MODE == 1:
		level = Levels.Level1()
		is_clearance = startLevelGame(level, screen, font_small)
		if MODE == Levels.NUMLEVELS:
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)

	if MODE == 2:
		level = Levels.Level2()
		is_clearance = startLevelGame(level, screen, font_small)
		if MODE == Levels.NUMLEVELS:
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)



'''test'''
if __name__ == '__main__':
	main(initialize())
