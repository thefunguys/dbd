#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:08:27 2016

@author: William Cox
"""
import pygame
from random import randint
import numpy as np


 
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
 
# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
neuro_width = 15
neuro_height = 15
game_width = 320
game_height = 240
# Margin between each segment
segment_margin = 3
 
# Set initial speed
x_change = (segment_width + segment_margin)
y_change = 0
direction = 0 #right

 
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
def collision(snake_segments,score):
    for ii in range(len(snake_segments)-1,1,-1):
        if snake_segments[0].rect.x == snake_segments[ii].rect.x:
            if snake_segments[0].rect.y == snake_segments[ii].rect.y:
                for jj in range(ii,len(snake_segments)):
                    temp = snake_segments.pop()
                    temp.image.fill(BLACK)
                    score.reset()
    for jj in range(len(snake_segments)-1):
        if snake_segments[jj].rect.x > game_width - 10:
            snake_segments[jj].rect.x = snake_segments[jj].rect.x % game_width - 10
        if snake_segments[jj].rect.y > game_height - 10:
            snake_segments[jj].rect.y = snake_segments[jj].rect.y % game_height - 10
        if snake_segments[jj].rect.x < 10:
            snake_segments[jj].rect.x = snake_segments[jj].rect.x + game_width
        if snake_segments[jj].rect.y < 10:
            snake_segments[jj].rect.y = snake_segments[jj].rect.y + game_height
    
   
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
        
            
            
                
class neuro(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([neuro_width, neuro_height])
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()
        self.rect.x = randint(30,game_width - 30) // 18 * 18
        self.rect.y = randint(30,game_height - 30) // 18 * 18
    def update(self):
        
        self.rect = self.image.get_rect()
        self.rect.x = randint(30,game_width - 30) // 18 * 18
        self.rect.y = randint(30,game_height - 30) // 18 * 18 - 3
        pass
        
def collision_neuro(neuro,snake_segments,score):
    if np.abs(snake_segments[0].rect.x - neuro.rect.x) < 10:
        print('hello')
        if np.abs(snake_segments[0].rect.y - neuro.rect.y) < 10:
            print('but')
            neuro.update()
            x = snake_segments[len(snake_segments)-1].rect.x - (segment_width + segment_margin)
            y = snake_segments[len(snake_segments)-1].rect.y - (segment_height + segment_margin)
            segment = Segment(x,y)
            snake_segments.append(segment)
            allspriteslist.add(segment)
            score.add(1)
            

            
 
# Call this function so the Pygame library can initialize itself
main = __name__ == "__main__"
if main:
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([game_width, game_height])


    # Set the title of the window
    pygame.display.set_caption('Dylans Bad Day')
else:
    screen = pygame.Surface((game_width, game_height))
 
allspriteslist = pygame.sprite.Group()
 
# Create an initial snake
snake_segments = []
for i in range(2):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
    
#Create initial neurotransmitter

neuro = neuro()
allspriteslist.add(neuro)
score = Score((100,30))
allspriteslist.add(score)
 
 
clock = pygame.time.Clock()
done = False
 
def update(dt, pressed): 
    global x_change, y_change, direction, done
    speed = 1


    # Set the speed based on the key pressed
    # We want the speed to be enough that we move a full
    # segment, plus the margin.
    keys = pressed
    if keys[pygame.K_LEFT]:
        if direction != 0:
            x_change = (speed * segment_width + segment_margin) * -1
            direction = 2
        else:
            x_change = (speed * segment_width + segment_margin)
        y_change = 0
    if keys[pygame.K_RIGHT]:
        if direction != 2:
            x_change = (speed * segment_width + segment_margin)
            direction = 0
        else:
            x_change = (speed * segment_width + segment_margin) * -1
        y_change = 0
    if keys[pygame.K_UP]:
        x_change = 0
        if direction != 1:
            y_change = (speed * segment_height + segment_margin) * -1
            direction = 3
        else:
            y_change = (speed * segment_width + segment_margin)
    if keys[pygame.K_DOWN]:
        x_change = 0
        if direction != 3:
            y_change = (speed * segment_height + segment_margin)
            direction = 1
        else:
            y_change = (speed * segment_width + segment_margin) * -1
    if keys[pygame.K_ESCAPE]:
        done = True
    collision(snake_segments,score)
    collision_neuro(neuro,snake_segments,score)
 
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
 
    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change 
    y = snake_segments[0].rect.y + y_change 
    segment = Segment(x, y)
 
    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)
    score.score = len(snake_segments) - 1
    score.reRender()
    
    
 
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
 
    allspriteslist.draw(screen)
 
    clock.tick(5)
    # Flip screen
    if main:
        pygame.display.flip()

        # Pause
 

if main:
    while not done:
        update()
    pygame.quit()


                
