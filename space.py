#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 19:58:31 2016

@author: William Cox
"""

import pygame
from pygame.locals import *
from random import randint

#---GLOBALS---#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
word_list = ['the','and','red','green','yellow','stop','go','slow']
game_height = 240
game_width = 320
mid_x = 220
word_width = 15
word_height = 15
x_change = 20

class Ship(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #self.image = pygame.image.load('heart.png')
        self.image = pygame.Surface([20,25])
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = mid_x
        self.rect.y = game_height - 20
        
        
class Word(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.x = randint(20,game_width - 20)
        self.y = 15
        self.xy = (self.x,self.y)
        self.font = pygame.font.Font(None,25)
        self.word = word_list[randint(0,len(word_list)-1)]
        if self.word == 'yellow':
            self.color = YELLOW
        elif self.word == 'red':
            self.color = RED
        else:
            self.color = GREEN
        self.reRender()
        
    def reRender(self):
        self.image = self.font.render(self.word, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.xy
        
    def update(self):
        self.rect.y = self.rect.y + len(self.word) / 2
        pass
        
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self,Ship):
        super().__init__()
        self.x = Ship.rect.x
        self.y = Ship.rect.y
        
        self.image = pygame.Surface((5,15))
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.rect.y = self.rect.y - 7
        
        
class Score(pygame.sprite.Sprite):
    """sprite for score"""

    def __init__(self,xy):
        pygame.sprite.Sprite.__init__(self)
        self.xy = xy
        self.font = pygame.font.Font(None,50)
        self.color = (255,165,0)
        self.score = 0
        self.reRender()       
    
    def add(self,points):
        self.score += points
        self.reRender()
        
    def reset(self):
        self.score = 0
        self.reRender()
        
    def reRender(self):
        self.image = self.font.render("%d" %(self.score), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.xy        
        
        
        
            
    
        
def collision_word(bullet,sword):
    global word
    if bullet.rect.colliderect(sword.rect):
        sword.image.fill(BLACK)
        allspriteslist.remove(sword)
        sword.rect.x = 10000
        score.add(1)
        if len(words) < 10:
            rand_word = randint(1,4)
            for i in range(0,rand_word-1):
                temp_word = Word()
                words.append(temp_word)
                allspriteslist.add(temp_word)
                
        
def collision_word_wall(word):
    if word.rect.y > game_height -10:
        word.rect.y = 0
        if score.score > 0:
            score.add(-1)
        
def collision_ship(ship):
    if ship.rect.x > game_width - 10:
        ship.rect.x = ship.rect.x % (game_width -10)
    if ship.rect.x < 10:
        ship.rect.x = ship.rect.x + game_width

        
main = __name__ == "__main__"
if main:
    pygame.init()

    screen = pygame.display.set_mode([game_width,game_height])

    pygame.display.set_caption('Dylans Bad Day')
else:
    screen = pygame.Surface((game_width, game_height))

allspriteslist = pygame.sprite.Group()

ship = Ship()
allspriteslist.add(ship)

clock = pygame.time.Clock()
done = False
score = Score((30,30))
allspriteslist.add(score)

words = pygame.sprite.Group() 
words.add(Word())
allspriteslist.add(words)


def update(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.rect.x = ship.rect.x - x_change
            if event.key == pygame.K_RIGHT:
                ship.rect.x = ship.rect.x + x_change
            if event.key == pygame.K_UP:
                bullet = Bullet(ship)
                allspriteslist.add(bullet)
            if event.key == pygame.K_ESCAPE:
                done = True
    collision_ship(ship)
    screen.fill(BLACK)
    allspriteslist.update()
    bulletlist = pygame.sprite.Group()
    for sprite in allspriteslist.sprites():
        if type(sprite) == Bullet:
            bulletlist.add(sprite)
    remw = []
    for word in words:
        hit_list = pygame.sprite.spritecollide(word, bulletlist, True)
        for hit in hit_list:
            word.rect.x = 1000
            score.add(1)
            remw.append(word)
            print(len(words))
            rand_word = randint(1,3)
            if len(words) > 10:
                print('contd')
                continue
            for i in range(0,rand_word):
                temp_word = Word()
                words.add(temp_word)
                allspriteslist.add(temp_word)
            
        
                
        collision_word_wall(word)
        
    for rw in remw:
        words.remove(rw)
        
    allspriteslist.draw(screen)
    clock.tick(15)
    if main:
        pygame.display.flip()
        
if main:
    while not done:
        events = pygame.event.get()
        update(events)
        
    pygame.quit()
                
                
                
    
