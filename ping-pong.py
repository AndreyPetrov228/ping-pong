import pygame

W = 700
H = 500

window = pygame.display.set_mode((W, H))
pygame.display.set_caption('Пинг понг')
background = (114, 165, 247)
window.fill(background)

clock = pygame.time.Clock()
FPS = 60

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, width, height, player_speed):
        self.image = pygame.transform.scale(pygame.image.load(player_img), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


class Player(GameSprite):
    def update(self):
        global lost
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < W - 85:
            self.rect.x += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            pass

player = Player('левая ракетка.jpg', 0, 350, 100, 210, 5)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    
    Player.update()
    Player.reset()
    display.update()
    clock.tick(FPS)