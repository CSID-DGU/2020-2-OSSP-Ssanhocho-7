import os, sys ,pygame,Levels,Fever,time,pymysql
import pandas as pd

pygame.init()

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
FONTPATH = os.path.join(os.getcwd(), 'resources/font/Firenight-Regular.otf')
HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), 'resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), 'resources/images/Pinky.png')
FEVERPATH = os.path.join(os.getcwd(),'resources/images/fever.png')
FVTXTPATH=os.path.join(os.getcwd(),'resources/images/bomb.png')
backgroundimg = pygame.image.load("resources/images/background.png")

#좌표 설정
#1. 움직임 좌표
MOVE_LEFT=[-0.5,0]
MOVE_RIGHT=[0.5,0]
MOVE_UP=[0,-0.5]
MOVE_DOWN=[0,0.5]
DIRECTION_INIT=[0,0]
#2. info,img 표시 좌표
INFO = [10, 10]
GATE_MID=[246,140]
GATE_MID_H=[235, 252]
FEVER_INFO=[220,130]
TIMER_INFO=[420,10]
back_loc = (0,0)

#스크린
screen_size=606,606
initial_screen_size=606,606
easy_screen=577,306
show_text_size = 400,200

set_easy_color='WHITE'
set_hard_color='WHITE'
set_rank_color='WHITE'
moniter_size=pygame.display.Info().current_w,pygame.display.Info().current_h

music_on=True
#폰트 50은 초기값지정입니다 후에 변경합니다
gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',int(screen_size[0]/15))
title_size = 50
small_font_size = 24
big_font_size = 30
#--------------
#1.타임
TIME_INIT=0.0
startTime=0.0
endTime=0.0
#2.피버
FEVER_TOTAL = 5
FEVER_SCORE = 1000
FEVER_EAT = 50
FEVER_COUNT = 1
#3.점수
SCORE_INIT=0
SCORE_SMALL=30
SCORE_BIG=60
SCORE=0
#4.목숨
LIFE_INIT=3
LIFE=3
#5.스테이지
STAGE=1
STAGE_INIT = 1
#6.fps
FPS=10
#7.유저 정보
user_id=''
id_init=''
user_score=0
#8.rank
rank_num = 10
rank_line_num = 12

#그룹지정
loss_food_sprites = pygame.sprite.Group()

#스테이지
STAGEFONT = pygame.font.Font('resources/font/Firenight-Regular.otf',50)
WIDTH=606
HEIGHT=606

#서버
host =  "ssanhocho.cigvjaajbt9o.ap-southeast-1.rds.amazonaws.com"
port = 3306
username = "ssanhocho"
password = "ssanhocho7&"
database = "test"
conn = pymysql.connect(host=host,port=port,user=username,passwd=password,db=database,charset='utf8')
curs=conn.cursor()

#x[index]/n (index=0 -> 가로 index=1 -> 세로) 를 n등분 이하 코드 모두 적용

def restart_screen(screen):
	global set_easy_color
	global set_hard_color
	global screen_size,gameFont
	runn=True
	resizing=False
	gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',int(screen_size[0]/15))
	startmsg=gameFont.render("PRESS ESC KEY TO START",True,WHITE)
	restartmsg=gameFont.render("PRESS R KEY TO RESTART",True,WHITE)

	startmsg_size=startmsg.get_rect().size
	startmsg_size_width=startmsg_size[0]
	startmsg_size_height=startmsg_size[1]
	startmsg_x_po=(screen_size[0]/2)-(startmsg_size_width/2)
	startmsg_y_po=(screen_size[1]/3)-(startmsg_size_height/2)


	restartmsg_size=restartmsg.get_rect().size
	restartmsg_size_width=restartmsg_size[0]
	restartmsg_size_height=restartmsg_size[1]
	restartmsg_x_po=(screen_size[0]/2)-(restartmsg_size_width/2)
	restartmsg_y_po=(screen_size[1]/1.5)-(restartmsg_size_height/2)

	screen.fill(BLACK)
	screen.blit(startmsg,(startmsg_x_po,startmsg_y_po))
	screen.blit(restartmsg,(restartmsg_x_po,restartmsg_y_po))
	pygame.display.flip()
	while runn:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.VIDEORESIZE:
				last_resize=event.w,event.h
				if event.w>event.h :
					if last_resize[0]>=moniter_size[1]:
						a=moniter_size[1]
						event.w=a
					last_resize=event.w , event.w


				elif(event.h>event.w):
					if last_resize[1]>=moniter_size[1]:
						b=moniter_size[1]
						event.h=b

					last_resize=event.h , event.h

				if event.w < initial_screen_size[0] or event.h < initial_screen_size[1] :
					last_resize=initial_screen_size

				screen_size=last_resize
				resizing=True
				if resizing :
					screen_size=last_resize
					screen=pygame.display.set_mode(screen_size, pygame.RESIZABLE)
					resizing=False
					resizing_this_frame=False
					last_resize=None
					gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',int(screen_size[0]/12))
					startmsg=gameFont.render("PRESS ESC KEY TO START",True,WHITE)
					restartmsg=gameFont.render("PRESS R KEY TO RESTART",True,WHITE)

					startmsg_size=startmsg.get_rect().size
					startmsg_size_width=startmsg_size[0]
					startmsg_size_height=startmsg_size[1]
					startmsg_x_po=(screen_size[0]/2)-(startmsg_size_width/2)
					startmsg_y_po=(screen_size[1]/3)-(startmsg_size_height/2)


					restartmsg_size=restartmsg.get_rect().size
					restartmsg_size_width=restartmsg_size[0]
					restartmsg_size_height=restartmsg_size[1]
					restartmsg_x_po=(screen_size[0]/2)-(restartmsg_size_width/2)
					restartmsg_y_po=(screen_size[1]/1.5)-(restartmsg_size_height/2)

					screen.fill(BLACK)
					screen.blit(startmsg,(startmsg_x_po,startmsg_y_po))
					screen.blit(restartmsg,(restartmsg_x_po,restartmsg_y_po))
					pygame.display.flip()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
						runn=False

				elif event.key == pygame.K_r:
						set_easy_color='WHITE'
						set_hard_color='WHITE'
						main(initialize())



def startLevelGame(level, screen, font):

	#변수 불러오기
	global LIFE, SCORE, STAGE , user_score , direction
	global startTime, endTime
	global loss_food_sprites
	global screen_size ,moniter_size, set_easy_color, set_hard_color, set_rank_color , gameFont
	global music_on
	global INFO,GATE_MID,GATE_MID_H,FEVER_INFO,TIMER_INFO
	gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',int(screen_size[0]/15))

	fever=Fever.Fever()
	#시간표시
	clock = pygame.time.Clock()
	startTime = TIME_INIT
	endTime= TIME_INIT
	start_ticks = pygame.time.get_ticks()

	#그룹지정
	wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
	gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
	food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])
	#total_score = len(food_sprites) * SCORE_MUL * STAGE

	#INFO
	INFO = [screen_size[0]/60.6, screen_size[1]/60.6]
	GATE_MID=[screen_size[0]/2.4,screen_size[1]/4.33]
	GATE_MID_H=[screen_size[0]/2.58,screen_size[1]/2.40]
	FEVER_INFO=[screen_size[0]/2.5,screen_size[1]/2.16]
	TIMER_INFO=[screen_size[0]/1.44,screen_size[1]/60.6]

	#초기화
	is_clearance = False

	#feverTime
	isFeverTime = False
	fever_count = FEVER_COUNT
	is_nextstage=False
	#stage

	direction = DIRECTION_INIT

	#기록
	user_score=SCORE_INIT

	#easy mode
	easytitle=gameFont.render("EASY",True,WHITE)
	clicked_easytitle=gameFont.render("EASY",True,RED)
	easy_size=easytitle.get_rect().size
	easy_size_width=easy_size[0]
	easy_size_height=easy_size[1]
	easy_x_po=(screen_size[0]/3)-(easy_size_width/2)
	easy_y_po=(screen_size[1]/3)-(easy_size_height/2)

	#hard mode
	hardtitle=gameFont.render("HARD",True,WHITE)
	clicked_hardtitle=gameFont.render("HARD",True,RED)
	hard_size=hardtitle.get_rect().size
	hard_size_width=hard_size[0]
	hard_size_height=hard_size[1]
	hard_x_po=(screen_size[0]/1.5)-(hard_size_width/2)
	hard_y_po=(screen_size[1]/3)-(hard_size_height/2)

	#ranking
	ranktitle = gameFont.render("RANK", True, WHITE)
	clicked_ranktitle = gameFont.render("RANK", True, YELLOW)
	rank_size = ranktitle.get_rect().size
	rank_size_width = hard_size[0]
	rank_size_height = hard_size[1]
	rank_x_po = screen_size[0]/2 - rank_size_width/2
	rank_y_po = screen_size[1]/2

	#배경
	background=pygame.transform.scale(backgroundimg,screen_size)
	background.set_alpha(200)

	#시작 버튼
	start_image_ex=pygame.image.load('resources/images/start_button.png')
	start_image=pygame.transform.scale(start_image_ex,((int)(screen_size[0]/5),(int)(screen_size[1]/10)))
	start_image_size=start_image.get_rect().size
	start_image_width=start_image_size[0]
	start_image_height=start_image_size[1]
	start_x_po=(screen_size[0]/2)-(start_image_width/2)
	start_y_po=(screen_size[1]/1.5)-(start_image_height/2)
	#start_scr(screen,WHITE,WIDTH,HEIGHT)
	resizing=False
	#resizing_this_frame=False
	last_resize=None

	#게임 진행
	while True:
		#키보드 입력(게임 진행)
		#show_rank(screen,font)
		gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',int(screen_size[0]/15))
		start_image=pygame.transform.scale(start_image_ex,((int)(screen_size[0]/5),(int)(screen_size[1]/10)))
		start_image_size=start_image.get_rect().size
		start_image_width=start_image_size[0]
		start_image_height=start_image_size[1]
		start_x_po=(screen_size[0]/2)-(start_image_width/2)
		start_y_po=(screen_size[1]/1.5)-(start_image_height/2)

		screen.blit(background,back_loc)
		if set_easy_color =='WHITE':
			screen.blit(easytitle,(easy_x_po,easy_y_po))
		elif  set_easy_color=='RED':
			screen.blit(clicked_easytitle,(easy_x_po,easy_y_po))
		if set_hard_color =='WHITE':
			screen.blit(hardtitle,(hard_x_po,hard_y_po))
		elif set_hard_color =='RED':
			screen.blit(clicked_hardtitle,(hard_x_po,hard_y_po))
		if set_rank_color == 'WHITE':
			screen.blit(ranktitle, (rank_x_po, rank_y_po))
		elif set_rank_color == 'YELLOW':
			screen.blit(clicked_ranktitle, (rank_x_po, rank_y_po))

		screen.blit(start_image,(start_x_po,start_y_po))
		pygame.display.flip()
		screen.fill(BLACK)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
				# 음악 일시정지
					if music_on:
						pygame.mixer.music.pause()
						music_on=False
					else:
						pygame.mixer.music.unpause()
						music_on=True
			if event.type == pygame.VIDEORESIZE:
				#resizing_this_frame=True
				last_resize=event.w,event.h
				if event.w>event.h :
					if last_resize[0]>=moniter_size[1]:
						a=moniter_size[1]
						event.w=a
					last_resize=event.w , event.w

				elif(event.h>event.w):
					if last_resize[1]>=moniter_size[1]:
						b=moniter_size[1]
						event.h=b
					last_resize=event.h , event.h

				if event.w < initial_screen_size[0] or event.h < initial_screen_size[1] :
					last_resize=initial_screen_size

					#resizing=True
				screen_size=last_resize
				resizing=True

				if resizing :
					screen=pygame.display.set_mode(screen_size , pygame.RESIZABLE)
					resizing=False
					resizing_this_frame=False
					last_resize=None
					start_image=pygame.transform.scale(start_image_ex,((int)(screen_size[0]/5),(int)(screen_size[1]/10)))
					start_image_size=start_image.get_rect().size
					start_image_width=start_image_size[0]
					start_image_height=start_image_size[1]
					start_x_po=(screen_size[0]/2)-(start_image_width/2)
					start_y_po=(screen_size[1]/1.5)-(start_image_height/2)
					screen.blit(start_image,(start_x_po,start_y_po))
					if set_easy_color == 'RED' and set_hard_color == 'WHITE':
						main(initialize())
					elif set_easy_color == 'WHITE' and set_hard_color =='RED' :
						main1(initialize())
					else :main(initialize())

			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.MOUSEMOTION:
				#get_pos[index] (index = 0 -> 가로 , index = 1 -> 세로)
				if pygame.mouse.get_pos()[0] >= easy_x_po and pygame.mouse.get_pos()[0] <= easy_x_po+easy_size_width and pygame.mouse.get_pos()[1] >= easy_y_po and pygame.mouse.get_pos()[1] <= easy_y_po+easy_size_height:
					easytitle=gameFont.render("EASY",True,RED)
				elif pygame.mouse.get_pos()[0] >= hard_x_po and pygame.mouse.get_pos()[0] <= hard_x_po+hard_size_width and pygame.mouse.get_pos()[1] >= hard_y_po and pygame.mouse.get_pos()[1] <= hard_y_po+hard_size_height:
					hardtitle=gameFont.render("HARD",True,RED)
				elif rank_x_po <= pygame.mouse.get_pos()[0] <= rank_x_po+rank_size_width and rank_y_po <= pygame.mouse.get_pos()[1] <= rank_y_po+rank_size_height:
					ranktitle = gameFont.render("RANK", True, YELLOW)
				else:
					easytitle=gameFont.render("EASY",True,WHITE)
					hardtitle=gameFont.render("HARD",True,WHITE)
					ranktitle = gameFont.render("RANK", True, WHITE)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if easy_x_po <= pygame.mouse.get_pos()[0] <= easy_x_po+easy_size_width and easy_y_po <= pygame.mouse.get_pos()[1] <= easy_y_po+easy_size_height:
					set_easy_color='RED'
					set_hard_color='WHITE'
					set_rank_color = 'WHITE'
					main(initialize())
				if hard_x_po <= pygame.mouse.get_pos()[0] <= hard_x_po+hard_size_width and hard_y_po <= pygame.mouse.get_pos()[1] <= hard_y_po+hard_size_height:
					set_easy_color='WHITE'
					set_hard_color='RED'
					set_rank_color = 'WHITE'
					main1(initialize())
				if rank_x_po <= pygame.mouse.get_pos()[0] <= rank_x_po+rank_size_width and rank_y_po <= pygame.mouse.get_pos()[1] <= rank_y_po+rank_size_height:
					set_easy_color='WHITE'
					set_hard_color='WHITE'
					set_rank_color = 'YELLOW'
					show_rank(screen,font)

				if start_x_po <= pygame.mouse.get_pos()[0] <= start_x_po+start_image_width and start_y_po <= pygame.mouse.get_pos()[1] <= start_y_po+start_image_height:
					is_true = True
					while is_true:

						if LIFE>=1 and LIFE<LIFE_INIT and is_nextstage==False :
							food_sprites = loss_food_sprites

						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit(-1)
								pygame.quit()
							if event.type == pygame.VIDEORESIZE:
								last_resize=event.w,event.h
								if event.w>event.h :
									if last_resize[0]>=moniter_size[1]:
										a=moniter_size[1]
										event.w=a
									last_resize=event.w , event.w

								elif(event.h>event.w):
									if last_resize[1]>=moniter_size[1]:
										b=moniter_size[1]
										event.h=b
									last_resize=event.h , event.h

								if event.w<initial_screen_size[0] or event.h < initial_screen_size[1] :
									last_resize=initial_screen_size

									#resizing=True
								screen_size=last_resize
								resizing=True

								if resizing :
									screen_size=last_resize
									screen=pygame.display.set_mode(screen_size, pygame.RESIZABLE)
									resizing=False
									resizing_this_frame=False
									last_resize=None
									wall_sprites = level.setupWalls(SKYBLUE,screen_size[0],screen_size[1])
									gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
									food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])




							if event.type == pygame.KEYDOWN:

								if event.key == pygame.K_m:
									if music_on:
										pygame.mixer.music.pause()
										music_on = False
									else:
										pygame.mixer.music.unpause()
										music_on = True


								if event.key == pygame.K_LEFT:
									for hero in hero_sprites:
										hero.pchangeSpeed(isFeverTime,MOVE_LEFT)
										direction = MOVE_LEFT
										hero.is_move = is_true

								elif event.key == pygame.K_RIGHT:
									for hero in hero_sprites:
										hero.pchangeSpeed(isFeverTime,MOVE_RIGHT)
										direction = MOVE_RIGHT
										hero.is_move = is_true

								elif event.key == pygame.K_UP:
									for hero in hero_sprites:
										hero.pchangeSpeed(isFeverTime,MOVE_UP)
										direction = MOVE_UP
										hero.is_move = is_true

								elif event.key == pygame.K_DOWN:
									for hero in hero_sprites:
										hero.pchangeSpeed(isFeverTime,MOVE_DOWN)
										direction = MOVE_DOWN
										hero.is_move = is_true

								elif event.key == pygame.K_r:
									show_rank(screen,font)

								elif event.key == pygame.K_a:
										sys.exit()
										pygame.quit()
								elif event.key == pygame.K_ESCAPE:
									user_score = SCORE
									SCORE = SCORE_INIT
									LIFE=LIFE_INIT
									fever_count = FEVER_COUNT#fevercount 초기화
									is_clearance = False
									is_nextstage = False
									STAGE=STAGE_INIT
									restart_screen(screen)
								elif event.type == pygame.QUIT:
									sys.exit()
									pygame.quit()

							if event.type == pygame.KEYUP:
									if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
										hero.pchangeSpeed(isFeverTime,direction)
										hero.is_move = is_true


		#게임 승리(아이템 소진)
						if len(food_sprites) == 0: #맵 내의 남아있는 아이템의 갯수가 0일 때
							is_clearance = True
							SCORE=SCORE
							LIFE=LIFE
							STAGE+=1 #next stage
							is_nextstage=True
							direction=DIRECTION_INIT
								#break
							wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
							gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
							hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
							food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])

				        #피버타임
						if SCORE > (fever_count*FEVER_SCORE) and isFeverTime == False:#1000점 단위
							isFeverTime = True#1000점의 배수일 때 마다 fever모드 on
							fever_count += 1 #피버 발동 시 마다 카운트(횟수 세기)
							start_ticks = pygame.time.get_ticks()

						if isFeverTime == True: #fever모드가 on 일 때
							fever.feverTime(hero_sprites,ghost_sprites) #fever타임 실행
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
						if pygame.sprite.groupcollide(hero_sprites, ghost_sprites,False, False) and not isFeverTime:
							if LIFE<=1:#life의 개수가 소진
								user_score = SCORE
								SCORE = SCORE_INIT
								LIFE=LIFE_INIT
								fever_count = FEVER_COUNT#fevercount 초기화
								is_clearance = False
								is_nextstage = False
								STAGE=STAGE_INIT
								print("유저 점수",user_score)
								break
							else:
								LIFE -=  1 #life 감소
								SCORE = SCORE
								loss_food_sprites = food_sprites
								STAGE=STAGE
								is_clearance=False
								is_nextstage=False
								wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
								gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
								hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
								food_sprites = loss_food_sprites
								direction = DIRECTION_INIT
								lrestart_screen(screen)


						#스크린 그리기
						screen.fill(BLACK)
						for hero in hero_sprites:
							hero.update(wall_sprites, gate_sprites)

						hero_sprites.draw(screen)
						for hero in hero_sprites:
							food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
							hero.pchangeSpeed(isFeverTime,direction)
						for food in food_eaten:
							# food.width == screen_size[0]/40, screen_size[0]/30 : 큰아이템
							if food.width == screen_size[0]/40 or food.width == screen_size[0]/30:
								SCORE += SCORE_BIG
							# 작은아이템
							else:
								SCORE += SCORE_SMALL
						#SCORE += SCORE_MUL*len(food_eaten)
						wall_sprites.draw(screen)
						gate_sprites.draw(screen)
						food_sprites.draw(screen)

						#피버 타이머
						if isFeverTime==True:
							elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000 #초 단위
				    		# 피버 타이머
							gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',int(screen_size[0]/15))
							timer = font.render("FEVER Timer: " + str(int(FEVER_TOTAL - elapsed_time)), True, WHITE)
					    	#피버 경과 시간 표시
							timer_size=timer.get_rect().size
							timer_size_width=timer_size[0]
							timer_size_height=timer_size[1]
							timer_x_po=(screen_size[0]/1.44)-(timer_size_width/60.6)
							timer_y_po=(screen_size[1]/60.6)-(timer_size_height/60.6)
							screen.blit(timer, (timer_x_po,timer_y_po))

						ghost_move(isFeverTime,hero_sprites,ghost_sprites,wall_sprites,gate_sprites,screen)

						#피버타임 그리기
						if isFeverTime == True:
							fever_text = pygame.image.load('resources/images/bomb.png')
							fv_txt_img= pygame.transform.scale(fever_text,((int)(screen_size[0]/5),(int)(screen_size[1]/5)))
							fv_image_size=fv_txt_img.get_rect().size
							fv_image_width=fv_image_size[0]
							fv_image_height=fv_image_size[1]
							fv_x_po=(screen_size[0]/2)-(fv_image_width/2)
							fv_y_po=(screen_size[1]/2)-(fv_image_height/2)

							if Levels.MODE=='EASY':
								fv_txt_img= pygame.transform.scale(fever_text,((int)(screen_size[0]/7),(int)(screen_size[1]/12)))
								fv_image_size=fv_txt_img.get_rect().size
								fv_image_width=fv_image_size[0]
								fv_image_height=fv_image_size[1]
								fv_x_po=(screen_size[0]/2)-(fv_image_width/2)
								fv_y_po=(screen_size[1]/2)-(fv_image_height/2)
								screen.blit(fv_txt_img,(fv_x_po,fv_y_po))
							elif Levels.MODE=='HARD':

								screen.blit(fv_txt_img,(fv_x_po,fv_y_po))

						#상단바 그리기

						gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',int(screen_size[0]/24))
						score_text = gameFont.render("Score: %s    %s Mode    LIFE : %s" % (SCORE,Levels.MODE,LIFE), True, WHITE)
						score_size=score_text.get_rect().size
						score_size_width=score_size[0]
						score_size_height=score_size[1]
						score_x_po=(screen_size[0]/60.6)-(score_size_width/60.6)
						score_y_po=(screen_size[1]/60.6)-(score_size_height/60.6)
						screen.blit(score_text, (score_x_po,score_y_po))

						pygame.display.flip()
						clock.tick(FPS)

					return is_clearance

def lrestart_screen(screen):
	global set_easy_color
	global set_hard_color
	global screen_size
	runn=True
	resizing=False
	startmsg=gameFont.render("LIFE - 1",True,WHITE)
	restartmsg=gameFont.render("Press Enter to Restart",True,WHITE)

	startmsg_size=startmsg.get_rect().size
	startmsg_size_width=startmsg_size[0]
	startmsg_size_height=startmsg_size[1]
	startmsg_x_po=(screen_size[0]/2)-(startmsg_size_width/2)
	startmsg_y_po=(screen_size[1]/3)-(startmsg_size_height/2)

	restartmsg_size=restartmsg.get_rect().size
	restartmsg_size_width=restartmsg_size[0]
	restartmsg_size_height=restartmsg_size[1]
	restartmsg_x_po=(screen_size[0]/2)-(restartmsg_size_width/2)
	restartmsg_y_po=(screen_size[1]/1.5)-(restartmsg_size_height/2)
	screen.fill(BLACK)
	screen.blit(startmsg,(startmsg_x_po,startmsg_y_po))
	screen.blit(restartmsg,(restartmsg_x_po,restartmsg_y_po))
	pygame.display.flip()

	if Levels.MODE == 'EASY':
		level = Levels.Level1()
	elif Levels.MODE == 'HARD':
		level = Levels.Level2()

	while runn:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.VIDEORESIZE:
				last_resize=event.w,event.h
				if event.w>event.h :
					if last_resize[0]>=moniter_size[1]:
						a=moniter_size[1]
						event.w=a
					last_resize=event.w , event.w

				elif(event.h>event.w):
					if last_resize[1]>=moniter_size[1]:
						b=moniter_size[1]
						event.h=b
					last_resize=event.h , event.h

				if event.w<initial_screen_size[0] or event.h < initial_screen_size[1] :
					last_resize=initial_screen_size

				screen_size=last_resize
				resizing=True

				if resizing :
					screen_size=last_resize
					screen=pygame.display.set_mode(screen_size, pygame.RESIZABLE)
					resizing_this_frame=False
					last_resize=None
					startmsg_size_width=startmsg_size[0]
					startmsg_size_height=startmsg_size[1]
					startmsg_x_po=(screen_size[0]/2)-(startmsg_size_width/2)
					startmsg_y_po=(screen_size[1]/3)-(startmsg_size_height/2)

					restartmsg_size_width=restartmsg_size[0]
					restartmsg_size_height=restartmsg_size[1]
					restartmsg_x_po=(screen_size[0]/2)-(restartmsg_size_width/2)
					restartmsg_y_po=(screen_size[1]/1.5)-(restartmsg_size_height/2)

					screen.fill(BLACK)
					screen.blit(startmsg,(startmsg_x_po,startmsg_y_po))
					screen.blit(restartmsg,(restartmsg_x_po,restartmsg_y_po))
					pygame.display.flip()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
					gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
					hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
					food_sprites = loss_food_sprites
					runn=False

				elif event.key == pygame.K_r:
						set_easy_color='WHITE'
						set_hard_color='WHITE'
						main(initialize())
#유령 움직임
def ghost_move(isFeverTime,hero_sprites,ghost_sprites,wall_sprites,gate_sprites,screen):
	for ghost in ghost_sprites:
		if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:#ghost별로 지정된 트랙 인덱스를 나태낸 것. 아래 코드 모두 동일
			ghost.gchangeSpeed(isFeverTime,hero_sprites,ghost_sprites,ghost.tracks[ghost.tracks_loc[0]][0: 2])
			ghost.tracks_loc[1] += 1
		else:
			if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
				ghost.tracks_loc[0] += 1
			elif ghost.role_name == 'Clyde':
				ghost.tracks_loc[0] = 2
			else:
				ghost.tracks_loc[0] = 0
			ghost.gchangeSpeed(isFeverTime,hero_sprites,ghost_sprites,ghost.tracks[ghost.tracks_loc[0]][0: 2])
			ghost.tracks_loc[1] = 0
		if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
			ghost.gchangeSpeed(isFeverTime,hero_sprites,ghost_sprites,ghost.tracks[ghost.tracks_loc[0]][0: 2])
		else:
			if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
				loc0 = ghost.tracks_loc[0] + 1
			elif ghost.role_name == 'Clyde':
				loc0 = 2
			else:
				loc0 = 0
			ghost.gchangeSpeed(isFeverTime,hero_sprites,ghost_sprites,ghost.tracks[loc0][0: 2])
		ghost.update(wall_sprites, gate_sprites)
	ghost_sprites.draw(screen)

def add_rank(id):
	global host
	global port
	global username
	global password
	global database
	global conn
	global curs

	print("유저 점수 : ",user_score)

	sql="insert into test.rank(id,score) values(%s,%s);"
	curs.execute(sql,(id,user_score))
	conn.commit()
	conn.close()

def show_rank(screen,font):
	global host
	global port
	global username
	global password
	global database
	global conn
	global curs
	global set_easy_color , set_hard_color , set_rank_color, WIDTH , HEIGHT,screen_size , moniter_size
	T=True
	ID=[]
	SCORE=[]

	sql = "select*from test.rank"
	df_rank=pd.read_sql(sql,conn)

	"""
+------------+--------------+------+-----+---------+
| Field      | Type         | Null | Key | Default |
+------------+--------------+------+-----+---------+
| ID         | varchar(45)  | NO   | PRI | NULL    |
| SCORE      | INT          | NO   |     | NULL    |
+------------+--------------+------+-----+---------+
	"""

	high_rank=df_rank.sort_values(by=['SCORE'], axis=0,ascending=False)
	high_rank = high_rank.reset_index(drop=True)
	for i in range(0,rank_num):#1위부터 10위까지 출력
		ID.append(high_rank.loc[i][0]) #Dataframe i행의 0번째열(ID)에 userid 저장
		SCORE.append(high_rank.loc[i][1]) #Dataframe i행의 1번째열(SCORE)에 userid 저장

	for i,j in zip(ID,SCORE):
		print("ID : ",i,"  SCORE : ",j)
	positions = [[screen_size[0]/5, screen_size[1]/12*0.5], [screen_size[0]/5, screen_size[1]/12*2]
					,[screen_size[0]/5,screen_size[1]/12*3],[screen_size[0]/5,screen_size[1]/12*4]
					,[screen_size[0]/5,screen_size[1]/12*5],[screen_size[0]/5,screen_size[1]/12*6],
					[screen_size[0]/5,screen_size[1]/12*7],[screen_size[0]/5,screen_size[1]/12*8],
					[screen_size[0]/5,screen_size[1]/12*9],[screen_size[0]/5,screen_size[1]/12*10],
					[screen_size[0]/5,screen_size[1]/12*11]]
	texts=[]
	texts.append(font.render("PRESS ENTER KEY TO BACK MAIN",True,RED))
	for i,j in zip(ID,SCORE):
		texts.append(font.render('ID : %s       SCORE : %s'%(i,j), True, WHITE))
	screen.fill(BLACK)
	for idx, (text, position) in enumerate(zip(texts, positions)):
		screen.blit(text, position)

	notice_msg=gameFont.render("PRESS R KEY TO BACK INITIAL",True,WHITE)
	notice_size=notice_msg.get_rect().size
	notice_size_width=notice_size[0]
	notice_size_height=notice_size[1]
	notice_x_po=(screen_size[0]/2)-(notice_size_width/2)
	notice_y_po=(screen_size[1]/2)-(notice_size_height/2)

	while T:
		for event in pygame.event.get():
			if event.type == pygame.VIDEORESIZE:
				#resizing_this_frame=True
				last_resize=event.w,event.h
				if event.w>event.h :
					if last_resize[0]>=moniter_size[1]:
						a=moniter_size[1]
						event.w=a
					last_resize=event.w , event.w

				elif(event.h>event.w):
					if last_resize[1]>=moniter_size[1]:
						b=moniter_size[1]
						event.h=b
					last_resize=event.h , event.h

				if event.w<initial_screen_size[0] or event.h < initial_screen_size[1] :
					last_resize=initial_screen_size

					#resizing=True
				screen_size=last_resize
				resizing=True
				if resizing :
					screen=pygame.display.set_mode(screen_size , pygame.RESIZABLE )
					resizing=False
					resizing_this_frame=False
					last_resize=None
					screen.blit(notice_msg,(notice_x_po,notice_y_po))
					sql = "select*from test.rank"
					df_rank=pd.read_sql(sql,conn)
					high_rank=df_rank.sort_values(by=['SCORE'], axis=0,ascending=False)
					high_rank = high_rank.reset_index(drop=True)
					for i in range(0,rank_num):
						ID.append(high_rank.loc[i][0])
						SCORE.append(high_rank.loc[i][1])
					for i,j in zip(ID,SCORE):
						print("ID : ",i,"  SCORE : ",j)
					positions = [[screen_size[0]/5, screen_size[1]/12], [screen_size[0]/5, screen_size[1]/12*2]
									,[screen_size[0]/5,screen_size[1]/12*3],[screen_size[0]/5,screen_size[1]/12*4]
									,[screen_size[0]/5,screen_size[1]/12*5],[screen_size[0]/5,screen_size[1]/12*6],
									[screen_size[0]/5,screen_size[1]/12*7],[screen_size[0]/5,screen_size[1]/12*8],
									[screen_size[0]/5,screen_size[1]/12*9],[screen_size[0]/5,screen_size[1]/12*10]]
					texts=[]
					texts.append(font.render("PRESS ENTER KEY TO BACK MAIN",True,RED))
					for i,j in zip(ID,SCORE):
						texts.append(font.render('ID : %s       SCORE : %s'%(i,j), True, WHITE))
					screen.fill(BLACK)
					for idx, (text, position) in enumerate(zip(texts, positions)):
						screen.blit(text, position)
			if event.type == pygame.QUIT:
				sys.exit()
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if  event.key == pygame.K_RETURN:
					set_easy_color='WHITE'
					set_hard_color='WHITE'
					set_rank_color = 'WHITE'
					main(initialize())

		pygame.display.flip()

'''显示文字'''
def showText(screen, font, is_clearance, flag=False):
	global set_easy_color
	global set_hard_color
	global set_rank_color
	save = False
	clock = pygame.time.Clock()
	if not is_clearance:
		if LIFE < LIFE_INIT:
			print(LIFE)
			msg = 'LIFE-1'
			positions = [[screnn_size[0]/2.3, screen_size[1]/2.6], [screen_size[0]/3.78, screen_size[1]/2]] if not is_clearance else [[screen_size[0]/4.18, screen_size[1]/2.6], [screen_size[0]/9.32, screen_size[1]/2]]
			texts=[font.render(msg, True, WHITE),
				   font.render('Press ENTER to continue', True, WHITE)]
		elif LIFE == LIFE_INIT:
			save=True
			msg='Game Over'
			positions = [[screen_size[0]/2.58, screen_size[1]/2.6], [screen_size[0]/9.32, screen_size[1]/2], [screen_size[0]/9.32, screen_size[1]/1.82]] if not is_clearance else [[screen_size[0]/4.18, screen_size[1]/2.6], [screen_size[0]/9.32, screen_size[1]/2], [screen_size[0]/9.32, screen_size[1]/1.82]]
			texts = [font.render(msg, True, WHITE),
				     font.render('Press ENTER to continue or play again.', True, WHITE),
			     	 font.render('Press ESC to quit and save game score.', True, WHITE)]
	elif is_clearance:
		msg = 'Congratulations, you won!'
		positions = [[screen_size[0]/2.75, screen_size[1]/2.6],[screen_size[0]/6.73, screen_size[1]/2], [screen_size[0]/3.36, screen_size[1]/1.82]] if not is_clearance else [[screen_size[0]/2.75, screen_size[1]/2.6],[screen_size[0]/6.73, screen_size[1]/2], [screen_size[0]/3.36, screen_size[1]/1.82]]
		texts = [font.render(msg, True, WHITE),
			     font.render('Press ENTER to play NEXT STAGE', True, WHITE),
		     	 font.render('Press ESC to quit.', True, WHITE)]

	surface = pygame.Surface((show_text_size))
	surface.set_alpha(10) #투명도 설정
	surface.fill(BLACK)
	screen.blit(surface, (screen_size[0]/6, screen_size[1]/3))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					set_easy_color='WHITE'
					set_hard_color='WHITE'
					set_rank_color = 'WHITE'

					if is_clearance:
						if not flag:
							main(initialize())
						else:
							main1(initialize())
					else:
						main1(initialize())
				elif event.key == pygame.K_r:
					show_rank(screen,font)
				elif event.key == pygame.K_ESCAPE and save==True:
					user_id = id_init
					ID_INFO = "Please Enter Your User Name"
					font = pygame.font.Font(None,title_size)
					background = pygame.image.load('resources/images/name.png').convert()
					background =pygame.transform.scale(background,(WIDTH,HEIGHT))
					while True:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.unicode.isalpha():
									user_id+=event.unicode
								elif event.key == pygame.K_BACKSPACE:
									user_id = user_id[:-1] #글자 하나 삭제
								elif event.key == pygame.K_RETURN:
									add_rank(user_id)
									sys.exit()
									pygame.quit()

						screen.fill(BLACK)
						block = [font.render(ID_INFO, True, WHITE),
							     font.render(user_id, True, YELLOW)]
						rect = [block[0].get_rect(),block[1].get_rect()] #block[idx] idx=0 -> ID_INFO_txt ,idx=1 -> get user id
						rect[1].center = screen.get_rect().center
						positions = [[WIDTH/9, HEIGHT/3], rect[1]]
						screen.blit(background,(back_loc))
						for idx,(block,rect) in enumerate(zip(block,positions)):
							screen.blit(block,rect)
						pygame.display.flip()

					if event.type == pygame.K_RETURN:
						sys.exit()
						pygame.quit()

		for idx, (text, position) in enumerate(zip(texts, positions)):
			screen.blit(text, position)
		pygame.display.flip()
		clock.tick(FPS)


'''初始化'''
def initialize():
	global screen_size
	pygame.init()
	icon_image = pygame.image.load(ICONPATH)
	pygame.display.set_icon(icon_image)
	screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
	pygame.display.set_caption('OSSP Ssanhocho pacman')
	return screen


'''主函数'''
def main(screen):
	pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0) #-1 : 게임 종료시까지 음악 반복 의미
	pygame.font.init()
	font_small = pygame.font.Font(FONTPATH, small_font_size)
	font_big = pygame.font.Font(FONTPATH, big_font_size)
	Levels.MODE='EASY'

	if Levels.MODE == 'EASY':
		level = Levels.Level1()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.MODE == 'EASY':
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)


def main1(screen):
	pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0) #-1 : 게임 종료시까지 음악 반복 의미
	pygame.font.init()
	font_small = pygame.font.Font(FONTPATH, small_font_size)
	font_big = pygame.font.Font(FONTPATH, big_font_size)
	Levels.MODE='HARD'

	if Levels.MODE == 'HARD':
		level = Levels.Level2()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.MODE == 'HARD':
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)
\

'''test'''
if __name__ == '__main__':
	main(initialize())
