from tkinter import *
from PIL import *
import random
root=Tk()
root.geometry('780x550')
im=['paper.png','rock.png','scissors.png']
computer_finalvalue=1
player_finalvalue=1

def computer_point_updation():
    global computer_finalvalue
    computer_point.configure(text='POINTS '+str(computer_finalvalue))
    int(computer_finalvalue)
    computer_finalvalue =computer_finalvalue + 1

def player_point_updation():
    global player_finalvalue
    player_point.configure(text='POINTS '+str(player_finalvalue))
    int(player_finalvalue)
    player_finalvalue =player_finalvalue + 1

def start():
    button_start.destroy()
    #rock,paper,scissors button creations
    button_rock = Button(root,text='ROCK',font=('bold',24),width=10,bg='lawn green',command=lambda:player_choice('rock.png'),state='disabled')
    button_rock.place(x=30,y=400)

    button_paper = Button(root,text='PAPER',font=('bold',24),width=10,bg='lawn green',command=lambda:player_choice('paper.png'),state='disabled')
    button_paper.place(x=280,y=400)

    button_scissor = Button(root,text='SCISSOR',font=('bold',24),width=10,bg='lawn green',command=lambda:player_choice('scissors.png'),state='disabled')
    button_scissor.place(x=530,y=400)

    #creating a quite button
    button_quite = Button(root,text='QUITE',width=10,font=('bold',16),bg='red',fg='white',command=quit)
    button_quite.place(x=185,y=500)

    #creating a restart button
    button_quite = Button(root,text='RESTART',width=10,font=('bold',16),bg='red',fg='white',command=restart)
    button_quite.place(x=430,y=500)
    button_rock.configure(state='normal')
    button_paper.configure(state='normal')
    button_scissor.configure(state='normal')
    computer_point.configure(text='POINT 0')
    player_point.configure(text='POINT 0')
    coumputer_label.configure(text='COMPUTER')
    player_label.configure(text='PLAYER')
def quit():
    root.destroy()

def restart():
    global computer_finalvalue,player_finalvalue
    computer_finalvalue=0
    player_finalvalue=0
    computer_point.configure(text='POINTS '+str(computer_finalvalue))
    player_point.configure(text='POINTS '+str(player_finalvalue))
    computer_finalvalue +=1
    player_finalvalue +=1

def player_choice(a):
    global randimg
    randimg=random.choice(im)
    computer_image=PhotoImage(file=randimg)
    computer_image_label=Label(root,image=computer_image)
    computer_image_label.configure(image=computer_image)
    computer_image_label.image=computer_image
    computer_image_label.place(x=50,y=100)
    playim=a
    player_image=PhotoImage(file=a)
    player_image_label=Label(root,image=player_image)
    player_image_label.configure(image=player_image)
    player_image_label.image=player_image
    player_image_label.place(x=500,y=100)
    if (randimg == playim):
        comment_label.configure    (text='        IT IS TIE    ')
    elif(randimg == 'rock.png'):
        if(playim == 'scissors.png'):
            comment_label.configure(text='COMPUTER WINS !!!')
            computer_point_updation()
        elif(playim == 'paper.png'):
            comment_label.configure(text=' PLAYER WINS !!!  ')
            player_point_updation()
    elif(randimg == 'paper.png'):
        if (playim == 'rock.png'):
            comment_label.configure(text='COMPUTER WINS !!!')
            computer_point_updation()
        elif (playim == 'scissors.png'):
            comment_label.configure(text=' PLAYER WINS !!!  ')
            player_point_updation()
    elif(randimg == 'scissors.png'):
        if(playim == 'paper.png'):
            comment_label.configure(text='COMPUTER WINS !!!')
            computer_point_updation()
        elif (playim == 'rock.png'):
            comment_label.configure(text='   PLAYER WINS !!!  ')
            player_point_updation()
    else:
        pass

#computer and player name creating
coumputer_label=Label(root,font=('bold',14))
coumputer_label.place(x=100,y=30)

player_label=Label(root,font=('bold',14))
player_label.place(x=600,y=30)

#creating points label

computer_point=Label(root,font=('bold',13))
computer_point.place(x=125,y=70)

player_point=Label(root,font=('bold',13))
player_point.place(x=610,y=70)


#creating comment label
comment_label=Label(root,text='',font=('bold',20))
comment_label.place(x=260,y=330)

#creating a start button
button_start=Button(root,width=10,text='START',font=('bold',24),command=start)
button_start.place(x=280,y=200)

root.mainloop()