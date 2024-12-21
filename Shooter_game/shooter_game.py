#Створи власний Шутер!

from pygame import *
from random import randint
mixer.init()
mixer.music.load('space.wav')
mixer.music.play()
goal = 200
fire_sound = mixer.Sound('fire.mp3')
img_hero="rocket.png"
img_back="galaxy.gif"
img_enemy="ufo.png"
img_bullet="bullet.png"
win_width = 700
win_height = 500

# шрифти і написи
font.init()
font2 = font.Font(None, 40)
font1 = font.Font(None, 100)
font3 = font.Font(None, 20)
win = font1.render('You Won!', True, (255, 215, 0))
lose = font1.render('You Lost..', True, (255,0,0))
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
background = transform.scale(image.load("galaxy.gif"), (win_width, win_height))
clock = time.Clock()
FPS=60
score = 0  # збито кораблів
lost = 0  # пропущено кораблів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
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
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15,20, -15)
       bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):  
        self.rect.y += self.speed
        global lost
        if self.rect.y>win_height:
            self.rect.x = randint(80,win_width-80)
            self.rect.y=0
            lost=lost+1
class Bullet(GameSprite):
    def update(self):
        self.rect.y +=self.speed
        if self.rect.y<0:
            self.kill()



ship=Player(img_hero,5,win_height-100,80,100,10)   
monsters = sprite.Group()
bullets =sprite.Group()
for i in range(1,6):
    monster=Enemy(img_enemy,randint(80,win_width-80),-40,80,50,(randint(1,5)))
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
    text_lose = font2.render("Пропущено: " + str(lost), 1, (237, 236, 223))
    window.blit(text_lose,(10, 40))
    text = font2.render("Рахунок: " + str(score), 1, (237, 236, 225))
    window.blit(text,(10, 10))
    text_warning = font3.render("25 Промахів = Програш", 0.5, (204, 64, 29))
    window.blit(text_warning,(5, 70))
    text_win = font3.render("200 На Рахунку = Виграш", 0.5, (172, 255, 120))
    window.blit(text_win,(5, 85))
    for c in collides:
        score+=1
        monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
        monsters.add(monster)
    if score >= goal:
        finish = True
        window.blit(win, (200,200))
    if sprite.spritecollide(ship,monsters, False) or lost >=25:
        finish = True
        window.blit(lose, (200, 200))
    display.update()
    clock.tick(FPS)
time.delay(50)