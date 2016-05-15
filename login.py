#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import csv

class loginApp:
    def __init__(self, master):
        #makes the gui

        topframe = Frame(master)
        topframe.pack()

        botframe = Frame(master)
        botframe.pack(side=BOTTOM and RIGHT)

        self.userlabel = Label(topframe, text='Username: ')
        self.userlabel.grid(sticky=E)

        self.passlabel = Label(topframe, text ='Password: ')
        self.passlabel.grid(row=1, sticky=E)

        self.userentry = Entry(topframe)
        self.userentry.grid(row=0,column=1)

        self.passentry = Entry(topframe)
        self.passentry.grid(row=1,column=1)

        self.loginbutton = Button(botframe, text='Log In', command=self.log_in)
        self.loginbutton.grid(row=0,column=1)

        self.newacbutton = Button(botframe, text='New Account', command=self.new_acc)
        self.newacbutton.grid(row=0, column=2, sticky=E)

        self.ntries = 4

    def log_in(self):
       with open('scores.csv') as csvfile:
            data = list(csv.reader(csvfile))

            usernm = self.userentry.get()
            passwd = self.passentry.get()


            if usernm == '' or passwd == '':
                messagebox.showerror('Empty Fields','You left either your username or password empty! Without both, you cannot log in!!!')
            elif usernm != '' and passwd != '':
                if not any(usernm in line for line in data):
                    if messagebox.askyesno('Username does not exist', 'Would you like to make a new account?'):
                        self.new_acc()
                else:
                    for index, line in enumerate(data):
                        if usernm == line[0]:
                            usernmindex = index
                            print('found username at index %s in data' %index)
                            print('password should be %s' %(data[usernmindex][1]))
                    if passwd == data[usernmindex][1]:
                        print('success! logging you in...')
                    elif self.ntries > 1:
                        self.ntries -= 1
                        messagebox.showerror('WRONG PASSWORD ENTERED', 'YOU HAVE %s TRIES REMAINING' %self.ntries)

                    else:
                        messagebox.showerror('INTRUDER ALERT', 'UNAUTHORIZED USER DETECTED, PROGRAM EXITING...')
                        root.destroy()
    def new_acc(self):
        print('making a new account, now all I need to do is code')




root = Tk()
a = loginApp(root)
root.title('Login To Flappy Bird')
root.mainloop()