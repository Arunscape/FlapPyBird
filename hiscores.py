#!/usr/bin/env python3
from tkinter import *


class hiscore:
  def __init__(self, master):
    #makes the gui
    

    topframe = Frame(master)
    topframe.pack()

    botframe = Frame(master)
    botframe.pack()


    self.tryagainbutton = Button(botframe, text='Try again', command=self.try_again)
    self.tryagainbutton.grid()
    self.exitbutton = Button(botframe, text = 'Exit' , command=self.exit)
    self.exitbutton.grid(row = 0, column = 1)

    v = IntVar()
    self.label = Label(topframe, text='Sort by:')
    self.label.grid(row = 0, column = 0)
    
    def sort_name():
      print('sortname')
    def sort_score():
      print('sortscore')

    Radiobutton(topframe, text='Name', variable = v, value = 1, command=sort_name).grid(row=0, column=1)
    Radiobutton(topframe, text='Score', variable = v, value =2, command=sort_score).grid(row=0,column=2)

    
    
    


  def try_again(self):
    pass
  def exit(self):
    root.destroy()
root = Tk()
a = hiscore(root)
root.title('Highscores of Flappy Bird')
root.mainloop()
