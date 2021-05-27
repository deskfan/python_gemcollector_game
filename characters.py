#for gems
#Images licensed under Creative Commons Attribution 3.0. https://creativecommons.org/licenses/by/3.0/us/
#gem.png <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660

class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        super(Player,self).__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255,255,255),pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.score = 0


    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Gem:
    def __init__(self,image,screen):
        self.screen = screen
        self.surf = pygame.image.load(image)
        self.surf.set_colorkey((0,0,0),pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.randomize()
        self.collected = False
        self.last_collision = ()
        self.circle = Circle((self.rect.x,self.rect.y))

    def move(self):
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


    def randomize(self):
        self.rect.left = random.randint(50,900)
        self.rect.top = random.randint(50,600)

    def check_if_collected(self):
        if self.collected:
            self.rect.y -= 5
            self.circle.draw_circle(self.screen)
        else:
            self.circle.radius = 30
            self.circle.px = 30

        if self.rect.y <= -50:#SCREEN_HEIGHT:
            self.collected = False
            self.randomize()

class Villain:
    def __init__(self,image):
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((0,0,0),pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.randomize()
        self.x_change = 1
        self.y_change = 0

    def move_around(self):
        self.rect.x = self.rect.x + self.x_change

        if self.rect.left <= 0:
            self.x_change = 1
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_change = -1
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


    def randomize(self):
        self.rect.left = random.randint(75,850)
        self.rect.top = random.randint(75,550)

class Circle:
    def __init__(self,position):
        self.color = (255,255,255)
        self.position = position
        self.radius = 30
        self.px = 30
        self.start_time = pygame.time.get_ticks()

    def draw_circle(self,screen):
        if self.radius <= SCREEN_WIDTH/2:
            self.radius = self.radius + 2
            if self.px <= 1:
                self.px = 1
            else:
                self.px = self.px - 1
            pygame.draw.circle(screen, self.color, self.position, self.radius, self.px)
