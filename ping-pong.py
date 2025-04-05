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

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        global lost
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < W - 85:
            self.rect.x += self.speed

class Player(GameSprite):
    def update(self):
        global lost
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < W - 85:
            self.rect.x += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            pass

racket1 = Player('racket.png', 10, H // 2, 25, 100, 10)
racket2 = Player('racket.png', W - 35, H // 2, 25, 100, 10)
ball = GameSprite('ball.png', W // 2, H // 2, 50, 50, 0)

#музыка

pygame.mixer.init()
pygame.mixer.music.load('MUSIC.ogg')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

speed_x = 5
speed_y = 5

game = True
finish = False
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if finish != True:
        window.fill(background)

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        #racket1.update_l()
        #racket2.update_r()
    
        Player.update()
        Player.reset()
        pygame.display.update()
        clock.tick(FPS)