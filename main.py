import pygame as pg
import random
from sett import *
from sprites import *

#global playing
#playing = 0

f = open("dun.txt",)

class Game:
    
    def __init__(self):
        
        self.running = True
        self.current = ""
        self.curent_color = (0,0,0)
        pg.init()
        pg.mixer.init()
        self.win = pg.display.set_mode((W_W,W_H))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        
        
    def new(self):
        self.score = 0
        
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        
        self.buttons = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for i in PLAT_LIST:
            p = Platform(i[0],i[1],i[2],i[3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        #for i in Butt_list:
            #b = Button(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            #self.buttons.add(b)
        self.run()
        
    def run(self):
        global playing
        self.go = True
        while self.go:
            self.clock.tick(FPS)
            self.events()
            
                
            
            self.update()
            self.draw()
            
    def update(self):
        global playing
        global diff
        global dead
        global BEST_SCORE
        global curent_score
        if playing == 2:
            self.all_sprites.update()
            if self.player.vel.y >0:
                hits = pg.sprite.spritecollide(self.player,self.platforms,False)
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
            if self.player.rect.top <= W_H/4+30:
                self.player.pos.y += abs(self.player.vel.y)
                for i in self.platforms:
                    i.rect.y += abs(self.player.vel.y)
                    if i.rect.top >= W_H:
                        
                        i.kill()
                        self.score+=1
                        if self.score == diff:
                            playing = 3
                            dead = 1
                            self.go = False

            if self.player.rect.bottom > W_H:
                for sprite in self.all_sprites:
                    sprite.rect.y -= max(self.player.vel.y,10)
                    if sprite.rect.bottom<0:
                        sprite.kill()
                        playing = 3
                        dead = 0
                        
                        curent_score = self.score
                        if self.score > BEST_SCORE:
                            BEST_SCORE = self.score
                        self.go = False

            if len(self.platforms) == 0:
                
                self.go = False
               
                    
            while len(self.platforms)<4 and self.score<diff and self.player.vel[1] ==0:
                width = random.randint(50,100)
                p = Platform(random.randint(0,W_W-width),0,width,20)
                self.platforms.add(p)
                self.all_sprites.add(p)
                if self.current == "Endless":
                    diff+=1
                
    def events(self):
        global playing
        global diff
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.go:
                    self.go = False
                self.running = False
            
            if playing == 0:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                            playing = 1
                    if event.key == pg.K_ESCAPE:
                        if self.go:
                            self.go = False
                            self.running = False
                            
            elif playing == 1:
                if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            if self.go:
                                self.go = False
                                self.running = False
                        if event.key == pg.K_1:
                            diff = 50
                            
                            self.current = "Easy"
                            self.curent_color = DR_GREEN
                        if event.key == pg.K_2:
                            diff = 100
                            
                            self.current = "Normal"
                            self.curent_color = DR_JULTO
                        if event.key == pg.K_3:
                            diff = 150
                            
                            self.current = "Hard"
                            self.curent_color =DR_RED
                        if event.key == pg.K_4:
                            diff = 10
                            
                            self.current = "Endless"
                            self.curent_color =DR_PURPLE
                        if event.key == pg.K_SPACE and diff>0:
                                playing = 2
                            
            elif playing == 2:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE or event.key == pg.K_w:
                        self.player.jump()
                
            elif playing ==3:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        playing =2
                    if event.key == pg.K_ESCAPE:
                        diff = 0
                        self.current = " "
                        playing = 1
            
            #self.buttons.update() 
                
    def draw(self):
        global playing
        if playing ==0:
            g.show_st_win()
        elif playing ==1:
            g.chose_win()
        elif playing ==2:
            self.win.fill(BG)
            self.all_sprites.draw(self.win)
            
            self.draw_txt(str(self.score),30,RED,50,50)

        elif playing == 3:
            g.res_win()
            
        #print(diff)
        
        pg.display.update()
    def show_st_win(self):
        self.win.fill(WHITE)
        self.draw_txt("Game Start",50,BLACK,W_W/2,W_H/2-200)
        self.draw_txt("Press Space to continiue",15,BLACK,W_W/2,W_H/2+50-200)
        self.draw_txt("""A[left]...D[right]...W/Space[up]""",15,BLACK,100,530)
        #self.draw_txt("Choose DIfficulty",50,BLACK,W_W/2,W_H/2-100)
        #self.buttons.draw(self.win)

    def show_end_win(self):
        self.win.fill(WHITE)

    def chose_win(self):
        self.win.fill(WHITE)
        self.draw_txt("Choose DIfficulty",50,BLACK,W_W/2,W_H/2-100)
        pg.draw.rect(self.win,e_color,(50,300,100,50))
        self.draw_txt("Easy[1]",20,BLACK,95,310)
        pg.draw.rect(self.win,n_color,(185,300,100,50))
        self.draw_txt("Normal[2]",20,BLACK,230,310)
        pg.draw.rect(self.win,h_color,(320,300,100,50))
        self.draw_txt("Hard[3]",20,BLACK,365,310)
        pg.draw.rect(self.win,en_color,(187,400,100,50))
        self.draw_txt("Endless[4]",20,BLACK,W_W/2,410)
        self.draw_txt("Current dificulty: " + self.current,15,self.curent_color,W_W/2,525)
        if diff>0:
            self.draw_txt("Press Space to continiue",15,BLACK,W_W/2,550)
        
    def res_win(self):
        global curent_score
        self.win.fill(WHITE)
        self.draw_txt("Press Space to restart",15,BLACK,W_W/2,W_H/2+200)
        self.draw_txt("Press Esc to choose difficulty",15,BLACK,W_W/2,W_H/2+250)
        if self.current == "Endless":
            self.draw_txt("BEST SCORE: " + str(BEST_SCORE),50,BLACK,W_W/2,W_H/2-100)
            self.draw_txt("You'r score: " + str(curent_score),50,BLACK,W_W/2,W_H/2-150)
        if dead:
            self.draw_txt("You won",50,BLACK,W_W/2,W_H/2-200)
            
             
        else:
            #self.draw_txt("NOOOB",50,RED,W_W/2,W_H/2+200)
            self.draw_txt("You lost",50,BLACK,W_W/2,W_H/2-200)
            
    def draw_txt(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name,size)
        text_surf= font.render(text,True,color)
        text_rect = text_surf.get_rect()
        text_rect.midtop = (x,y)
        self.win.blit(text_surf,text_rect)

g = Game()

while g.running:
    
    g.new()
    
    g.show_end_win()
f.close()
pg.quit()
