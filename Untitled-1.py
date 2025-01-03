from pygame import*
from random import randint
mixer.init()
mixer.music.load('flying battery alt.wav')
mixer.music.play()
win_width = 700
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Defenders")
background = transform.scale(image.load("background.png"), (win_width, win_height))
clock = time.Clock()
FPS=60
finish=False
run=True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0, 0))
        
    display.update()
    clock.tick(FPS)
time.delay(50)
