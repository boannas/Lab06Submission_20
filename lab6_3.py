class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.x = x
        self.y = y

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    # self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
            
        

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

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
                self.color = (166,156,173)
                if pg.mouse.get_pressed() == (1, 0, 0):
                    self.color = (156,146,163)
                    # print("Something happen")
                    return 1 
            else :
                self.color = (176,166,183)
        else :
            self.color = (176,166,183)

import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 75, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(100, 325, 140, 32) # สร้าง InputBox2
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
font2 = pg.font.Font('freesansbold.ttf', 16)
something = ''
text1 = font.render('First Name', True,(166,100,177), (255,255,255)) # (text,is smooth?,letter color,background color)
text2 = font.render('Last Name', True,(166,100,177))
text3 = font.render('Age', True,(166,100,177))
text4 = pg.font.Font('freesansbold.ttf', 20).render('submit', True,(255,255,255))

textRect = text1.get_rect() # text size
textRect.center = (win_x // 2, win_y // 2)

btn = Button(550,300,100,50)    
btn.color = (176,166,183)


while run:
    mouse = pg.mouse.get_pos()
    screen.fill((255, 255, 255))
    btn.draw(screen)
    btn.isMouseOn()
    text5 = font2.render(something , True,(255,0,0))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
            
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    if btn.isMouseOn() == 1 :
        if input_box1.text != '' and input_box2.text != '' and input_box3.text != '':
            if input_box3.text.isnumeric() == True :
                something = "Hello " + input_box1.text + " " + input_box2.text + "! " + "You are " + input_box3.text + " years old."
            else  :
                something = "Age doesn't contain the string!"
        else :
            something = "You miss something !"
    # print(btn.isMouseOn())
    screen.blit(text1, (input_box1.x , input_box1.y - 50))
    screen.blit(text2, (input_box2.x , input_box2.y - 50))
    screen.blit(text3, (input_box3.x , input_box3.y - 50))
    screen.blit(text4, (btn.x + (btn.w)/6 , btn.y + (btn.h)/8))
    screen.blit(text5, (200, 400))
    print(55)
    pg.time.delay(1)
    pg.display.update()