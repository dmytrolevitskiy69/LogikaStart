# from moviepy import VideoFileClip
# import pygame
# pygame.init()
# pygame.display.set_caption('Showing Cutscene..')
# video = VideoFileClip('cutscene.mp4')
# video.preview()
# Якраз ось цей фрагментик я пробував зробити катсцену, але не находить файл. я виокирстовував PIP manager moviepy
from pygame import *
from random import randint
mixer.init()
mixer.music.load('flying battery alt.wav')
mixer.music.play()
goal = 200
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
font2 = font.Font(None, 40)
font1 = font.Font(None, 100)
font3 = font.Font(None, 20)
win = font1.render('You Won!', True, (255, 255, 255))
lose = font1.render('You Lost..', True, (255,255,255))
window = display.set_mode((win_width, win_height))
display.set_caption("Defenders")
burn = transform.scale(image.load("burn.png"), (win_width, win_height))
background = transform.scale(image.load("background.png"), (win_width, win_height))
img_loser = transform.scale(image.load("loose_screen.png"), (win_width, win_height))
img_winner = transform.scale(image.load("win_screen.png"), (win_width, win_height))
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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
           self.image = transform.rotate(transform.scale(image.load(img_hero), (80, 80)), 90)
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            self.image = transform.rotate(transform.scale(image.load(img_hero), (80, 80)), -90)
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
           self.image = transform.rotate(transform.scale(image.load(img_hero), (80, 80)), 0)
        if  keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
            self.image = transform.rotate(transform.scale(image.load(img_hero), (80, 80)), 180)
    def fire(self):
       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 6,20, -25)
       bullets.add(bullet)
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, direction):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.direction = direction

        if self.direction == 'left':
            self.image = transform.rotate(self.image, 90)
        elif self.direction == 'right':
            self.image = transform.rotate(self.image, -90)
        elif self.direction == 'bottom':
            self.image = transform.rotate(self.image, 180)

    def update(self):
        global lost

        def reset_position(self):
            global lost
            side = randint(1,4)

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
    def update(self):
        self.rect.y +=self.speed
        if self.rect.y<0:
            self.kill()
              


class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height,):
        super().__init__()
        self.color_1 =color_1
        self.color_2=color_2
        self.color_3=color_3
        self.width=wall_width
        self.height=wall_height
        self.image=Surface((self.width,self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



ship=Player(img_hero,5,win_height-80,80,80,8)   
monsters = sprite.Group()
bullets =sprite.Group()
w1 = Wall(112, 76, 62, 280, 0, 120, 560) 
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

    monster = Enemy(img_enemy, x, y, 80, 80, randint(3, 4), direction)
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
        w1.draw_wall()
        window.blit(background,(0, 0))
        window.blit(burn, (0,0))
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

    monster = Enemy(img_enemy, x, y, 80, 80, randint(3, 4), direction)
    monsters.add(monster)

    text_lose = font2.render("Пропущено: " + str(lost), 1, (237, 236, 223))
    window.blit(text_lose,(10, 40))
    text = font2.render("Рахунок: " + str(score), 1, (237, 236, 225))
    window.blit(text,(10, 10))
    text_warning = font3.render("25 Промахів = Програш", 0.5, (204, 64, 29))
    window.blit(text_warning,(5, 70))
    text_win = font3.render("200 На Рахунку = Виграш", 0.5, (172, 255, 120))
    window.blit(text_win,(5, 85))

    if score >= goal:
        finish = True
        window.blit(img_winner, (0,0))
        window.blit(win, (200,200))
    if sprite.spritecollide(ship,monsters, False) or lost >=25:
        finish = True
        window.blit(img_loser, (0,0))
        window.blit(lose, (200, 200))
    if sprite.collide_rect(ship, w1):
        finish = True
        window.blit(img_loser, (0,0))
        window.blit(lose, (200, 200))
    display.update()
    clock.tick(FPS)
time.delay(50)