class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color=(177,156,217)):
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
        pass

import sys 
import pygame as pg

pg.init()

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
# btn = Button(20,20,300,300)                     # สร้าง Object จากคลาส Button ขึ้นมา
rec = Rectangle(20,20,100,100)
while(run):
    screen.fill((255, 255, 255))
    rec.draw(screen)
    # pg.time.delay(1)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D Right")
            rec.x += 5
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key A Left")
            rec.x -= 5
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key W Up")
            rec.y -= 5
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key S Down")
            rec.y += 5
            
        if rec.x >= 0 and rec.x <= win_x and rec.y >= 0 and rec.y <= win_y:
            pass 
        else :
            print("Out of frame")
    