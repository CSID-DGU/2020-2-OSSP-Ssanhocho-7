# EASY version setupFood
def setupFood_easy(self, food_color, bg_color):
    self.food_sprites = pygame.sprite.Group()
    for row in range(9):
        for col in range(18):
            if (row == 3 or row == 4) and (col == 7 or col == 8 or col == 9 or col == 10):
                continue
            else:
                if ((row == 1 or row == 8) and (col == 0 or col == 18)) or ((row == 2 or row == 5) and (col == 0 or col == 3 or col == 15)):
                    food = Food(30*col+23, 30*row+23, 20, 20, food_color, bg_color)
                else:
                    food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
            is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
            if is_collide:
                continue
            is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
            if is_collide:
                continue
            self.food_sprites.add(food)
    return self.food_sprites

# HARD version setupFood
def setupFood_hard(self, food_color, bg_color):
    self.food_sprites = pygame.sprite.Group()
    for row in range(19):
        for col in range(19):
            if (row == 7 or row == 8) and (col == 7 or col == 8 or col == 9 or col == 10 or col == 11):
                continue
            else:
                if ((row == 1 or row == 14) and (col == 0 or col == 18)) or ((row == 2 or row == 10) and (col == 0 or col == 3 or col == 10)):
                    food = Food(30*col+23, 30*row+23, 20, 20, food_color, bg_color)
                else:
                    food = Food(30*col+32, 30*row+32, 4, 4, food_color, bg_color)
            is_collide = pygame.sprite.spritecollide(food, self.wall_sprites, False)
            if is_collide:
                continue
            is_collide = pygame.sprite.spritecollide(food, self.hero_sprites, False)
            if is_collide:
                continue
            self.food_sprites.add(food)
    return self.food_sprites
