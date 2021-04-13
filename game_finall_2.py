import pygame
import sys

pygame.init()
width_window=500
height_window=600

window=pygame.display.set_mode((width_window , height_window))
window.fill((255,0,0))
pygame.display.set_caption('game')

#color
yellow=(0,255,255)
blue=(0,0,255)


class rect:
    global yellow
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def show(self,window):
        pygame.draw.rect(window , yellow , (self.x,self.y,400,400))


class ball:
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.radius=20

    def show(self , window):
        self.x-=self.vx
        self.y-=self.vy
        pygame.draw.circle(window , blue , (self.x , self.y) , self.radius)
    
    def move(self):
        new_x=self.x-self.vx
        new_y=self.y-self.vy


        if new_x-self.radius<rect_1.x or new_x+self.radius>rect_1.x+400:
            self.vx=-self.vx
        elif new_y+self.radius>rect_1.y+400 or new_y-self.radius<rect_1.y:
            self.vy=-self.vy
        else:
            self.vx=self.vx
            self.vy=self.vy

        self.show(window)
        


rect_1=rect(50,100)
ball_1=ball(300 , 120 , 1,1)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    rect_1.show(window)
    ball_1.move()

    pygame.display.update()










