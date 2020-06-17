

W_W = 480
W_H = 600
FPS = 120
FONT_NAME= 'arial' 

WHITE = (255,255,255)
BLACK = (0,0,0)
DR_RED = (200,0,0)
RED = (255,0,0)
DR_GREEN = (0,200,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DR_JULTO = (200,200,0)
JULTO = (255,255,0)
PURPLE = (255,0,255)
DR_PURPLE =(200,0,200)
TITLE = "DungeonBoss"
BG = (140, 156, 184)

e_color = GREEN
n_color = JULTO
h_color = RED
en_color = PURPLE

P_ACC = 0.5
P_FRIC = -0.12
P_GRAV = 0.8
P_JUMP = 20


PLAT_LIST= [(0,W_H-30,W_W,30),(W_W/2,W_H/2+100,100,20),
            (0,W_H-400,100,20)]

"""EASY = 50
NORMAL  = 100
HARD = 150

easy = (GREEN,DR_GREEN,W_W/2-200,W_H/2,100,50,EASY)
normal = (JULTO,DR_JULTO,W_W/2-50,W_H/2,100,50,NORMAL)
hard = (RED,DR_RED, W_W/2+100,W_H/2,100,50,HARD)
Butt_list = [easy,normal,hard]"""

playing = 0
diff = 0
dead = 0

BEST_SCORE = 0
curent_score = 0
