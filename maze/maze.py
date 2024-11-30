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

#Ігрова сцена:
win_width = 700
win_height = 500
 
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Персонажі гри:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
# стіни
w1 = Wall(240, 208, 33, 100, 20, 450, 10) # жовта
w2 = Wall(253, 5, 0, 100, 480, 350, 10)
w3 = Wall(15, 170, 247, 100, 10, 10, 380) 




w4 = Wall(154, 205, 50, 200, 140, 340, 10)
w5 = Wall(154, 205, 50, 200, 140, 10, 300) 

game = True
clock = time.Clock()
FPS = 60

#музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick=mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
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

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()

   
     
    display.update()
    clock.tick(FPS)