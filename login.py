#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import csv
import flappy #, hiscores

class loginApp:
    def __init__(self, master):
        #makes the gui
        self.master = master

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

        ##end of gui making

        #opens csv file
        with open('scores.csv') as csvfile:
            self.data = list(csv.reader(csvfile))

        self.ntries = 4 #counter for incorrect attempts
        self.clicked_new_account_before = False

    def log_in(self):
        if not self.are_fields_empty():
            if self.validate_credentials():
                print('success! logging in...')
                self.master.destroy()
                flappy.main()

            elif not self.validate_credentials():
                self.username_exists()


    def new_acc(self):
        if not self.clicked_new_account_before:
            if not self.are_fields_empty():
                if self.username_available():
                    if self.doublecheck_passowrd():
                        return

        elif self.clicked_new_account_before == True:
            if self.verify_new_password():
                print('meking new account...')
                self.write_data()
                self.master.destroy()
                flappy.main()

            elif not self.verify_new_password():
                self.try_again()

    def username_exists(self):
        if any(self.userentry.get() == line[0] for line in self.data):
            self.intruder_alert()
            return True
        else:
            if messagebox.askyesno('Username does not exist!', 'The username you entered does not exist! Would you like to make a new account?'):
                self.new_acc()
            return False


    def are_fields_empty(self):
        if self.userentry.get() == '' or self.passentry.get() == '':
            messagebox.showerror('Empty Fields','You left either your username or password empty! Without both, you cannot log in!!!')
            return True
        else: return False

    def validate_credentials(self):
        global theperson
        for line in self.data:
            if self.userentry.get() == line[0] and self.passentry.get() == line[1]:
                flappy.theperson = self.userentry.get()
                return True
            #else: return False

    def intruder_alert(self):
        if self.ntries > 1:
            self.ntries -= 1
            messagebox.showerror('WRONG PASSWORD ENTERED', 'YOU HAVE %s TRIES REMAINING' % self.ntries)
        else:
            messagebox.showerror('INTRUDER ALERT', 'UNAUTHORIZED USER DETECTED, PROGRAM EXITING...')
            self.master.destroy()

    def username_available(self):
        if any(self.userentry.get() == line[0] for line in self.data):
            messagebox.showerror('Username taken!', 'The username you entered is taken by someone else, try a different one!')
            self.passentry.delete(0,'end')
            self.userentry.delete(0,'end')
            return False
        else: return True

    def doublecheck_passowrd(self):
        messagebox.showinfo('Retype password', 'Please confirm your password.')
        self.oldpass = self.passentry.get()
        self.passentry.delete(0, 'end')
        self.clicked_new_account_before = True
        self.loginbutton.configure(state='disabled')
        return True

    def verify_new_password(self):
        if self.oldpass == self.passentry.get():
            return True
        else: return False

    def try_again(self):
        messagebox.showerror('Passwords do not match', 'The passwords do not match, try again')
        oldpass = ""
        self.clicked_new_account_before = False
        self.passentry.delete(0,'end')
        self.loginbutton.configure(state='normal')

    def write_data(self):
        with open('scores.csv', 'a', newline='') as csvfile:
            user = self.userentry.get()
            pas = self.passentry.get()
            csv.writer(csvfile).writerow([user,pas,str(0)])
def main():
  root = Tk()
  a = loginApp(root)
  root.title('Login To Flappy Bird')
  root.mainloop()
main()
