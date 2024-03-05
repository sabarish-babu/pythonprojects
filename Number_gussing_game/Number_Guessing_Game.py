from tkinter import *
import random 
guess=Tk()
guess.title("guess the number")
guess.configure(bg='PaleTurquoise2')
guess.resizable(0,0)
guess.geometry("500x300")
answer= random.randint(1,100)
chance_var=IntVar()
def restart():
    global attempts
    global text
    global answer
    answer=random.randint(1,100)
    text.set("You have 10 Attempts Remainning ! Good luck !!")
    attempts=10
    guess_entry.delete(0,"end")
    guess_restart.config(state='disabled')
    guess_check.config(state='normal')
def escape():
    guess.destroy()
attempts=10
#function define for checking answers 
def check_answer():
    global attempts
    global text
    attempts -= 1
    guess = int(guess_entry.get())
    if answer == guess:
        text.set("                    You Won ! Congratlations")
        guess_check.config(state='disabled')
        guess_restart.config(state='normal')
    elif attempts == 0:
        text.set("                 You have Out of Attempts !")
        guess_check.config(state='disabled')
        guess_restart.config(state='normal')
    elif guess < answer:
        text.set("Incorrect ! You have " + str(attempts) + " remaining - Go higher !!")
    elif guess >answer:
        text.set("Incorrect ! You have " + str(attempts) + " remaining - Go lower !!")
    return
#defining the labels and buttons
guess_label=Label(guess,text='Guess the number between 1 - 99',font=('bold'),bg='PaleTurquoise2')
guess_label.place(x=130,y=25)
guess_entry=Entry(guess,width=40,borderwidth=4)
guess_entry.place(x=128,y=100)
guess_check=Button(guess,text="CHECK",width=8,command=check_answer,bg='blue',fg='white')
guess_check.place(x=50,y=200)
guess_quit=Button(guess,text="QUIT",width=8,command=escape,bg='blue',fg='white')
guess_quit.place(x=370,y=200)
guess_restart=Button(guess,text="restart",width=8,state='disabled',command=restart,bg='red',fg='white')
guess_restart.place(x=210,y=200)
text=StringVar()
text.set("You have 10 Attempts Remainning ! Good luck !!")
guess_attempts=Label(guess,textvariable=text,font=('Times_New_Roman,bold'),fg='red',bg='PaleTurquoise2')
guess_attempts.place(x=90,y=150)
guess.mainloop()