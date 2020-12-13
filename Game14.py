'''
Function:
	吃豆豆小游戏
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import os, sys ,pygame,Levels,Fever,time,pymysql
import pandas as pd

pygame.init()

<<<<<<< .merge_file_a07088
'''定义一些必要的参数'''
#색 지정
=======
'''定义一些必要的参数(몇가지 주요배개변수 )'''
>>>>>>> .merge_file_a06448
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
#img =pygame.image.load('resources/images/pacman.png')

set_easy_color='WHITE'
set_hard_color='WHITE'
set_rank_color='WHITE'
moniter_size=pygame.display.Info().current_w,pygame.display.Info().current_h

music_on=True

<<<<<<< .merge_file_a07088
gameFont = pygame.font.Font('resources/font/Firenight-Regular.otf',50)

#--------------
#1.타임
TIME_INIT=0.0
startTime=0.0
endTime=0.0
#2.피버
FEVER_TOTAL = 5
FEVER_SCORE = 1000
FEVER_EAT = 50
fever_count = 1
#3.점수
SCORE_INIT=0
<<<<<<< HEAD
SCORE_MUL=30
=======
SCORE_SMALL=30
SCORE_BIG=60
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
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

'''开始某一关游戏'''

def start_scr(screen,color,WHIDTH,HEIGHT):
	easytitle=gameFont.render("EASY",True,color)
	easy_size=easytitle.get_rect().size
	easy_size_width=easy_size[0]
	easy_size_height=easy_size[1]
	easy_x_po=(screen_size[0]/3)-(easy_size_width/2)
	easy_y_po=(HEIGHT/3)-(easy_size_height/2)

	hardtitle=gameFont.render("HARD",True,color)
	hard_size=hardtitle.get_rect().size
	hard_size_width=hard_size[0]
	hard_size_height=hard_size[1]
	hard_x_po=(screen_size[0]/1.5)-(hard_size_width/2)
	hard_y_po=(HEIGHT/3)-(hard_size_height/2)

def pause_scr(screen):
	global screen_size
	startmsg=gameFont.render("PRESS ESC KEY => START",True,WHITE)
	restartmsg=gameFont.render("PRESS R KEY => RESTART",True,WHITE)

	startmsg_size=startmsg.get_rect().size
	startmsg_size_width=startmsg_size[0]
	startmsg_size_height=startmsg_size[1]
	startmsg_x_po=(screen_size[0]/2)-(startmsg_size_width/2)
	startmsg_y_po=(screen_size[1]/3)-(startmsg_size_height/2)
	#screen.blit(startmsg,(startmsg_x_po,startmsg_y_po))

	restartmsg_size=restartmsg.get_rect().size
	restartmsg_size_width=restartmsg_size[0]
	restartmsg_size_height=restartmsg_size[1]
	restartmsg_x_po=(screen_size[0]/2)-(restartmsg_size_width/2)
	restartmsg_y_po=(screen_size[1]/1.5)-(restartmsg_size_height/2)
	#screen.blit(restartmsg,(restartmsg_x_po,restartmsg_y_po))

def restart_screen(screen):
	global set_easy_color
	global set_hard_color
	global screen_size
	runn=True
	resizing=False
	startmsg=gameFont.render("PRESS ESC KEY => START",True,WHITE)
	restartmsg=gameFont.render("PRESS R KEY => RESTART",True,WHITE)

	startmsg_size=startmsg.get_rect().size
	startmsg_size_width=startmsg_size[0]
	startmsg_size_height=startmsg_size[1]
	startmsg_x_po=(screen_size[0]/2)-(startmsg_size_width/2)
	startmsg_y_po=(screen_size[1]/3)-(startmsg_size_height/2)
	#screen.blit(startmsg,(startmsg_x_po,startmsg_y_po))

	restartmsg_size=restartmsg.get_rect().size
	restartmsg_size_width=restartmsg_size[0]
	restartmsg_size_height=restartmsg_size[1]
	restartmsg_x_po=(screen_size[0]/2)-(restartmsg_size_width/2)
	restartmsg_y_po=(screen_size[1]/1.5)-(restartmsg_size_height/2)
	#screen.blit(restartmsg,(restartmsg_x_po,restartmsg_y_po))
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
					print("가로길이",last_resize[0],last_resize[1])

				elif(event.h>event.w):
					if last_resize[1]>=moniter_size[1]:
						b=moniter_size[1]
						event.h=b
					print("hh")
					last_resize=event.h , event.h

				if event.w < initial_screen_size[0] or event.h < initial_screen_size[1] :
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
				if event.key == pygame.K_ESCAPE:
						runn=False

				elif event.key == pygame.K_r:
						set_easy_color='WHITE'
						set_hard_color='WHITE'
						main(initialize())

'''def name(screen):
	global user_id
	user_id = id_init
	ID_INFO = "Please Enter Your User Name"
	font = pygame.font.Font(None,50)
	background = pygame.image.load('resources/images/name.png').convert()
	background =pygame.transform.scale(background,(606,606))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.unicode.isalpha():
					user_id+=event.unicode
				elif event.key == pygame.K_BACKSPACE:
					user_id = user_id[:-1]
				elif event.key == pygame.K_RETURN:
					add_rank(user_id)
					sys.exit()
					pygame.quit()
		screen.fill(BLACK)
		block = [font.render(ID_INFO, True, WHITE),
			     font.render(user_id, True, YELLOW)]
		rect = [block[0].get_rect(),block[1].get_rect()]
		rect[1].center = screen.get_rect().center
		positions = [[70, 233], rect[1]]
		screen.blit(background,(back_loc))
		for idx,(block,rect) in enumerate(zip(block,positions)):
			screen.blit(block,rect)
		pygame.display.flip()'''

def startLevelGame(level, screen, font):

	#변수 불러오기
	global LIFE
	global SCORE
	global STAGE
	global fever_count
	global startTime
	global endTime
	global loss_food_sprites
	global user_score
	global direction
	global screen_size
	global set_easy_color
	global set_hard_color
	global music_on
	global set_rank_color
	global moniter_size

	fever=Fever.Fever()
	#시간표시
	clock = pygame.time.Clock()
	startTime = TIME_INIT
	endTime= TIME_INIT
	start_ticks = pygame.time.get_ticks()

	#그룹지정
	wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
<<<<<<< HEAD
	gate_sprites = level.setupGate(WHITE)
=======
	gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
	food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])
	#total_score = len(food_sprites) * SCORE_MUL * STAGE

	#초기화
	is_clearance = False

	#feverTime
	isFeverTime = False
	is_nextstage=False
	#stage

	direction = DIRECTION_INIT

	#기록
	user_score=SCORE_INIT

	#easy mode
	easytitle=gameFont.render("EASY",True,WHITE)
	clicked_easytitle=gameFont.render("EASY",True,RED)
=======
screen_size=606,606
initial_screen_size=606,606
easy_screen=577,306
img =pygame.image.load('resources/images/pacman.png')

bg = pygame.image.load("resources/images/pm_bg20.png")
set_easy_color='WHITE'
set_hard_color='WHITE'
set_rank_color='WHITE'
moniter_size=pygame.display.Info().current_w,pygame.display.Info().current_h

music_on=True
SCORE = 0

'''set_easy_color='WHITE'
set_hard_color='WHITE'
start_image_ex=pygame.image.load('resources/images/start_button2.png')
start_image=pygame.transform.scale(start_image_ex,((int)(screen_size[0]/5),(int)(HEIGHT/10)))
start_image_size=start_image.get_rect().size
start_image_width=start_image_size[0]
start_image_height=start_image_size[1]
start_x_po=(screen_size[0]/2)-(start_image_width/2)
start_y_po=(screen_size[1]/1.5)-(start_image_height/2)'''


yongFont = pygame.font.Font( 'resources/font/ALGER.TTF',50)

'''easytitle=yongFont.render("EASY",True,WHITE)
clicked_easytitle=yongFont.render("EASY",True,PURPLE)
easy_size=easytitle.get_rect().size
easy_size_width=easy_size[0]
easy_size_height=easy_size[1]
easy_x_po=(screen_size[0]/3)-(easy_size_width/2)
easy_y_po=(screen_size[1]/3)-(easy_size_height/2)

hardtitle=yongFont.render("HARD",True,WHITE)
hard_size=hardtitle.get_rect().size
hard_size_width=hard_size[0]
hard_size_height=hard_size[1]
hard_x_po=(screen_size[0]/1.5)-(hard_size_width/2)
hard_y_po=(screen_size[1]/3)-(hard_size_height/2)
set_color='WHITE'''

'''开始某一关游戏(특정레벨시 )'''
def start_scr(screen,color,WHIDTH,HEIGHT):
	easytitle=yongFont.render("EASY",True,color)
	easy_size=easytitle.get_rect().size
	easy_size_width=easy_size[0]
	easy_size_height=easy_size[1]
	easy_x_po=(screen_size[0]/3)-(easy_size_width/2)
	easy_y_po=(HEIGHT/3)-(easy_size_height/2)

	hardtitle=yongFont.render("HARD",True,color)
	hard_size=hardtitle.get_rect().size
	hard_size_width=hard_size[0]
	hard_size_height=hard_size[1]
	hard_x_po=(screen_size[0]/1.5)-(hard_size_width/2)
	hard_y_po=(HEIGHT/3)-(hard_size_height/2)

	'''screen.blit(background, (0, 0))
	screen.blit(easytitle,(easy_x_po,easy_y_po))
	screen.blit(hardtitle,(hard_x_po,hard_y_po))
	screen.blit(start_image,(start_x_po,start_y_po))
	pygame.display.flip()
	screen.fill(BLACK)'''


def pause_scr(screen):
	global screen_size
	yongFont = pygame.font.Font( None,50)
	yongtitle5=yongFont.render("PRESS ESC KEY => START",True,WHITE)
	yongtitle6=yongFont.render("PRESS R KEY => RESTART",True,WHITE)

	yongtitle5_size=yongtitle5.get_rect().size
	yongtitle5_size_width=yongtitle5_size[0]
	yongtitle5_size_height=yongtitle5_size[1]
	yongtitle5_x_po=(screen_size[0]/2)-(yongtitle5_size_width/2)
	yongtitle5_y_po=(screen_size[1]/3)-(yongtitle5_size_height/2)
	#screen.blit(yongtitle5,(yongtitle5_x_po,yongtitle5_y_po))

	yongtitle6_size=yongtitle6.get_rect().size
	yongtitle6_size_width=yongtitle6_size[0]
	yongtitle6_size_height=yongtitle6_size[1]
	yongtitle6_x_po=(screen_size[0]/2)-(yongtitle6_size_width/2)
	yongtitle6_y_po=(screen_size[1]/1.5)-(yongtitle6_size_height/2)
	#screen.blit(yongtitle6,(yongtitle6_x_po,yongtitle6_y_po))





def restart_screen(screen):
	global set_easy_color
	global set_hard_color
	runn=True
	resizing=False
	global screen_size
	yongFont = pygame.font.Font( None,50)
	yongtitle5=yongFont.render("PRESS ESC KEY => START",True,WHITE)
	yongtitle6=yongFont.render("PRESS R KEY => RESTART",True,WHITE)

	yongtitle5_size=yongtitle5.get_rect().size
	yongtitle5_size_width=yongtitle5_size[0]
	yongtitle5_size_height=yongtitle5_size[1]
	yongtitle5_x_po=(screen_size[0]/2)-(yongtitle5_size_width/2)
	yongtitle5_y_po=(screen_size[1]/3)-(yongtitle5_size_height/2)
	#screen.blit(yongtitle5,(yongtitle5_x_po,yongtitle5_y_po))

	yongtitle6_size=yongtitle6.get_rect().size
	yongtitle6_size_width=yongtitle6_size[0]
	yongtitle6_size_height=yongtitle6_size[1]
	yongtitle6_x_po=(screen_size[0]/2)-(yongtitle6_size_width/2)
	yongtitle6_y_po=(screen_size[1]/1.5)-(yongtitle6_size_height/2)
	#screen.blit(yongtitle6,(yongtitle6_x_po,yongtitle6_y_po))
	screen.fill(BLACK)
	screen.blit(yongtitle5,(yongtitle5_x_po,yongtitle5_y_po))
	screen.blit(yongtitle6,(yongtitle6_x_po,yongtitle6_y_po))
	pygame.display.flip()
	while runn:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.VIDEORESIZE:
				'''last_resize=event.w, event.h
				if screen_size[0]<=last_resize[0] and screen_size[1]<=last_resize[1] :
					screen_size=last_resize
					print(screen_size)
					resizing=True
				else:
					last_resize =screen_size
					screen_size = last_resize
					print(screen_size)
					resizing=True'''
				last_resize=event.w,event.h
				if event.w>event.h :
					if last_resize[0]>=moniter_size[1]:
						a=moniter_size[1]
						event.w=a
					print("gggg")
					last_resize=event.w , event.w

				elif(event.h>event.w):
					if last_resize[1]>=moniter_size[1]:
						b=moniter_size[1]
						event.h=b
					last_resize=event.h , event.h
					print("hhhhh")

				if event.w<initial_screen_size[0] or event.h < initial_screen_size[1] :
					last_resize=initial_screen_size
					print("hi")

					#resizing=True
				screen_size=last_resize
				resizing=True

				if resizing :
					screen_size=last_resize
					screen=pygame.display.set_mode(screen_size, pygame.RESIZABLE | pygame.NOFRAME)
					resizing=False
					resizing_this_frame=False
					last_resize=None
					yongtitle5_size_width=yongtitle5_size[0]
					yongtitle5_size_height=yongtitle5_size[1]
					yongtitle5_x_po=(screen_size[0]/2)-(yongtitle5_size_width/2)
					yongtitle5_y_po=(screen_size[1]/3)-(yongtitle5_size_height/2)

					yongtitle6_size_width=yongtitle6_size[0]
					yongtitle6_size_height=yongtitle6_size[1]
					yongtitle6_x_po=(screen_size[0]/2)-(yongtitle6_size_width/2)
					yongtitle6_y_po=(screen_size[1]/1.5)-(yongtitle6_size_height/2)

					screen.fill(BLACK)
					screen.blit(yongtitle5,(yongtitle5_x_po,yongtitle5_y_po))
					screen.blit(yongtitle6,(yongtitle6_x_po,yongtitle6_y_po))
					pygame.display.flip()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
						runn=False

				elif event.key == pygame.K_r:
						set_easy_color='WHITE'
						set_hard_color='WHITE'
						main(initialize())

def startLevelGame(level, screen, font):
	global screen_size
	global set_easy_color
	global set_hard_color
	global music_on, SCORE
	global set_rank_color
	clock = pygame.time.Clock()
	SCORE = 0
	wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
	gate_sprites = level.setupGate(WHITE)
	hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
	food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])
	is_clearance = False
	is_true=False

	easytitle=yongFont.render("EASY",True,WHITE)
	clicked_easytitle=yongFont.render("EASY",True,RED)
>>>>>>> .merge_file_a06448
	easy_size=easytitle.get_rect().size
	easy_size_width=easy_size[0]
	easy_size_height=easy_size[1]
	easy_x_po=(screen_size[0]/3)-(easy_size_width/2)
	easy_y_po=(screen_size[1]/3)-(easy_size_height/2)
<<<<<<< .merge_file_a07088

	#hard mode
	hardtitle=gameFont.render("HARD",True,WHITE)
	clicked_hardtitle=gameFont.render("HARD",True,RED)
=======
	hardtitle=yongFont.render("HARD",True,WHITE)
	clicked_hardtitle=yongFont.render("HARD",True,RED)
>>>>>>> .merge_file_a06448
	hard_size=hardtitle.get_rect().size
	hard_size_width=hard_size[0]
	hard_size_height=hard_size[1]
	hard_x_po=(screen_size[0]/1.5)-(hard_size_width/2)
	hard_y_po=(screen_size[1]/3)-(hard_size_height/2)

<<<<<<< .merge_file_a07088
	#ranking
	ranktitle = gameFont.render("RANK", True, WHITE)
	clicked_ranktitle = gameFont.render("RANK", True, YELLOW)
=======
	ranktitle = yongFont.render("RANK", True, WHITE)
	clicked_ranktitle = yongFont.render("RANK", True, YELLOW)
>>>>>>> .merge_file_a06448
	rank_size = ranktitle.get_rect().size
	rank_size_width = hard_size[0]
	rank_size_height = hard_size[1]
	rank_x_po = screen_size[0]/2 - rank_size_width/2
	rank_y_po = screen_size[1]/2

<<<<<<< .merge_file_a07088
	#배경
	background=pygame.transform.scale(backgroundimg,screen_size)
	background.set_alpha(200)

	#시작 버튼
	start_image_ex=pygame.image.load('resources/images/start_button.png')
=======
	background=pygame.transform.scale(bg,screen_size)
	background.set_alpha(200)


	start_image_ex=pygame.image.load('resources/images/start_button2.png')
>>>>>>> .merge_file_a06448
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
<<<<<<< .merge_file_a07088

	#게임 진행
	while True:
		#키보드 입력(게임 진행)
		#show_rank(screen,font)
		screen.blit(background,back_loc)
=======
	fullscreen=False
	global moniter_size

	while True:
		screen.blit(background,(0, 0))
>>>>>>> .merge_file_a06448
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
<<<<<<< .merge_file_a07088
<<<<<<< HEAD
=======
				# 음악 일시정지
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
=======
>>>>>>> .merge_file_a06448
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
<<<<<<< .merge_file_a07088
						print("dd")
					last_resize=event.w , event.w
					print(moniter_size[0])
					print("가로",last_resize[0],last_resize[1])
=======
					print("gggg")
					last_resize=event.w , event.w
>>>>>>> .merge_file_a06448

				elif(event.h>event.w):
					if last_resize[1]>=moniter_size[1]:
						b=moniter_size[1]
						event.h=b
					last_resize=event.h , event.h
<<<<<<< .merge_file_a07088
					print("tp로",last_resize[0],last_resize[1])

				if event.w < initial_screen_size[0] or event.h < initial_screen_size[1] :
					last_resize=initial_screen_size

					#resizing=True
				screen_size=last_resize
				print(screen_size)
				resizing=True

				if resizing :
					screen=pygame.display.set_mode(screen_size , pygame.RESIZABLE)
					resizing=False
					resizing_this_frame=False
					last_resize=None
=======
					print("hhhhh")

				if event.w<initial_screen_size[0] or event.h < initial_screen_size[1] :
					last_resize=initial_screen_size
					print("hi")

					#resizing=True
				screen_size=last_resize
				resizing=True

				if resizing :
					screen=pygame.display.set_mode(screen_size , pygame.RESIZABLE | pygame.NOFRAME)
					resizing=False
					resizing_this_frame=False
					last_resize=None

>>>>>>> .merge_file_a06448
					if set_easy_color == 'RED' and set_hard_color == 'WHITE':
						main(initialize())
					elif set_easy_color == 'WHITE' and set_hard_color =='RED' :
						main1(initialize())
					else :main(initialize())

			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type == pygame.MOUSEMOTION:
				if pygame.mouse.get_pos()[0] >= easy_x_po and pygame.mouse.get_pos()[0] <= easy_x_po+easy_size_width and pygame.mouse.get_pos()[1] >= easy_y_po and pygame.mouse.get_pos()[1] <= easy_y_po+easy_size_height:
<<<<<<< .merge_file_a07088
					easytitle=gameFont.render("EASY",True,RED)
				elif pygame.mouse.get_pos()[0] >= hard_x_po and pygame.mouse.get_pos()[0] <= hard_x_po+hard_size_width and pygame.mouse.get_pos()[1] >= hard_y_po and pygame.mouse.get_pos()[1] <= hard_y_po+hard_size_height:
					hardtitle=gameFont.render("HARD",True,RED)
				elif rank_x_po <= pygame.mouse.get_pos()[0] <= rank_x_po+rank_size_width and rank_y_po <= pygame.mouse.get_pos()[1] <= rank_y_po+rank_size_height:
					ranktitle = gameFont.render("RANK", True, YELLOW)
				else:
					easytitle=gameFont.render("EASY",True,WHITE)
					hardtitle=gameFont.render("HARD",True,WHITE)
					ranktitle = gameFont.render("RANK", True, WHITE)
=======
					easytitle=yongFont.render("EASY",True,RED)
				elif pygame.mouse.get_pos()[0] >= hard_x_po and pygame.mouse.get_pos()[0] <= hard_x_po+hard_size_width and pygame.mouse.get_pos()[1] >= hard_y_po and pygame.mouse.get_pos()[1] <= hard_y_po+hard_size_height:
					hardtitle=yongFont.render("HARD",True,RED)
				elif rank_x_po <= pygame.mouse.get_pos()[0] <= rank_x_po+rank_size_width and rank_y_po <= pygame.mouse.get_pos()[1] <= rank_y_po+rank_size_height:
					ranktitle = yongFont.render("RANK", True, YELLOW)
				else:
					easytitle=yongFont.render("EASY",True,WHITE)
					hardtitle=yongFont.render("HARD",True,WHITE)
					ranktitle = yongFont.render("RANK", True, WHITE)
>>>>>>> .merge_file_a06448
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
<<<<<<< .merge_file_a07088
					show_rank(screen,font)

				if start_x_po <= pygame.mouse.get_pos()[0] <= start_x_po+start_image_width and start_y_po <= pygame.mouse.get_pos()[1] <= start_y_po+start_image_height:
					is_true = True
					while is_true:

						if LIFE>=1 and LIFE<LIFE_INIT and is_nextstage==False :
							food_sprites = loss_food_sprites

=======


				if start_x_po <= pygame.mouse.get_pos()[0] <= start_x_po+start_image_width and start_y_po <= pygame.mouse.get_pos()[1] <= start_y_po+start_image_height:
					ff=True
					while ff:
>>>>>>> .merge_file_a06448
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
<<<<<<< .merge_file_a07088
=======
									print("gggg")
>>>>>>> .merge_file_a06448
									last_resize=event.w , event.w

								elif(event.h>event.w):
									if last_resize[1]>=moniter_size[1]:
										b=moniter_size[1]
										event.h=b
									last_resize=event.h , event.h
<<<<<<< .merge_file_a07088

								if event.w<initial_screen_size[0] or event.h < initial_screen_size[1] :
									last_resize=initial_screen_size
=======
									print("hhhhh")

								if event.w<initial_screen_size[0] or event.h < initial_screen_size[1] :
									last_resize=initial_screen_size
									print("hi")
>>>>>>> .merge_file_a06448

									#resizing=True
								screen_size=last_resize
								resizing=True
<<<<<<< .merge_file_a07088

								if resizing :
									screen_size=last_resize
									screen=pygame.display.set_mode(screen_size, pygame.RESIZABLE)
									resizing=False
									resizing_this_frame=False
									last_resize=None
									wall_sprites = level.setupWalls(SKYBLUE,screen_size[0],screen_size[1])
<<<<<<< HEAD
									for hero in hero_sprites:
										hero.base_image = pygame.transform.scale(hero.base_image, (80,80))
										hero.image = hero.base_image.copy()
									food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])
=======
									gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
									food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])
									hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
									for ghost in ghost_sprites:
										if pygame.sprite.spritecollide(ghost, hero_sprites, True):
											ghost.rect.left = x_prev
											ghost.rect.top = y_prev
									#pygame.transform.scale(self.base_image,(31,31))
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc

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
										#여기 제시작
									 	restart_screen(screen)
								elif event.type == pygame.QUIT:
									sys.exit()
									pygame.quit()

							if event.type == pygame.KEYUP:
									if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
										hero.pchangeSpeed(isFeverTime,direction)
										hero.is_move = is_true


		#게임 승리(아이템 소진)
						if len(food_sprites) == 0:
							is_clearance = True
							SCORE=SCORE
							LIFE=LIFE
							STAGE+=1
							is_nextstage=True
							direction=DIRECTION_INIT
								#break
							wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
<<<<<<< HEAD
							gate_sprites = level.setupGate(WHITE)
=======
							gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
							hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
							food_sprites = level.setupFood(YELLOW, WHITE, screen_size[0], screen_size[1])

				        #피버타임
						if SCORE > (fever_count*FEVER_SCORE) and isFeverTime == False:#1000점 단위
							isFeverTime = True#1000점의 배수일 때 마다 fever모드 on
							fever_count += 1
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
							if LIFE<=1:
								user_score = SCORE
								SCORE = SCORE_INIT
								LIFE=LIFE_INIT
								fever_count = 1
								is_clearance = False
								is_nextstage = False
								STAGE=STAGE_INIT
								print("유저 점수",user_score)
								break
							else:
								LIFE -=  1
								SCORE = SCORE
								loss_food_sprites = food_sprites
								STAGE=STAGE
								is_clearance=False
								is_nextstage=False
								wall_sprites = level.setupWalls(SKYBLUE, screen_size[0], screen_size[1])
<<<<<<< HEAD
								gate_sprites = level.setupGate(WHITE)
=======
								gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
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
<<<<<<< HEAD
						SCORE += SCORE_MUL*len(food_eaten)
=======
						for food in food_eaten:
							# food.width == screen_size[0]/40, screen_size[0]/30 : 큰아이템
							if food.width == screen_size[0]/40 or food.width == screen_size[0]/30:
								SCORE += SCORE_BIG
							# 작은아이템
							else:
								SCORE += SCORE_SMALL
						#SCORE += SCORE_MUL*len(food_eaten)
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
						if isFeverTime == True and pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
							SCORE += FEVER_EAT
						wall_sprites.draw(screen)
						gate_sprites.draw(screen)
						food_sprites.draw(screen)

						#피버 타이머
						if isFeverTime==True:
							elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
				    		# 피버 타이머
							timer = font.render("FEVER Timer: " + str(int(FEVER_TOTAL - elapsed_time)), True, WHITE)
					    	#피버 경과 시간 표시
							screen.blit(timer,TIMER_INFO)

						ghost_move(isFeverTime,hero_sprites,ghost_sprites,wall_sprites,screen)

						#피버타임 그리기
						if isFeverTime == True:
							fever_text = pygame.image.load('resources/images/bomb.png').convert()
							#fever_text = font.render("FEVER", True, PURPLE)
							fV_txt_img= pygame.transform.scale(fever_text,(140,46))
							if Levels.MODE=='EASY':
								screen.blit(fV_txt_img, FEVER_INFO)
							elif Levels.MODE=='HARD':
								screen.blit(fV_txt_img, GATE_MID_H)

						#상단바 그리기
						score_text = font.render("Score: %s    %s Mode    LIFE : %s" % (SCORE,Levels.MODE,LIFE), True, WHITE)
						screen.blit(score_text, INFO)

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
	#screen.blit(startmsg,(startmsg_x_po,startmsg_y_po))

	restartmsg_size=restartmsg.get_rect().size
	restartmsg_size_width=restartmsg_size[0]
	restartmsg_size_height=restartmsg_size[1]
	restartmsg_x_po=(screen_size[0]/2)-(restartmsg_size_width/2)
	restartmsg_y_po=(screen_size[1]/1.5)-(restartmsg_size_height/2)
	#screen.blit(restartmsg,(restartmsg_x_po,restartmsg_y_po))
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

					#resizing=True
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
<<<<<<< HEAD
					gate_sprites = level.setupGate(WHITE)
=======
					gate_sprites = level.setupGate(WHITE, screen_size[0], screen_size[1])
>>>>>>> 8ba7fb378c5453721f6bf8fcca6c67e537f096dc
					hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH],screen_size[0],screen_size[1])
					food_sprites = loss_food_sprites
					runn=False

				elif event.key == pygame.K_r:
						set_easy_color='WHITE'
						set_hard_color='WHITE'
						main(initialize())
#유령 움직임
def ghost_move(isFeverTime,hero_sprites,ghost_sprites,wall_sprites,screen):
	for ghost in ghost_sprites:
		if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
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
		ghost.update(wall_sprites, None)
	ghost_sprites.draw(screen)
=======
>>>>>>> .merge_file_a06448

def add_rank(id):
	global host
	global port
	global username
	global password
	global database
	global conn
	global curs

	print("유저 점수요",user_score)
	#conn = pymysql.connect(host=host,port=port,user=username,passwd=password,db=database,charset='utf8')
	#curs=conn.cursor()
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
	high_rank=df_rank.sort_values(by=['SCORE'], axis=0,ascending=False)
	high_rank = high_rank.reset_index(drop=True)
	for i in range (0,10):
		ID.append(high_rank.loc[i][0])
		SCORE.append(high_rank.loc[i][1])

	for i,j in zip(ID,SCORE):
		print("ID : ",i,"  SCORE : ",j)
	positions = [[WIDTH/6, 60], [100, 110],[100,160],[100,210],[100,260],[100,310],[100,360],[100,410],[100,460],[100,510]]
	texts=[]
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
					for i in range (0,10):
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

		'''for idx, (text, position) in enumerate(zip(texts, positions)):
			screen.blit(text, position)'''
		pygame.display.flip()

								if resizing :
									screen_size=last_resize
									screen=pygame.display.set_mode(screen_size, pygame.RESIZABLE)
									resizing=False
									resizing_this_frame=False
									last_resize=None
									wall_sprites = level.setupWalls(SKYBLUE,screen_size[0],screen_size[1])
									for hero in hero_sprites:
										hero.base_image = pygame.transform.scale(hero.base_image, (80,80))
										hero.image = hero.base_image.copy()
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
						for food in food_eaten:
							if food.width==screen_size[0]/40:
								SCORE+=50
							else:
								SCORE+=10
						wall_sprites.draw(screen)
						gate_sprites.draw(screen)
						food_sprites.draw(screen)
						for ghost in ghost_sprites:
							# 幽灵随机运动(效果不好且有BUG) 유령 무작위 이(나쁜효과 및버그)

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

	'''	if resizing :
			screen_size=last_resize
			screen=pygame.display.set_mode(screen_size, pygame.RESIZABLE)
			resizing=False
			resizing_this_frame=False
			last_resize=None
			print(screen_size)'''

'''显示文字텍스트 이름?'''
def showText(screen, font, is_clearance, flag=False):
	save = False
	clock = pygame.time.Clock()
	if not is_clearance:
		if LIFE<LIFE_INIT:
			print(LIFE)
			msg = 'LIFE-1'
			positions = [[260, 233], [160, 303]] if not is_clearance else [[145, 233], [65, 303]]
			texts=[font.render(msg, True, WHITE),
				   font.render('Press ENTER to continue', True, WHITE)]
		elif LIFE==LIFE_INIT:
			save=True
			msg='Game Over'
			positions = [[235, 233], [65, 303], [65, 333]] if not is_clearance else [[145, 233], [65, 303], [65, 333]]
			texts = [font.render(msg, True, WHITE),
				     font.render('Press ENTER to continue or play again.', True, WHITE),
			     	 font.render('Press ESC to quit and save game score.', True, WHITE)]
	elif is_clearance:
		msg = 'Congratulations, you won!'
		positions = [[220, 233], [90, 303], [180, 333]] if not is_clearance else [[130, 233], [90, 303], [180, 333]]
		texts = [font.render(msg, True, WHITE),
			     font.render('Press ENTER to play NEXT STAGE', True, WHITE),
		     	 font.render('Press ESC to quit.', True, WHITE)]

	surface = pygame.Surface((400, 200))
	surface.set_alpha(10)#투명
	surface.fill((128, 128, 128))
	screen.blit(surface, (100, 200))
<<<<<<< .merge_file_a07088
=======
	texts = [font.render(msg, True, WHITE),
			 font.render('Press ENTER to continue or play again.', True, WHITE),
			 font.render('Press ESCAPE to quit.', True, WHITE)]


>>>>>>> .merge_file_a06448

	while True:
		for idx, (text, position) in enumerate(zip(texts, positions)):
			screen.blit(text, position)
		pygame.display.flip()
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if is_clearance:
						if not flag:
<<<<<<< .merge_file_a07088
							main(initialize())
=======
							return
>>>>>>> .merge_file_a06448
						else:
							main1(initialize())
					else:
						main1(initialize())
<<<<<<< .merge_file_a07088
				elif event.key == pygame.K_r:
					show_rank(screen,font)
				elif event.key == pygame.K_ESCAPE and save==True:
					user_id = id_init
					ID_INFO = "Please Enter Your User Name"
					font = pygame.font.Font(None,50)
					background = pygame.image.load('resources/images/name.png').convert()
					background =pygame.transform.scale(background,(606,606))
					while True:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.unicode.isalpha():
									user_id+=event.unicode
								elif event.key == pygame.K_BACKSPACE:
									user_id = user_id[:-1]
								elif event.key == pygame.K_RETURN:
									add_rank(user_id)
									sys.exit()
									pygame.quit()
						screen.fill(BLACK)
						block = [font.render(ID_INFO, True, WHITE),
							     font.render(user_id, True, YELLOW)]
						rect = [block[0].get_rect(),block[1].get_rect()]
						rect[1].center = screen.get_rect().center
						positions = [[70, 233], rect[1]]
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
		clock.tick(60)
=======
				elif event.key == pygame.K_ESCAPE:
					sys.exit()
					pygame.quit()






		'''for idx, (text, position) in enumerate(zip(texts, positions)):
			screen.blit(text, position)
		pygame.display.flip()
		clock.tick(10)'''
>>>>>>> .merge_file_a06448


'''初始化(초기)'''
def initialize():
	global screen_size
	pygame.init()
	global screen_size
	icon_image = pygame.image.load(ICONPATH)
	pygame.display.set_icon(icon_image)
	screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
<<<<<<< .merge_file_a07088
	pygame.display.set_caption('OSSP Ssanhocho pacman')
=======

	pygame.display.set_caption('Pacman-微信公众号Charles的皮卡丘')
>>>>>>> .merge_file_a06448
	return screen


'''主函数(주요기)'''
def main(screen):
	'''pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)'''
	pygame.font.init()
<<<<<<< .merge_file_a07088
	font_small = pygame.font.Font(FONTPATH, 24)
	font_big = pygame.font.Font(FONTPATH, 30)
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
	pygame.mixer.music.play(-1, 0.0)
	pygame.font.init()
	font_small = pygame.font.Font(FONTPATH, 24)
	font_big = pygame.font.Font(FONTPATH, 30)
	Levels.MODE='HARD'
=======
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
>>>>>>> .merge_file_a06448

	if Levels.MODE == 'HARD':
		level = Levels.Level2()
		is_clearance = startLevelGame(level, screen, font_small)
		if Levels.MODE == 'HARD':
			showText(screen, font_big, is_clearance, True)
		else:
			showText(screen, font_big, is_clearance)
\

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
