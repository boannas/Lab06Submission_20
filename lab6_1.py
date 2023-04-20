class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color=(255,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouse = pg.mouse.get_pos()
        if mouse[0] >= self.x and mouse[0] <= self.x+self.w:
            if mouse[1] >= self.y and mouse[1] <= self.y+self.h:
                self.color = (121,121,121)
                if pg.mouse.get_pressed() == (1, 0, 0):
                    self.color = (177,156,217)
            else :
                self.color = (239,161,161)
        else :
            self.color = (239,161,161)

import sys 
import pygame as pg

pg.init()

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100)                     # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen)
    btn.isMouseOn()
    # print(mouse)
    # pg.time.delay(1)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    