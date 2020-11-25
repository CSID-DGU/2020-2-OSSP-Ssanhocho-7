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
import time


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
HyokyPATH = os.path.join(os.getcwd(),'resources/images/Hyoky.png')

#좌표 설정
pack_x = 287
pack_y = 439
MOVE_LEFT=[-0.5,0]
MOVE_RIGHT=[0.5,0]
MOVE_UP=[0,-0.5]
MOVE_DOWN=[0,0.5]
INFO = [10, 10]

#초기값지정
TIME_INIT=0.0
SCORE_INIT=0
SCORE_MUL=10
LIFE_INIT=3
LIFE=3
SCORE=0
startTime=0.0
endTime=0.0

'''开始某一关游戏'''
def startLevelGame(level, screen, font):
	#변수 불러오기
	global LIFE
	global SCORE
	global pack_x
	global pack_y
	global startTime
	global endTime

	#좌표 표시
	change_x = 0
	change_y = 0

	#시간표시
	clock = pygame.time.Clock()
	fever=Fever.Fever()
	startTime = 0.0
	endTime= 0.0
	total_time = 4
	start_ticks = pygame.time.get_ticks()




	#그룹지정
	wall_sprites = level.setupWalls(SKYBLUE)
	gate_sprites = level.setupGate(WHITE)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	fever_ghost_sprites = level.setupFever(HyokyPATH)
	food_sprites = level.setupFood(YELLOW, WHITE)

	#초기화
	is_clearance = False

	#feverTime
	isFeverTime = False

	#게임 진행
	while True:
		#if SCORE % 1000 == 0:
			#isFeverTime=True #1000점 달성 피버'''
		#키보드 입력(게임 진행)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					for hero in hero_sprites:
						hero.changeSpeed(MOVE_LEFT)
						hero.is_move = True

				elif event.key == pygame.K_RIGHT:
					for hero in hero_sprites:
						hero.changeSpeed(MOVE_RIGHT)
						hero.is_move = True

				elif event.key == pygame.K_UP:
					for hero in hero_sprites:
						hero.changeSpeed(MOVE_UP)
						hero.is_move = True

				elif event.key == pygame.K_DOWN:
					for hero in hero_sprites:
						hero.changeSpeed(MOVE_DOWN)
						hero.is_move = True

			if event.type == pygame.KEYUP:
				if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
					hero.is_move = True
					print("키업 상태")

		#pack_x += change_x
		#pack_y += change_y
		#print(pack_x,pack_y)
		#피버&모드

		#게임 승리(아이템 소진)
		if len(food_sprites) == 0:
			is_clearance = True
			SCORE=SCORE_INIT
			LIFE=LIFE_INIT
			break

        #피버타임
		if SCORE%1000==0 and SCORE>0 and isFeverTime == False:#1000점 단위
			isFeverTime = True#1000점의 배수일 때 마다 fever모드 on
			print("피버 on")
			start_ticks = pygame.time.get_ticks()
			#fever_ghost_sprites.draw(screen)
			#ghost_move(fever_ghost_sprites,wall_sprites,screen)
			#fever.feverTime(hero_sprites,ghost_sprites,SCORE,startTime,endTime,isFeverTime)

		if isFeverTime == True: #fever모드가 on 일 때
			fever.feverTime(hero_sprites,ghost_sprites)#fever타임 실행
			#fever_text = font.render("**FEVER**", True, RED)
			#screen.blit(fever_text, [50,50])
			#pygame.display.flip()
			#clock.tick(10)

			if startTime == 0.0:#starttime이 0 이라면
				startTime = time.time()#시간재기
			elif startTime != 0.0:#starttime이 0이 아니라면
				endTime = time.time()#endtime재기
				if endTime - startTime > 3: # 10초
					isFeverTime = False#10초끝나면 fever off
					#ghost_sprites.draw(screen)
					startTime = TIME_INIT
					endTime = TIME_INIT
					print("피버off")
				elif endTime - startTime <=3:
					isFEverTime = True



		#if SCORE>=500 and SCORE<=800:
			#if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, True):
				#is_clearance = True

		if pygame.sprite.groupcollide(hero_sprites, ghost_sprites,False, False):
			if LIFE<=1:
				SCORE = SCORE_INIT
				LIFE=LIFE_INIT
				is_clearance = False
				break
			else:
				LIFE -=  1
				SCORE = SCORE
				#is_clearance = False
				is_clearance=False
				print('남은 목숨은?!?!?!?! ',LIFE)
				break

		#스크린 그리기
		screen.fill(BLACK)
		for hero in hero_sprites:
			hero.update(wall_sprites, gate_sprites)

		hero_sprites.draw(screen)
		for hero in hero_sprites:
			food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
		SCORE += SCORE_MUL*5*len(food_eaten)
		wall_sprites.draw(screen)
		gate_sprites.draw(screen)
		food_sprites.draw(screen)

		if isFeverTime==True:
			#start_ticks = pygame.time.get_ticks()
			elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000

    		# 피버 타이머
			timer = font.render("timer: " + str(int(total_time - elapsed_time)), True, (255,255,255))
	    	#피버 경과 시간 표시
			screen.blit(timer,[500,10])
			if total_time-elapsed_time <=0:
				print("타임아웃")
				is_clearance = False


		'''for ghost in ghost_sprites:

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
		ghost_sprites.draw(screen)'''
		ghost_move(ghost_sprites,wall_sprites,screen)
		#ghost_move(fever_ghost_sprites,wall_sprites,screen)

		#피버타임 그리기
		if isFeverTime == True:
			fever_text = font.render("**FEVER**", True, PURPLE)
			screen.blit(fever_text, [246,140])

		#상단바 그리기
		score_text = font.render("Score: %s    %s Mode    LIFE : %s" % (SCORE,Levels.MODE,LIFE), True, RED)
		screen.blit(score_text, INFO)

		pygame.display.flip()
		clock.tick(10)

	return is_clearance

#유령 움직임
def ghost_move(ghost_sprites,wall_sprites,screen):
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

'''显示文字'''
def showText(screen, font, is_clearance, flag=False):
	clock = pygame.time.Clock()
	if not is_clearance:
		if LIFE<LIFE_INIT:
			print(LIFE)
			msg = 'LIFE-1'
			positions = [[260, 233], [160, 303]] if not is_clearance else [[145, 233], [65, 303]]
			texts=[font.render(msg, True, WHITE),
				   font.render('Press ENTER to continue', True, WHITE)]
		elif LIFE==LIFE_INIT:
			msg='Game Over'
			positions = [[235, 233], [65, 303], [170, 333]] if not is_clearance else [[145, 233], [65, 303], [170, 333]]
			texts = [font.render(msg, True, WHITE),
				     font.render('Press ENTER to continue or play again.', True, WHITE),
			     	 font.render('Press ESCAPE to quit.', True, WHITE)]
	elif is_clearance:
		msg = 'Congratulations, you won!'
		positions = [[235, 233], [65, 303], [170, 333]] if not is_clearance else [[145, 233], [65, 303], [170, 333]]
		texts = [font.render(msg, True, WHITE),
			     font.render('Press ENTER to continue or play again.', True, WHITE),
		     	 font.render('Press ESCAPE to quit.', True, WHITE)]

	#positions = [[235, 233], [65, 303], [170, 333]] if not is_clearance else [[145, 233], [65, 303], [170, 333]]
	surface = pygame.Surface((400, 200))
	surface.set_alpha(10)
	surface.fill((128, 128, 128))
	screen.blit(surface, (100, 200))
	#if msg == 'LIFE-1':
		#texts=[font.render(msg, True, WHITE),
			  # font.render('Press ENTER to continue', True, WHITE)]
	#else:
		#texts = [font.render(msg, True, WHITE),
			    # font.render('Press ENTER to continue or play again.', True, WHITE),
		     	# font.render('Press ESCAPE to quit.', True, WHITE)]
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if is_clearance:
						if not flag:
							main(initialize())
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
		clock.tick(60)


'''初始化'''
def initialize():
	pygame.init()
	icon_image = pygame.image.load(ICONPATH)
	pygame.display.set_icon(icon_image)
	screen = pygame.display.set_mode([606, 606])
	pygame.display.set_caption('OSSP Ssanhocho pacman')
	level = Levels.Level1()
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

	if Levels.MODE == 'EASY':
		level = Levels.Level1()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.MODE == 'HARD':
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)

	if Levels.MODE == 'HARD':
		level = Levels.Level2()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.MODE == 'HARD':
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)



'''test'''
if __name__ == '__main__':
	main(initialize())
