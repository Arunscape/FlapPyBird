#!/usr/bin/env python3
from tkinter import *
import csv
import flappy


class hiscore:
  def __init__(self, master):
    self.master = master
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

      self.listbox.delete(0,END)
      print('sortname')
      newlist = self.data
      sortedbyname = sorted(newlist, key=lambda x: x[0])
      print(sortedbyname)

      for line in sortedbyname:
        # distance = longestnamelength - len(line[0]) + 2
        self.listbox.insert(END, line[0], line[2], '-' * 20, '')
    def sort_score():
      self.listbox.delete(0,END)
      print('sortscore')
      newlist = self.data
      sortedbyscore = sorted(newlist,key=lambda x: int(x[2]), reverse = True)
      print(sortedbyscore)
      #longestname = max(self.data, key=lambda x: len(x[2]))
      #longestnamelength = len(longestname[0])

      for line in sortedbyscore:
        #distance = longestnamelength - len(line[0]) + 2
        self.listbox.insert(END, line[0], line[2], '-'*20, '')

    def get_score(person, score):
      for line in self.data:
        if flappy.theperson == line[0]:
          if flappy.totalscore > line[2]:
            high = line[2]

      newframe = Frame(master)
      newframe.pack()
      self.score = score
      self.person = person

      self.scorelabel = Label(newframe, text='Hello, %s! \n Your score that round was: %s \n Your all-time high is: %s' %(self.person, self.score, high))
      self.scorelabel.grid()


    get_score(flappy.theperson,flappy.totalscore)

    self.rd1 = Radiobutton(topframe, text='Name', variable = v, value = 1, command=sort_name)
    self.rd2 = Radiobutton(topframe, text='Score', variable = v, value =2, command=sort_score)

    self.rd1.grid(row=0, column=1, sticky =W)
    self.rd2.grid(row=0,column=2, sticky =W)



    scrollbar = Scrollbar(topframe, orient=VERTICAL)
    self.listbox = Listbox(topframe)
    self.listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=self.listbox.yview)
    scrollbar.grid(row=1, column=3)
    self.listbox.grid(row=1,columnspan=2)
    self.rd2.invoke()
       
    
    


  def try_again(self):
    self.master.destroy()
    flappy.main()
  def exit(self):
    self.master.destroy()



def main():
  root = Tk()
  a = hiscore(root)

  root.title('Highscores of Flappy Bird')
  root.mainloop()

