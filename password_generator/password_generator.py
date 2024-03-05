from tkinter import *
from tkinter import messagebox
import random
import pyperclip

root = Tk()
root.geometry("497x500+350+100")
root.resizable(0,0)

#creating title
title_label= Label(root,text="PASSWORD GENERATOR",font=('bold',24))
title_label.place(x=50,y=10)

#decession frame
decession_frame=Frame(root,width=476,height=240,highlightthickness=2,highlightbackground='black')
decession_frame.place(x=10,y=60)

check_var1=IntVar()
check_var2=IntVar()
check_var3=IntVar()
check_var4=IntVar()

uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
numeric_letters="1234567890"
special_char_letters="`~!@#$%^&*()-_=+{}[]|\"/:;'<>,.?"
all=""
#function defining 
def click():
    global uppercase_letters,lowercase_letters,numeric_letters,special_char_letters,all
    global check_var1,check_var2,check_var3,check_var4
    global length_entry,password_amount
    password_text_box.delete(0,END)
    uppercase = check_var1.get()
    lowercase = check_var2.get()
    number = check_var3.get()
    special = check_var4.get()
    if uppercase == 1:
        all +=uppercase_letters
    if lowercase == 1:
        all +=lowercase_letters
    if number== 1:
        all +=numeric_letters
    if special == 1:
        all += special_char_letters
    length = int(length_entry.get())
    amount = int(password_amount.get())
    a= len(all)
    if a >= length:
        for x in range(amount):
            password= "".join(random.sample(all,length))
            password_text_box.insert(END,password)
    else:
        messagebox.showinfo("invalid length","There will be not enough charater in selected options")
    all=""

def clear():
    password_text_box.delete(0,END)
    length_entry.delete(0,END)
    password_amount.delete(0,END)
    check_button1.deselect()
    check_button2.deselect()
    check_button3.deselect()
    check_button4.deselect()

def copy():
    global password_text_box
    a= password_text_box.curselection()
    if a :
        index = a[0]
        val= password_text_box.get(index)
    pyperclip.copy(val)
    messagebox.showinfo("copied","sucessfully copied")

#creating check buttons and there text labels
check_button1=Checkbutton(decession_frame,variable=check_var1,onvalue= 1 ,offvalue= 2,width=3,height=2)
check_button1.place(x=10,y=10)

check_button1_text=Label(decession_frame,text='Uppercase Alphabet [A-Z]' ,font=('bold',12))
check_button1_text.place(x=45,y=16)

check_button2=Checkbutton(decession_frame,variable=check_var2,width=3,height=2)
check_button2.place(x=10,y=50)

check_button2_text=Label(decession_frame,text='lowercase Alphabet [a-z]',font=('bold',12))
check_button2_text.place(x=45,y=56)

check_button3=Checkbutton(decession_frame,variable=check_var3,width=3,height=2)
check_button3.place(x=10,y=90)

check_button3_text=Label(decession_frame,text='Numeric values [1-0]',font=('bold',12))
check_button3_text.place(x=45,y=96)

check_button4=Checkbutton(decession_frame,variable=check_var4,width=3,height=2)
check_button4.place(x=10,y=130)

check_button4_text=Label(decession_frame,text='Special Charaters [@#$...]',font=('bold',12))
check_button4_text.place(x=45,y=136)

Length_label=Label(decession_frame,text='Length of Password',font=('bold',12))
Length_label.place(x=260,y=16)

length_entry=Spinbox(decession_frame,font=('bold',12),from_=0,to=100000)
length_entry.place(x=260,y=48)

password_amount_label=Label(decession_frame,text='password to create',font=('bold',12))
password_amount_label.place(x=260,y=90)

password_amount=Spinbox(decession_frame,font=('bold',12),from_=0,to=10000)
password_amount.place(x=260,y=122)

generate_button=Button(decession_frame,text='Generate password',width=17,font=('bold',12),command=click)
generate_button.place(x=20,y=180)

copy_button=Button(decession_frame,text='Copy to Clickboard',width=17,font=('bold',12),command=copy)
copy_button.place(x=205,y=180)

clear_button=Button(decession_frame,text='clear',width=5,font=('bold',12),command=clear)
clear_button.place(x=390,y=180)

#text frame
text_frame = Frame(root,width=480,height=180,highlightbackground='black',highlightthickness=1)
text_frame.place(x=10,y=310)

generated_pass_label=Label(root,text='Generated Passwords')
generated_pass_label.place(x=20,y=300)

password_text_box=Listbox(text_frame,font=('bold',14),width=42,height=7,activestyle='none')
password_text_box.pack(side='bottom',fill='both',pady=10,padx=4)

password_text_box_scrollbar=Scrollbar(text_frame)
password_text_box_scrollbar.place(x=451,y=11,height=162)

password_text_box.config(yscrollcommand=password_text_box_scrollbar.set)
password_text_box_scrollbar.config(command=password_text_box.yview)

root.mainloop()
