import pygame
import sys
from math import dist

pygame.init()

width_window=500
height_window=600
window=pygame.display.set_mode((width_window,height_window))
pygame.display.set_caption('game')
window.fill((0,0,0))

#color
white=(255,255,255)


velocity=1


class rect_1:
    global white
    def __init__(self,y,x):
        self.x=x
        self.y=y

    def show(self,window):
        pygame.draw.rect(window , white , (self.x,self.y,20,70))

    def move(self):
        window.fill((0,0,0))
        self.y=pygame.mouse.get_pos()[1]
        if self.y<0:
            self.y=0
        elif self.y+70>height_window:
            self.y=height_window-70


class rect_2:
    def __init__(self,y,x):
        self.y=y
        self.x=x

    def show(self,window):
        pygame.draw.rect(window , white , (self.x ,self.y ,20,70))

    def move(self):
        window.fill((0,0,0))
        self.y=pygame.mouse.get_pos()[1]
        
        if self.y<0:
            self.y=0
        elif self.y+70>height_window:
            self.y=height_window-70

        
  
class ball:
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vy=vy
        self.vx=vx
        self.radius=10

    def show(self,window):
        self.y-=self.vy
        self.x-=self.vx
        pygame.draw.circle(window , white , (self.x , self.y) , self.radius)

    def move(self):
        new_y=self.y-self.vy
        new_x=self.x-self.vx

        if new_x-self.radius<0 :
            self.vx=-self.vx

        elif new_y-self.radius<0 or new_y+self.radius>height_window:
            self.vy=-self.vy

        elif dist((self.x-self.radius  , self.y) , (rect_1_class.x+20 , rect_1_class.y))<30:
            self.vx=-self.vx
        
        elif dist((self.x-self.radius , self.y) , (rect_1_class.x+20 , rect_1_class.y+70))<30:
            self.vx=-self.vx

        elif dist((self.x+self.radius , self.y) , (rect_2_class.x , rect_2_class.y))<30:
            self.vx=-self.vx
        
        elif dist((self.x+self.radius , self.y) , (rect_2_class.x , rect_2_class.y+70))<30:
            self.vx=-self.vx

        elif dist((self.x - self.radius , self.y) , (rect_1_class.x+20 , rect_1_class.y+35))<30:
            self.vx=-self.vx
        
        elif dist((self.x+self.radius , self.y) , (rect_2_class.x , rect_2_class.y+35))<30:
            self.vx=-self.vx

        else:
            self.vx=self.vx
            self.vy=self.vy
        self.show(window)



ball_1=ball(50,400,0.2,0.2)
rect_1_class=rect_1(50 ,0)
rect_2_class=rect_2(50,width_window-20)


while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()




    rect_1_class.move()
    rect_2_class.move()
    ball_1.move()
    rect_1_class.show(window)
    rect_2_class.show(window)







    pygame.display.update()



