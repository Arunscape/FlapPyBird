#!/usr/bin/env python3
from tkinter import *

class hiscore:
  def __init__(self, master):
    #makes the gui
    

    topframe = Frame(master)
    topframe.pack()

    botframe = Frame(master)
    botframe.pack()


    self.bg_image = PhotoImage(file ="assets/sprites/background-night.png")
    self.x = Label (topframe, image = self.bg_image)
    #self.x.place(x=0, y=0, relwidth=1 ,relheight=1)
    self.x.pack()


    self.tryagainbutton = Button(botframe, text='Try again', command=self.try_again)
    self.tryagainbutton.grid()
    self.exitbutton = Button(botframe, text = 'Exit' , command=self.exit)
    self.exitbutton.grid(row = 0, column = 1)



  def try_again(self):
    pass
  def exit(self):
    root.destroy()
root = Tk()
a = hiscore(root)
root.title('Highscores of Flappy Bird')
root.mainloop()
