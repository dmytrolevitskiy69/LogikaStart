# from moviepy import VideoFileClip
#import pygame
#pygame.init()
# pygame.display.set_caption('Showing Cutscene..')
# video = VideoFileClip('cutscene.mp4')
# video.preview()
# Якраз ось цей фрагментик я пробував зробити катсцену, але не находить файл. я виокирстовував PIP manager moviepy


from pygame import *
from random import randint
mixer.init()
goal = 50
fire_sound = mixer.Sound('fire.mp3')
img_hero="player.png"
img_back="background.png"
img_enemy="enemy.png"
img_bullet="bullet.png"
img_winner="win_screen.png"
img_loser="loose_screen.png"
win_width = 700
win_height = 700




# шрифти і написи
font.init()
font1 = font.Font("norwester.otf", 100)
font2 = font.Font("norwester.otf", 40)
font3 = font.Font("norwester.otf", 20)
font4 = font.Font("norwester.otf", 105)
win = font1.render('You Won!', True, (255, 255, 255))
lose = font1.render('Game Over.', True, (255,255,255))
window = display.set_mode((win_width, win_height))
display.set_caption("Defenders")
background = transform.scale(image.load("background.png"), (win_width, win_height))
img_loser = transform.scale(image.load("loose_screen.png"), (win_width, win_height))
img_winner = transform.scale(image.load("win_screen.png"), (win_width, win_height))
img_title = transform.scale(image.load("title.png"), (win_width, win_height))
def show_start_sreeen():
      start = True
      small_font = font.Font("norwester.otf", 30)
    
      while start:
        play_button = Rect(300, 300, 100, 50)
        for e in event.get():
            if e.type == QUIT:
                start = False
            if e.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = mouse.get_pos()
                if play_button.collidepoint(mouse_x, mouse_y):
                    start = False

        window.blit(img_title, (0,0))
        text = font4.render('DEFENDERS', True, (255,255,255))
        play_text = small_font.render('Play', True, (255,255,255))
        window.blit(text, (350 - text.get_width() // 2, 200))
        draw.rect(window, (0, 0, 0), play_button)
        window.blit(play_text, (350 - play_text.get_width() // 2, 325 - play_text.get_height() // 2))
        display.update()
show_start_sreeen()
mixer.music.load('flying battery alt.wav')
mixer.music.play()
clock = time.Clock()
FPS=60
score = 0  # вбито
lost = 0  # пропущено
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        #властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        #rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.direction = 'up'  # Початковий напрямок (вгору)

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.image = transform.rotate(transform.scale(image.load(img_hero), (80, 80)), 90)
            self.direction = 'left'
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            self.image = transform.rotate(transform.scale(image.load(img_hero), (80, 80)), -90)
            self.direction = 'right'
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            self.image = transform.scale(image.load(img_hero), (80, 80))
            self.direction = 'up'
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
            self.image = transform.rotate(transform.scale(image.load(img_hero), (80, 80)), 180)
            self.direction = 'down'

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.centery, 10, 10, self.direction)
        bullets.add(bullet)
        fire_sound.play()

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, direction):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.direction = direction
        if self.direction == 'top':
            self.image = transform.rotate(self.image, 0)
        elif self.direction == 'left':
            self.image = transform.rotate(self.image, 90)
        elif self.direction == 'right':
            self.image = transform.rotate(self.image, -90)
        elif self.direction == 'bottom':
            self.image = transform.rotate(self.image, 180)

    def update(self):
        global lost
        if self.direction == 'top':
            self.rect.y += self.speed
            if self.rect.y > win_height:
                self.reset_position()
        elif self.direction == 'left':
            self.rect.x += self.speed
            if self.rect.x > win_width:
                self.reset_position()
        elif self.direction == 'right':
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.reset_position()
        elif self.direction == 'bottom':
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.reset_position()

    def reset_position(self):
        global lost
        side = randint(1, 4)
        if side == 1:
            self.rect.x = randint(90, win_width - 80)
            self.rect.y = -80
            self.direction = 'top'
        elif side == 2:
            self.rect.x = -80
            self.rect.y = randint(80, win_height - 80)
            self.direction = 'left'
            self.image = transform.rotate(transform.scale(image.load(img_enemy), (80, 80)), 90)
        elif side == 3:
            self.rect.x = win_width + 80
            self.rect.y = randint(80, win_height - 80)
            self.direction = 'right'    
            self.image = transform.rotate(transform.scale(image.load(img_enemy), (80, 80)), -90)
        elif side == 4:
            self.rect.x = randint(80, win_width -80)
            self.rect.y = win_height + 80
            self.direction = 'bottom'
            self.image = transform.rotate(transform.scale(image.load(img_enemy), (80, 80)), 180)
        lost += 1

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, direction):
        super().__init__(player_image, player_x, player_y, size_x, size_y, 20)
        self.direction = direction

        if self.direction == 'up':
            self.image = transform.rotate(self.image, 0)
        elif self.direction == 'left':
            self.image = transform.rotate(self.image, 90)
        elif self.direction == 'right':
            self.image = transform.rotate(self.image, -90)
        elif self.direction == 'down':
            self.image = transform.rotate(self.image, 180)

    def update(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        if self.rect.bottom < 0 or self.rect.top > win_height or self.rect.right < 0 or self.rect.left > win_width:
            self.kill()
ship=Player(img_hero,300,300,80,80,8)   
monsters = sprite.Group()
bullets =sprite.Group()

for i in range(1,6):
    side = randint(1, 4)

    if side == 1:
        x = randint(80, win_width -80)
        y = -80
        direction = 'top'
    elif side == 2:
        x = -80
        y = randint(80, win_height -80)
        direction = 'left'
    elif side == 3:
        x = win_width + 80
        y = randint(80, win_height -80)
        direction = 'right'
    elif side == 4:
        x = randint(80, win_width - 80)
        y = win_height + 80
        direction = 'bottom'

    monster = Enemy(img_enemy, x, y, 80, 80, randint(2, 3), direction)
    monsters.add(monster)

finish=False
run=True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key==K_SPACE: 
                fire_sound.play()
                ship.fire()


    if not finish:
        window.blit(background,(0, 0))
        ship.update()
        ship.reset()
        monsters.update()
        monsters.draw(window)
        bullets.draw(window)
        bullets.update()
        
        collides=sprite.groupcollide(monsters,bullets,True,True)
        for c in collides:
            score +=1
            side = randint(1, 4)
            if side == 1:
                x = randint(80, win_width -80)
                y = -80
                direction = 'top'
            elif side == 2:
                x = -80
                y = randint(80, win_height -80)
                direction = 'left'
            elif side == 3:
                x = win_width + 80
                y = randint(80, win_height -80)
                direction = 'right'
            elif side == 4:
                x = randint(80, win_width - 80)
                y = win_height + 80
                direction = 'bottom'

            monster = Enemy(img_enemy, x, y, 80, 80, randint(2, 3), direction)
            monsters.add(monster)

    text_lose = font2.render("Skipped: " + str(lost), 1, (237, 236, 223))
    window.blit(text_lose,(10, 5))
    text = font2.render("Count: " + str(score), 1, (237, 236, 225))
    window.blit(text,(10, 40))
    text_warning = font3.render("25 Misses = You lost", 0.5, (204, 64, 29))
    window.blit(text_warning,(5, 75))
    text_win = font3.render("50 On count = You win", 0.5, (172, 255, 120))
    window.blit(text_win,(5, 95))

    if score >= goal:

        mixer.music.stop()
        finish = True
        window.blit(img_winner, (0,0))
        window.blit(win, (150,100))
    if sprite.spritecollide(ship,monsters, False) or lost >=25:


        mixer.music.stop()
        finish = True
        window.blit(img_loser, (0,0))
        window.blit(lose, (130, 100))

    display.update()
    clock.tick(FPS)
time.delay(50)