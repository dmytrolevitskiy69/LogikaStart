from pygame import*
window = display.set_mode((700, 500))
display.set_caption("Лабіринт")
background = transform.scale(image.load("background.jpg"),(700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite('hero.png', 5, 420, 4)
monster = GameSprite('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 480, 420, 0)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
FPS = 60
clock = time.Clock()


game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    player.reset()
    monster.reset()
    final.reset()

    display.update()
    clock.tick(FPS)