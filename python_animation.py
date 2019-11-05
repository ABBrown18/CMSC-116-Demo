from tkinter import *
import time
import random

win=Tk()
canvas=Canvas(win,width=400,height=500)
canvas.pack()

class Ball():
    def __init__(self,color,size):    
        self.shape=canvas.create_oval(10,10,size,size,fill=color)
        self.xspeed=random.randint(1,6)#user can give suitable speed
        self.yspeed=random.randint(5,10)#user can give suitable speed

    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        if pos[3]>=500 or pos[1]<=0:
            self.yspeed=-self.yspeed
        if pos[2]>=400 or pos[0]<=0:
            self.xspeed=-self.xspeed
            
redball=Ball("red",60)
greenball=Ball("green",100)
orangeball=Ball("orange",60)#here user can create another ball 
purpleball=Ball("purple", 50)
purpleball.xspeed=50
purpleball.yspeed=50

while True:
    redball.move()
    greenball.move()
    orangeball.move()
    purpleball.move()
    #if user create annother ball then user must call the move function inside while loop
    win.update()
    time.sleep(0.05)