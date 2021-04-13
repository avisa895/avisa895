import pygame
import sys
import random
from math import dist
import os

pygame.init()


width_window=500
height_window=600
window=pygame.display.set_mode((width_window , height_window))
pygame.display.set_caption('play game ')

base_dir=os.getcwd()


xchange=0
bullets=[]
ychange=1
ychange_1=1
enemies=[]
score=0
explosions=[]
health_backs=[]


font_1=pygame.font.SysFont('arial' , 20 , bold=20)

sound_effects={
    'collision':pygame.mixer.Sound(os.path.join(base_dir , 'collision.wav')),
    'heal':pygame.mixer.Sound(os.path.join(base_dir , 'heal.wav')),
    'hit':pygame.mixer.Sound(os.path.join(base_dir , 'hit.wav')),
    'shoot1':pygame.mixer.Sound(os.path.join(base_dir , 'shoot1.wav'))
}



class player:
    def __init__(self , x , y):
        self.x=x
        self.y=y
        self.img=pygame.image.load('player.png')
        self.health=110
    
    def show(self , window):
        window.blit(self.img , (self.x , self.y))
    
    def move(self):
        global xchange
        self.x+=xchange

        if self.x<0:
            self.x=0
        elif self.x+60>width_window:
            self.x=width_window-60


player_1=player(50 , height_window-120)


class background:
    def __init__(self):
        self.x1=0
        self.x2=height_window
        self.img=pygame.image.load('background.jpg')
        self.vel=1
    
    def show(self , window):
        window.blit(self.img , (0 , self.x1))
        window.blit(self.img , (0 , self.x2))

    def move(self):
        self.x1-=self.vel
        self.x2-=self.vel

        if self.x1+height_window<0:
            self.x1=self.x2+height_window
        elif self.x2+height_window<0:
            self.x2=self.x1+height_window
        
        self.show(window)


def running():
    menu_azad=True
    


class bullet:
    def __init__(self , x , y ):
        self.x=x
        self.y=y
        self.img=pygame.image.load('bullet.png')

    def show(self , window):
        window.blit(self.img , (self.x , self.y))
    
    def move(self):
        global ychange
        self.y-=ychange


    def add(self , list_1):
        list_1.append(self)

    def remove(self , list_1):
        list_1.pop(list_1.index(self))
    
def bullet_control():
    for bullet in bullets:
        bullet.move()
        bullet.show(window)
        if bullet.y<0:
            bullet.remove(bullets)



class enemy:
    def __init__(self , x,y):
        self.x=x
        self.y=y
        self.img=pygame.image.load('enemy.png')
        self.damage=10
    
    def show(self, window):
        window.blit(self.img , (self.x , self.y))

    def move(self):
        self.y+=ychange_1

    def add(self , list_1):
        list_1.append(self)

    def remove(self , list_1):
        list_1.pop(list_1.index(self))


def enemy_control():
    global score
    global enemies
    r_x=random.randint(0,width_window)
    r_y=random.randint(-800,-200)
    if len(enemies)<7:
        enemi_1=enemy(r_x ,r_y)
        if all(dist((r_x , r_y) , (enemi.x , enemi.y))>70 for enemi in enemies):
            enemi_1.add(enemies)

    
    for enemi in enemies:
        enemi.move()
        enemi.show(window)

        if enemi.y>height_window:
            enemi.remove(enemies)
        
        for bullet in bullets:
            if dist((bullet.x , bullet.y) , (enemi.x , enemi.y))<34:
                sound_effects.get('hit').play()
                explosion_1=explosion(enemi.x , enemi.y , pygame.time.get_ticks())
                explosion_1.add(explosions)
                enemi.remove(enemies)
                bullet.remove(bullets)
                score+=1
                player_1.health+=enemi.damage


        if dist((enemi.x , enemi.y) , (player_1.x , player_1.y))<30:
            sound_effects.get('collision').play()
            enemi.remove(enemies)
            player_1.health-=enemi.damage



    

class heart:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.img=pygame.image.load('heart.png')
        self.color=(0,255,0)
        self.x_rect=70

    

    def show(self , window , health):
        global color_heart
        pygame.draw.rect(window , (255,255,255) , (self.x , self.y , width_window , 50))
        render=font_1.render(f'score={score}' , True, (0,0,0))
        window.blit(render , (420 , height_window-30))
        window.blit( pygame.transform.scale( self.img , (40,40)) , (10 , height_window-40))
        pygame.draw.rect(window , (0,0,0) , (70 , height_window-40 , 110,30) , 3)
        pygame.draw.rect(window , self.color , (self.x_rect , height_window-40 , health ,30))

        
        if health<40:
            self.color=(255,0,0)
        elif health<60:
            self.color=(255,255,0)
        elif health<100:
            self.color=(0,255,0)



class explosion:
    def __init__(self , x,y , time):
        self.x=x
        self.y=y
        self.img=pygame.image.load('explosion.png')
        self.vel=0.4
        self.time=time

    def show(self , window):
        window.blit(self.img , (self.x , self.y))
    
    def move(self):
        self.y+=self.vel
    
    def add(self , list_1):
        list_1.append(self)

    def remove(self , list_1 , time):
        if time-self.time>300:
            list_1.pop(list_1.index(self))


def explosion_control():
    for explosion in explosions:
        explosion.move()
        explosion.show(window)
        explosion.remove(explosions , pygame.time.get_ticks())



class health_back:

    def __init__(self , x , y ,time , timer):
        self.x=x
        self.y=y
        self.time=time
        self.timer=timer
        self.rotate=1
        self.angle=6
        self.img=pygame.image.load('heart.png')
        self.vel=1


    def show(self , window ):
        window.blit(self.img , (self.x , self.y))

    def move(self,time):
        #after n sanie
        if time-self.time>self.timer:
            self.y+=self.vel
            self.img=pygame.transform.rotate(pygame.image.load('heart.png') , self.angle)
            self.angle+=self.rotate

            if self.angle==15:
                self.rotate=-1
            
            elif self.angle==-15:
                self.rotate=1

    def add(self , list_1):
        list_1.append(self)

    def remove(self , list_1):
        list_1.pop(list_1.index(self))

def health_back_control():
    global health_backs
    if player_1.health<40 and len(health_backs)<1:
        health_back_1=health_back(random.randint(0,width_window) , random.randint(-800,-200) , pygame.time.get_ticks() , random.randint(1000,3000))
        health_back_1.add(health_backs)

    for health_1 in health_backs:
        health_1.move(pygame.time.get_ticks())
        health_1.show(window)

        if health_1.y>height_window:
            health_1.remove(health_backs)
        elif dist((health_1.x , health_1.y) , (player_1.x , player_1.y))<30:
            sound_effects.get('hit').play()
            health_1.remove(health_backs)
            player_1.health+=10


def reset_game():
    global enemies , bullets ,health_backs , explosions , score 

    enemies=[]
    bullets=[]
    health_backs=[]
    explosions=[]
    score=0



back_ground=background()
heart_1=heart(0 , height_window-50 )

menu=True
menu_azad=False
running=True
while running:
    bullet_1=bullet(player_1.x , player_1.y)

    while menu_azad:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    menu_azad=False
                
        render_1=font_1.render('you game over' , True , (255,255,0))
        window.blit(render_1 , (150 , 300))
        render_2=font_1.render(f'yor score is {score}' , True , (255,255,0))
        window.blit(render_1 , (150 , 350))
        render_3=font_1.render('start again' , True , (255 , 255 , 0))
        window.blit(render_3 , (150 , 400))
        pygame.display.update()
        

        

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    menu=False
                


        render=font_1.render('press enter to start game' , True , (255,255,0))
        window.blit(render , (130,300))
        
        pygame.display.update()

                

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                xchange=1
            if event.key==pygame.K_LEFT:
                xchange=-1
            if event.key==pygame.K_SPACE:
                sound_effects.get('shoot1').play()
                bullet_1.add(bullets)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                xchange=0

    if player_1.health<10:
        menu_azad=True
        


    player_1.move()
    back_ground.move()
    bullet_control()
    enemy_control()
    health_back_control()
    heart_1.show(window , player_1.health)
    player_1.show(window)
    explosion_control()



    pygame.display.update()

    pygame.display.update()












 


