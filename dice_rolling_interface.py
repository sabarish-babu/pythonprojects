from tkinter import *
from PIL import Image
import random
root=Tk()
root.geometry("500x400")
root.title("dice rolling")

# function definations
def rgb_of_pixel(image_path,x,y):
    #to conver the image into rgb value
    im = Image.open(image_path).convert('RGB')
    r,g,b=im.getpixel((x,y))
    #stroe the values in a 
    a=(r,g,b)
    # decision to return the values @ 1 to 6 by using rgb values
    if a == (211, 40, 48):
        b=1
    elif a == (180, 52, 56):
        b=2
    elif a == (210, 35, 48):
        b=3
    elif a == (197, 37, 49):
        b=4
    elif a == (218, 17, 10):
        b=5
    elif a == (178, 54, 57):
        b=6
    return b

# definition to play button
def to_play():
    play_button.destroy()
    roll_button.configure(state='normal')

# definition to roll the dice
def roll_dice():
    # destroy the into_dice_label
    intro_dice_label.destroy()
    global rand_img1,rand_img2
    # take the random images
    rand_img1=random.choice(dice)
    rand_img2=random.choice(dice)
    # By using the class photoimage store the values and display on the labels 
    image1 = PhotoImage(file=rand_img1)
    dice_label1=Label(root,image=image1)
    dice_label1.configure(image= image1)
    dice_label1.image = image1
    dice_label1.place(x=100,y=40)
    # smilarly  to the second image
    image2 = PhotoImage(file=rand_img2)
    dice_label2=Label(root,image=image2)
    dice_label2.configure(image= image2)
    dice_label2.image = image2
    dice_label2.place(x=300,y=40)
    # to gethe return values by using the user defined function of rgb_of_pixel 
    sd1=rgb_of_pixel(rand_img1,5,5)
    sd2=rgb_of_pixel(rand_img2,5,5)
    #update total label
    total =sd1+sd2
    total_label.config(text=f"You Rolled : {total}")    
    #update sub labels
    sub_dice_label1.config(text=sd1)
    sub_dice_label2.config(text=sd2)

#defintion to quit the window
def escape():
    root.destroy()

#creating a dice list 
dice=["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]

# creating the intro images and labeled
intro_image= PhotoImage(file='intro_dice.png')
intro_dice_label=Label(root,image=intro_image)
intro_dice_label.image=intro_dice_label
intro_dice_label.place(x=120,y=40)
# creating sub dice label to identific the values
sub_dice_label1=Label(root,text='')
sub_dice_label1.place(x=140,y=150)

sub_dice_label2=Label(root,text='')
sub_dice_label2.place(x=340,y=150)

# create total label for display the total value will rolled
total_label =Label(root,text='',font=('Helvetica',24),fg='gray')
total_label.place(x=135,y=300)

#creating Roll button
roll_button=Button(root,text='Roll Dice',command=roll_dice,width=10,state='disabled')
roll_button.place(x=50,y=225)

#creating quite button
quit_button=Button(root,text='Quit',command=escape,width=10,)
quit_button.place(x=350,y=225)

#creating play button
play_button=Button(root,text='Play',command=to_play,width=10,)
play_button.place(x=50,y=225)

root.mainloop()