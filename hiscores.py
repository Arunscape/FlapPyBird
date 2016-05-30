#!/usr/bin/env python3
from tkinter import *
import csv
from operator import itemgetter

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
    v.set(2)
    self.label = Label(topframe, text='Sort by:')
    self.label.grid(row = 0, column = 0)

    with open('scores.csv') as csvfile:
      self.data = list(csv.reader(csvfile))
    
    def sort_name():
      print('sortname')
    def sort_score():
      print('sortscore')
      newlist = self.data
      sortedbyscore = sorted(newlist,key=lambda x: int(x[2]), reverse = True)
      print(sortedbyscore)
      longestname = max(self.data, key=lambda x: len(x[2]))
      longestnamelength = len(longestname[0])

      for line in sortedbyscore:
        #distance = longestnamelength - len(line[0]) + 2
        self.listbox.insert(END, line[0], line[2], '-'*20)


    rd1 = Radiobutton(topframe, text='Name', variable = v, value = 1, command=sort_name)
    rd2 = Radiobutton(topframe, text='Score', variable = v, value =2, command=sort_score)
    rd2.select()
    rd1.grid(row=0, column=1, sticky =W)
    rd2.grid(row=0,column=2, sticky=W)



    scrollbar = Scrollbar(topframe, orient=VERTICAL)
    self.listbox = Listbox(topframe)
    self.listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=self.listbox.yview)
    scrollbar.grid(row=1, column=3)
    self.listbox.grid(row=1,columnspan =3)
    
       
    
    


  def try_again(self):
    pass
  def exit(self):
    root.destroy()

def main():
  root = Tk()
  a = hiscore(root)
  root.title('Highscores of Flappy Bird')
  root.mainloop()
