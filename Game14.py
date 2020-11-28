'''
Function:
	吃豆豆小游戏
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import os, sys ,pygame,Levels,Fever,time
pygame.init()

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
MOVE_LEFT=[-0.5,0]
MOVE_RIGHT=[0.5,0]
MOVE_UP=[0,-0.5]
MOVE_DOWN=[0,0.5]
INFO = [10, 10]
GATE_MID=[246,140]

#초기값지정
TIME_INIT=0.0
startTime=0.0
endTime=0.0
FEVER_TOTAL = 5
FEVER_SCORE = 1000
fever_count = 1
SCORE_INIT=0
SCORE_MUL=30
SCORE=0
LIFE_INIT=3
LIFE=3
FPS=10

#그룹지정
loss_food_sprites = pygame.sprite.Group()

'''开始某一关游戏'''
def startLevelGame(level, screen, font):

	#변수 불러오기
	global LIFE
	global SCORE
	global fever_count
	global startTime
	global endTime
	global loss_food_sprites

	#시간표시
	clock = pygame.time.Clock()
	fever=Fever.Fever()
	startTime = TIME_INIT
	endTime= TIME_INIT
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

		#키보드 입력(게임 진행)
		if LIFE>=1 and LIFE<LIFE_INIT:
			food_sprites = loss_food_sprites
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

		#게임 승리(아이템 소진)
		if len(food_sprites) == 0:
			is_clearance = True
			SCORE=SCORE_INIT
			LIFE=LIFE_INIT
			break

        #피버타임
		if SCORE > (fever_count*FEVER_SCORE) and isFeverTime == False:#1000점 단위
			isFeverTime = True#1000점의 배수일 때 마다 fever모드 on
			fever_count += 1
			start_ticks = pygame.time.get_ticks()

		if isFeverTime == True: #fever모드가 on 일 때
			fever.feverTime(hero_sprites,ghost_sprites)#fever타임 실행

			if startTime == TIME_INIT:#starttime이 0 이라면
				startTime = time.time()#시간재기
			elif startTime != TIME_INIT:#starttime이 0이 아니라면
				endTime = time.time()#endtime재기
				if endTime - startTime > FEVER_TOTAL: # 5초
					isFeverTime = False#5초끝나면 fever off
					startTime = TIME_INIT
					endTime = TIME_INIT
				elif endTime - startTime <=FEVER_TOTAL:
					isFEverTime = True

		#목숨 처리
		if pygame.sprite.groupcollide(hero_sprites, ghost_sprites,False, False):
			if LIFE<=1:
				SCORE = SCORE_INIT
				LIFE=LIFE_INIT
				fever_count = 0
				is_clearance = False
				break
			else:
				LIFE -=  1
				SCORE = SCORE
				loss_food_sprites = food_sprites
				is_clearance=False
				break

		#스크린 그리기
		screen.fill(BLACK)
		for hero in hero_sprites:
			hero.update(wall_sprites, gate_sprites)

		hero_sprites.draw(screen)
		for hero in hero_sprites:
			food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
		SCORE += SCORE_MUL*len(food_eaten)
		wall_sprites.draw(screen)
		gate_sprites.draw(screen)
		food_sprites.draw(screen)

		#피버 타이머
		if isFeverTime==True:
			#start_ticks = pygame.time.get_ticks()
			elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    		# 피버 타이머
			timer = font.render("FEEVR Timer: " + str(int(FEVER_TOTAL - elapsed_time)), True, WHITE)
	    	#피버 경과 시간 표시
			screen.blit(timer,[460,10])

		ghost_move(ghost_sprites,wall_sprites,screen)

		#피버타임 그리기
		if isFeverTime == True:
			fever_text = font.render("**FEVER**", True, PURPLE)
			screen.blit(fever_text, GATE_MID)

		#상단바 그리기
		score_text = font.render("Score: %s    %s Mode    LIFE : %s" % (SCORE,Levels.MODE,LIFE), True, RED)
		screen.blit(score_text, INFO)

		pygame.display.flip()
		clock.tick(FPS)

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

	surface = pygame.Surface((400, 200))
	surface.set_alpha(10)
	surface.fill((128, 128, 128))
	screen.blit(surface, (100, 200))

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
