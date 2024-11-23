from pygame import *
 
#клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x<620:
            self.rect.x+=self.speed
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<420:
            self.rect.y+=self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.x<=470:
            self.direction='right'
        if self.rect.x>=615:
            self.direction='left'
        if self.direction=='left':
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed
 
#Ігрова сцена:
win_width = 700
win_height = 500
 
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background2.jpg"), (win_width, win_height))
 
#Персонажі гри:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
clock = time.Clock()
FPS = 60
 
#музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick=mixer.Sound('kick.ogg')
finish=False 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish!=True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()

    player.reset()
    monster.reset()
    final.reset()

   
     
    display.update()
    clock.tick(FPS)