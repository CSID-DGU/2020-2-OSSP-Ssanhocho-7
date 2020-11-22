import os
import sys
import pygame
import Levels
import random

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
FONTPATH = os.path.join(os.getcwd(), 'resources/font/Firenight-Regular.otf')
HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), 'resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), 'resources/images/Pinky.png')

HEIGHT = 606
WIDTH = 606

f1 = True

# 음악 일시정지 기능
music_on = True

INTRO = [["EASY MODE", 0], ["HARD MODE", 0], ["VIEW RANKING", 0], ["QUIT", 0]]

"""
def load_image(name):
    fullname = os.path.join(os.getcwd(), )
	image = pygame.image.load(fullname)
	return image
	"""

"""
class StartScreen:
	def __init__(self):
		global INTRO
		image = os.path.join(os.getcwd(), 'resources/images/start_screen.png')
		image = pygame.image.load(image)
"""


def print_text(screen):
	"""
	시작화면 텍스트 출력
	"""
	for i in range(len(INTRO)):
		if INTRO[i][1] == 0:
			color = pygame.Color(WHITE)
		font = pygame.font.Font(FONTPATH, 20)
		text = font.render(INTRO[i][0], 1, (color))
		start_x = WIDTH // 2 - text.get_width() // 2
		start_y = HEIGHT // 2 - text.get_height() // 2 - 20
		text_x = start_x
		text_y = start_y + i * 60
		screen.blit(text, (text_x, text_y))

def startLevelGame(level, screen, font):
	global music_on

	clock = pygame.time.Clock()
	SCORE = 0
	wall_sprites = level.setupWalls_easy(SKYBLUE)
	gate_sprites = level.setupGate_easy(RED)
	hero_sprites, ghost_sprites = level.setupPlayers_easy(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites = level.setupFood_easy(YELLOW, WHITE)
	is_clearance = False

	while True:
		for i in range(len(INTRO)):
			if INTRO[i][1] == 0:
				color = pygame.Color(WHITE)
			font = pygame.font.Font(FONTPATH, 20)
			text = font.render(INTRO[i][0], 1, (color))
			start_x = WIDTH // 2 - text.get_width() // 2
			start_y = HEIGHT // 2 - text.get_height() // 2 - 20
			text_x = start_x
			text_y = start_y + i * 60
			pygame.display.flip()
			screen.fill(BLACK)
			screen.blit(text, (text_x, text_y))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(-1)
				pygame.quit()

			if event.type == pygame.KEYDOWN:

				"""
				음악 정지
				"""
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
			'''if event.type == pygame.KEYUP:
				if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
					hero.is_move = False'''
		screen.fill(BLACK)
		for hero in hero_sprites:
			hero.update(wall_sprites, gate_sprites)
		hero_sprites.draw(screen)
		for hero in hero_sprites:
			food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
		SCORE += len(food_eaten) * 10
		wall_sprites.draw(screen)
		gate_sprites.draw(screen)
		food_sprites.draw(screen)

		for ghost in ghost_sprites:
			# ghost_sprites = [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH
			# 유령 이동경로 랜덤 ( 버그 있음 )
			'''
			res = ghost.update(wall_sprites, None)
			while not res:
				ghost.changeSpeed(ghost.randomDirection())
				res = ghost.update(wall_sprites, None)
			'''
			# 유령 이동경로 지정
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
			# main(initialize())
			break
		if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
			is_clearance = False
			break
		pygame.display.flip()
		clock.tick(10)
	return is_clearance


'''디스플레이'''
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


'''초기화'''
def initialize():
	pygame.init()
	icon_image = pygame.image.load(ICONPATH)
	pygame.display.set_icon(icon_image)
	screen_hard = pygame.display.set_mode([606, 606])
	screen_easy = pygame.display.set_mode([576, 306])
	pygame.display.set_caption('산호초조_PACMAN HARD')
	screen = screen_easy
	return screen


'''메인함수'''
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
		"""
		elif num_level == 2:
			level = Levels.Level2()
			is_clearance = startLevelGame(level, screen, font_small)
			if num_level == Levels.NUMLEVELS:
				showText(screen, font_big, is_clearance, True)
			else:
				showText(screen, font_big, is_clearance)
		"""

'''test'''
if __name__ == '__main__':
	main(initialize())
