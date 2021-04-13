import pygame
import sys
import random

pygame.init()

height_window=600
width_window=500
window=pygame.display.set_mode((width_window,height_window))
window.fill((255,255,255))
pygame.display.set_caption('game')
window.fill((255,255,0))

#color
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
yellow=(0,255,255)
black=(0,0,0)

font_1=pygame.font.SysFont('arial' , 30 , bold=20)
font_2=pygame.font.SysFont('arial' , 40 , bold=20)

is_mine=True
distance=50
xchange=0
distance_2=0
distance_y=500
speed=0.25
x=random.randint(0,width_window-100)
score=0
running=True




def clear():
    global is_mine
    global green
    global red
    global black
    green=(255,255,0)
    red=(255,255,0)
    black=(255,255,0)
    is_mine=False



def game_over():
    global xchange
    global speed
    global yellow
    global blue
    yellow=(0, 255,255)
    blue=(0,0,255)
    render=font_2.render('you game over' , True , (0,0,0))
    window.blit(render , (100,200))
    render_2=font_2.render(f'your score is {score}' , True , (0,0,0))
    window.blit(render_2 , (100,100))
    speed=0
    xchange=0
    pygame.display.update()





def accident():
    if ((distance<x<distance+100 or distance<x+100<distance+100) and  (distance_y<distance_2<distance_y+60 or distance_y<distance_2+60<distance_y+60)):
        game_over()
    


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse=pygame.mouse.get_pos()
            if is_mine:
                if 50<mouse[0]<250 and 300<mouse[1]<380:
                    clear()
                if 270<mouse[0]<470 and 300<mouse[1]<380:
                    sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                xchange=-1
            if event.key==pygame.K_RIGHT:
                xchange=1
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                xchange=0

    
    pygame.draw.rect(window ,green ,(50,300,200,80))
    pygame.draw.rect(window , red , (270 ,300 , 200,80))

    render_1=font_1.render('play!' ,True ,black )
    render_2=font_1.render('quit' , True , black)
    render_3=font_2.render('lets play game' , True , green)

    window.blit(render_1 , (100 ,320))
    window.blit(render_2 , (300,320))
    window.blit(render_3 , (100 , 100))

    

    
    if is_mine==False:
        window.fill((255,255,0))
        distance+=xchange
        distance_2+=speed
        pygame.draw.rect(window , yellow , (x, distance_2 ,100,60))
        pygame.draw.rect(window , blue , (distance,distance_y,100,60))
        if distance-3<0:
            xchange=0
        elif distance+105>width_window:
            distance=width_window-105
        
        if distance_2+60>height_window:
            x=random.randint(0,500)
            distance_2=0
            speed+=0.04
            score+=1

        accident()


    pygame.display.update()



    
    


































