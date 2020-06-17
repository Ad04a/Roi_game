import pygame as pg
from sett import *

vec = pg.math.Vector2

bb =0

class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.rect.center = (W_W/2,W_H/2+100)
        self.pos = vec(W_W/2,W_H/2+300)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -P_JUMP
        
    
    def update(self):
        self.acc = vec(0,P_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.image = pg.image.load("alien.2.png")
            self.acc.x = -P_ACC
            if self.pos.x < W_W - (W_W-P_ACC):
                self.pos.x = W_W
        if keys[pg.K_d]:
            self.image = pg.image.load("alien.png")
            self.acc.x = P_ACC
            if self.pos.x > W_W -P_ACC:
                self.pos.x = 0
            
        self.acc.x += (self.vel.x * P_FRIC)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        
class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button(pg.sprite.Sprite):
    def __init__(self,color,dr_color,x,y,w,h,TYPE):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y =y
        self.color =color
        self.dr_color = dr_color
        self.TYPE = TYPE
        
    def hover(self):
        
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image.fill(self.dr_color)
            
        else:
            self.image.fill(self.color)
            
    def on_click(self):
        global bb
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if self.rect.collidepoint(mouse):
            if click[0] == 1:
                diff =  self.TYPE
                playing = 2
          
