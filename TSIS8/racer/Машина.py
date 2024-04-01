import pygame as pg
from pygame.locals import *
import random, sys
import time

from pygame.sprite import *

pg.init()
W, H = 400, 600
clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))
screen.fill("white")
speed = 5
speed_player=5
score = 0
back_ground = pg.image.load("AnimatedStreet.png")
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "red")
coin=["coin1.png","coin2.png","coin3.png","coin4.png","coin5.png","coin6.png"]
coin_sheet_index = 0
point=0

class player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-speed, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(speed, 0)


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(coin[coin_sheet_index]), (pg.image.load(coin[coin_sheet_index]).get_width()//2, pg.image.load(coin[coin_sheet_index]).get_height()//2))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        
        if self.rect.top > 600:
           
            self.rect.center = (random.randint(30, 370), -300)

    def update_image(self):
        global coin_sheet_index
        coin_sheet_index = (coin_sheet_index + 1) % len(coin)  # Обновляем индекс изображения монетки с учетом цикличности
        self.image = pg.transform.scale(pg.image.load(coin[coin_sheet_index]), (pg.image.load(coin[coin_sheet_index]).get_width()//7, pg.image.load(coin[coin_sheet_index]).get_height()//7))


class Enemy(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, W - 30), 0)

    def move(self):
        global score  # Делаем переменную score глобальной
        self.rect.move_ip(0, speed)
        if self.rect.top> 600:
            self.rect.top= 0
            score += 1
            self.rect.center = (random.randint(30, 370), 0)


p1 = player()
e1 = Enemy()
c1 = Coin()
enemies = pg.sprite.Group()
enemies.add(e1)
all_sprites = pg.sprite.Group()
coins=pg.sprite.Group()
coins.add(c1)
all_sprites.add(p1)
all_sprites.add(e1)
inc_speed = pg.USEREVENT + 1
coin_ap = pg.USEREVENT + 1
pg.time.set_timer(coin_ap, 100)
pg.time.set_timer(inc_speed, 1000)
g = pg.mixer.Sound('background.mp3').play()
running = True

while running:

    
    screen.blit(back_ground, (0, 0))
    points=font_small.render(str(point), True, "yellow")
    scores = font_small.render(str(score), True, "black")
    screen.blit(scores, (10, 10))
    screen.blit(points, (W-20, 10))
    for en in all_sprites:
        screen.blit(en.image, en.rect)
        en.move()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == inc_speed:
            speed += 0.3
        if event.type == coin_ap:
            c1.update_image()
    screen.blit(c1.image, c1.rect)
    c1.move()
    if pg.sprite.spritecollideany(p1, coins):
        c1.rect.center = (random.randint(30, 370), -500)
        point+=1
    if pg.sprite.spritecollideany(p1, enemies):
        g.stop()
        pg.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        screen.fill("blue")
        screen.blit(game_over, (30, 250))
        pg.display.update()
        for entity in all_sprites:
            entity.kill()
        screen.blit(font_small.render(f"У вас {score} очков ", True, "black"), (10, 10))

        screen.blit(points, (W-20, 10))
        time.sleep(2)
        pg.quit()
        sys.exit()
    pg.display.update()
    clock.tick(60)
