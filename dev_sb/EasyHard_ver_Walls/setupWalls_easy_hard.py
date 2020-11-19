def setupWalls_easy(self, wall_color):
    self.wall_sprites = pygame.sprite.Group()
    wall_positions = [[0, 0, 6, 306], # 맨 왼쪽
                      [0, 0, 576, 6], # 맨 위쪽
                      [0, 300, 576, 6], # 맨 아래쪽
                      [570, 0, 6, 306], # 맨 오른쪽
                      [150, 0, 6, 66], # 맨 위 왼쪽 |
                      [420, 0, 6, 66], # 맨 위 오른쪽 |
                      [210, 60, 154, 6], # ghost zone 위 가운데 -----
                      [60, 60, 36, 6], [60, 60, 6, 66], # 맨 위 왼쪽 ㄱ자 좌우반전한것
                      [480, 60, 36, 6], [510, 60, 6, 66], # 맨 위 오른쪽 ㄱ자 좌우반전한것
                      [120, 120, 36, 6], [420, 120, 36, 6], [120, 180, 36, 6], [420, 180, 36, 6], # 조그마한 - 4개
                      [60, 240, 36, 6], [60, 180, 6, 66], # 아래 왼쪽 L자
                      [480, 240, 36, 6], [510, 180, 6, 66], # 아래 오른쪽 L자 좌우반전한것
                      [150, 240, 6, 66], # 맨 아래 왼쪽 |
                      [420, 240, 6, 66], # 맨 아래 오른쪽 |
                      [210, 240, 154, 6], # ghost zone 아래 가운데 -----
                      [210, 120, 36, 6], # ghost zone start
                      [210, 120, 6, 66],
                      [210, 180, 154, 6],
                      [330, 120, 36, 6],
                      [360, 120, 6, 66], # ghost zone fin
                      ]
    for wall_position in wall_positions:
        wall = Wall(*wall_position, wall_color)
        self.wall_sprites.add(wall)
    return self.wall_sprites


def setupWalls_hard(self, wall_color):
    self.wall_sprites = pygame.sprite.Group()
    wall_positions = [[0, 0, 6, 600], # 외벽
                      [0, 0, 600, 6],
                      [0, 600, 606, 6],
                      [600, 0, 6, 606],
                      [210, 240, 66, 6], # ghost zone start
                      [210, 240, 6, 66],
                      [210, 300, 184, 6],
                      [330, 240, 66, 6],
                      [390, 240, 6, 66], # ghost zone fin
                      [240, 0, 6, 66], # 맨 위 왼쪽 |
                      [360, 0, 6, 66], # 맨 위 오른쪽 |
                      [60, 60, 124, 6], [60, 60, 6, 36], # 맨 위 왼쪽 ㄱ자 좌우반전한것
                      [420, 60, 124, 6], [540, 60, 6, 36], # 맨 위 오른쪽 ㄱ자 좌우반전한것
                      [300, 60, 6, 66], # 맨 위 두번째 가운데 |
                      [180, 120, 66, 6], # 맨 위 두번째 왼쪽  -
                      [360, 120, 66, 6],  # 맨 위 두번째 오른쪽  -
                      [0, 150, 66, 6], # 맨 왼쪽 외벽쪽 -
                      [540, 150, 66, 6], # 맨 오른쪽 외벽쪽 -
                      [120, 120, 6, 66], [120, 180, 36, 6], # 맨 위 왼쪽 L자
                      [480, 120, 6, 66], [450, 180, 36, 6], # 맨 위 오른쪽 L자 좌우반전
                      [210, 180, 184, 6], # ghost zone 위 가운데 -----
                      [60, 210, 6, 36], [60, 240, 36, 6], # ghost zone 왼쪽 조그만 ㄴ자
                      [540, 210, 6, 36], [510, 240, 36, 6], # ghost zone 왼쪽 조그만 ㄴ자
                      [150, 240, 6, 66], [120, 300, 36, 6], # 맨 위 왼쪽 L자
                      [450, 240, 6, 66], [450, 300, 36, 6], # 맨 위 오른쪽 L자 좌우반전
                      [60, 300, 6, 66], [60, 360, 36, 6], # 맨 위 왼쪽 L자
                      [540, 300, 6, 66], [510, 360, 36, 6], # 맨 위 오른쪽 L자 좌우반전
                      [150, 360, 6, 66], [150, 360, 96, 6], # 맨 위 왼쪽 L자
                      [360, 360, 96, 6], [450, 360, 6, 66], # 맨 위 오른쪽 L자 좌우반전
                      [300, 360, 6, 66], [210, 420, 184, 6], # 밑에서 두번째 ㅗ자
                      [300, 480, 6, 66], [210, 540, 184, 6], # 맨 밑 ㅗ 자
                      [0, 420, 36, 6], # 맨 왼쪽 외벽쪽 -
                      [570, 420, 36, 6], # 맨 오른쪽 외벽쪽 -
                      [90, 420, 6, 66], [60, 480, 36, 6], # 맨 위 왼쪽 L자
                      [510, 420, 6, 66], [510, 480, 36, 6], # 맨 위 오른쪽 L자 좌우반전
                      [60, 540, 36, 6], # 맨 아래 왼쪽  -
                      [510, 540, 36, 6], # 맨 아래 오른쪽  -
                      [150, 480, 6, 120], [150, 480, 96, 6], # 맨 아래 ㅗ자 감싸는 박스 왼쪽
                      [360, 480, 96, 6], [450, 480, 6, 120] # 맨 아래 ㅗ자 감싸는 박스 오른쪽
                      ]
    for wall_position in wall_positions:
        wall = Wall(*wall_position, wall_color)
        self.wall_sprites.add(wall)
    return self.wall_sprites


    # 문 만들기
	def setupGate_easy(self, gate_color):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(246, 122, 84, 2, gate_color))
		return self.gate_sprites


	def setupGate_hard(self, gate_color):
		self.gate_sprites = pygame.sprite.Group()
		self.gate_sprites.add(Wall(276, 242, 54, 2, gate_color))
		return self.gate_sprites
