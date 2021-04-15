import pygame
import sys
import random
from math import dist



pygame.init()

width_window=500
height_window=600

window=pygame.display.set_mode((width_window , height_window))
clock=pygame.time.Clock()
pygame.display.set_caption('play')



#variables !


down=True
ychange=0.2
yellow=(255 , 255 ,0)
green=(0,255,0)
xchange=0.2
score=0

font_2=pygame.font.SysFont('arial' , 30  , bold=20)

font_1=pygame.font.SysFont('arial' , 20 , bold=10)


class background:
    def __init__(self , x1 ,x2):
        self.x1=x1
        self.x2=x2
        self.vel=0.2
        self.img=pygame.image.load('background.jpg')
    
 
    def show(self , window):
        window.blit(self.img , (self.x1  , 0))
        window.blit(self.img , (self.x2 , 0) ) 

    def move(self):
        self.x1-=self.vel
        self.x2-=self.vel

        if self.x1+width_window<0:
            self.x1=self.x2+width_window
            

        elif self.x2+width_window<0:
            self.x2=self.x1+width_window
            


def game_over():
    global score
    global ychange
    global xchange
    ychange=0
    xchange=0
    background_1.vel=0
    rect_2_class.vel=0
    rect_1_class.vel=0
    render=font_2.render('you game over' , True , (255,255,0))
    render_2=font_2.render(f'your score is {score}' , True , (255,255,0))
    window.blit(render , (100 , 300))
    window.blit(render_2 , (100 , 400))

    pygame.display.update()





class enemy:
    def __init__(self , x , y):
        self.x=x
        self.y=y
        self.img=pygame.image.load('enemy.png')

    def show(self , window):
        window.blit(self.img , (self.x , self.y))

    def move(self ):
        global down
        global ychange

        if dist((self.x+33   , self.y) , ( rect_1_class.x , rect_1_class.y))<30:
            game_over()

            
        elif dist((self.x +33 , self.y) , (rect_2_class.x , rect_2_class.y)) <30:
            game_over()
        
        elif dist((self.x+33 , self.y) , (rect_1_class.x , rect_1_class.y-50))<30:
            game_over()

        elif dist((self.x+33 , self.y) , (rect_2_class.x , rect_2_class.y+50))<30:
            game_over()

 

        if not down:
            if ychange<0:
                self.y-=5
                ychange+=1
                self.y+=ychange
                
            else:
                down=True
        else:
            self.y+=xchange  

        
        if self.y<0:
            self.y=0

        elif self.y+60>height_window:
            self.y=height_window-60



class rect_1:
    def __init__(self , x , y):
        self.x=x
        self.y=y
        self.height=random.randint(50 , 210)
        self.vel=0.2
    
    def show(self, window):
        global green
        global yellow
        pygame.draw.rect(window ,  green , (self.x , self.y , 20 , self.height) , 2)
        pygame.draw.rect(window , yellow , (self.x-10 ,self.height , 40 , 10 ))


    def move(self):
        self.x-=self.vel

        if self.x+20<0:
            self.x=width_window
            self.height=random.randint(50, 210)


class rect_2:
    def __init__(self , x , height):
        self.x=x
        self.height=height
        self.y=height_window-self.height
        self.vel=0.2


    def show(self , window):
        pygame.draw.rect(window , green , (self.x , self.y , 20 , self.height) , 2)
        pygame.draw.rect(window , yellow , (self.x-10  ,self.y , 40 , 10))

            

    def move(self):
        global score
        self.x-=self.vel

        if self.x+20<0:
            self.x=width_window
            self.height=random.randint(50 , 210)
            self.y=height_window-self.height
            score+=5


def score_num():
    global score
    render_1=font_1.render(f'score is {score}' , True , (255,255,255))
    window.blit(render_1,  (50 , height_window-100))
 



background_1=background(0 , width_window)
enemy_1=enemy(60 , 300)
rect_1_class=rect_1(300 , 0)
rect_2_class=rect_2(rect_1_class.x , random.randint(50 , 210))



frame_counter=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                ychange=-10
                down=False




    background_1.move()
    enemy_1.move()
    rect_1_class.move()
    rect_2_class.move()
    background_1.show(window)
    enemy_1.show(window)
    rect_1_class.show(window)
    rect_2_class.show(window)
    score_num()

   

    
    pygame.display.update()













