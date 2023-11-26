from tkinter import*
import random
root=Tk()
root.geometry("500x400+400+150")
root.title("dice rolling")
#quit the window function
def escape():
    root.destroy()

#get the dice 
def get_number(x):
    if x == '\u2680':
        return(1)
    elif x == '\u2681':
        return(2)
    elif x == '\u2682':
        return(3)
    elif x == '\u2683':
        return(4)
    elif x == '\u2684':
        return(5)
    elif x== '\u2685':
        return(6)
#Roll the dice function
def roll_dice():
    #roll the random 
    d1=random.choice(dice)
    d2=random.choice(dice)
    
    #detrmine dice number
    sd1=get_number(d1)
    sd2=get_number(d2)
    
    #update labels
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)

    #update total label
    total =sd1+sd2
    total_label.config(text=f"You Rolled : {total}")    
    
    #update sub labels
    sub_dice_label1.config(text=sd1)
    sub_dice_label2.config(text=sd2)

#creating a dice list on list the images will be added
dice=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]

#creating a mainframe 
main_frame= Frame(root)
main_frame.pack(pady=20)

#creating a dice label
dice_label1 =Label(main_frame,text='',font=('Helvetica',100))
dice_label1.grid(row=0,column=0,padx=5)
sub_dice_label1=Label(main_frame,text='')
sub_dice_label1.grid(row=1,column=0)

dice_label2 =Label(main_frame,text='',font=('Helvetica',100))
dice_label2.grid(row=0,column=1,padx=5)
sub_dice_label2=Label(main_frame,text='')
sub_dice_label2.grid(row=1,column=1)

#creating Roll button
roll_button=Button(root,text='Roll Dice',command=roll_dice,width=10)
roll_button.place(x=50,y=225)

#creating quite button
quit_button=Button(root,text='Quit',command=escape,width=10,)
quit_button.place(x=350,y=225)

#create total label
total_label =Label(root,text='',font=('Helvetica',24),fg='gray')
total_label.place(x=135,y=300)

#intilize the roll dice
roll_dice()

root.mainloop()
