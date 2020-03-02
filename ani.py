import tkinter as tk
import time
import random



class Boxx(object):
    
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        self.id = canvas.create_rectangle(*args, **kwargs)
        self.vx = 3
        self.vy = 5
color  = "green"
lo = "hello"
class Text(object):
    def __init__(self, canvas, *args, **kwargs):
        global lo
        self.canvas = canvas 
        self.id = canvas.create_text(*args, **kwargs)

class App(object):
    
    def __init__(self, master ,**kwargs):
        global color
        self.master = master
        self.canvas = tk.Canvas(self.master, width=1400, height=1400)
        self.canvas.pack()
        
        Text(self.canvas, 40,30,text = lo ,fill = "blue")
        
        self.traffic = [
            #Alien(self.canvas, 2,2,30,30, outline = "white", fill = color)
        ]
        self.boxx = [
            Boxx(self.canvas,1350,75,10,50, fill = "black"),
            Boxx(self.canvas, 35,1350,10,49, fill = "black"),
            Boxx(self.canvas, 50,50, 60,76, outline = "white", fill = "white"),
            Boxx(self.canvas, 0, 300, 1400, 350, outline ="white", fill = "black"),
            Boxx(self.canvas, 0, 370, 1400, 420, outline ="white", fill = "black"),
  

        ]
        self.aliens = [
            #Alien(self.canvas, 20, 260, 120, 360,
            #      outline='white', fill='blue'),
            Alien(self.canvas, 0, 305, 20, 315, outline = "black", fill = 'green'),
            Alien(self.canvas, 2, 2, 40, 40, outline='white', fill='red'),
            Alien(self.canvas, 20, 60, 30, 70, outline='black', fill='yellow'),
            Alien(self.canvas, 0, 310, 20, 320, outline='black', fill='yellow'),
            Alien(self.canvas, 1130, 380, 1140, 400, outline='black', fill='yellow'),
            
        ]
        
        self.canvas.pack()
        self.master.after(0, self.animation)
        

    def animation(self):
        for alien in self.aliens:
            alien.move()
        self.master.after(12, self.animation)
    
    def update(self):
        self.color = "green"

    
        
        
        
class Alien(object):
    def __init__(self,canvas, *args, **kwargs):
        self.canvas = canvas
        self.id = canvas.create_oval(*args, **kwargs)
        self.vx = 2
        self.vy = 0
        
                
        

    def move(self):
        global color
        global lo
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        ra = random.choice([0.3, 0.4, 0.35, 0.29])
        
        rf = ra - 0.1
        if x2 > 1400:
            self.vx = -0.4 + rf
            if (x2 > 500):
                lo = "yeah"
                self.canvas.update()
                    
        if x1 < 0:
            self.vx = 0.4 +rf
        
        
        self.canvas.move(self.id, self.vx, self.vy)
    

root = tk.Tk()
app = App(root)
root.mainloop()