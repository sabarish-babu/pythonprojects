from tkinter import *
root = Tk()
root.geometry('500x500')

#creating a button click funciton
operator = ''
def ButtonCLick(number):
    global operator
    operator = operator+number
    Text_field.delete(0,END)
    Text_field.insert(END,operator)
#create a clear function
def clear():
    global operator
    operator=''
    Text_field.delete(0,END)
#create a answer function
def answer():
    global operator
    Text_field.delete(0,END)
    result= str(eval(operator))
    Text_field.insert(0,result)

#creating main_frame
main_frame = Frame(root,highlightthickness=3,highlightbackground='black',bg='cyan')
main_frame.place(x=80,y=70,width=320,height=295)

cal_text_label = Label(main_frame,text='CALCULATOR',font=('Times_New_Roman,bold',20),bg='cyan')
cal_text_label.place(x=70,y=5)

Text_field = Entry(main_frame,width=14,bd='2',font=('bold',20))
Text_field.place(x=10,y=51)

clear_button =Button(main_frame,text='C',font=('bold',15),width='5',command=clear)
clear_button.place(x=238,y=50)
#creating button frame

Button_frame = Frame(main_frame,bg='cyan')
Button_frame.place(x=5,y=95,width=305,height=190)

# creating buttons 
button_7 = Button(Button_frame,text='7',font=('bold',15),width='5',command=lambda:ButtonCLick('7'))
button_7.place(x=5,y=5)

button_8 = Button(Button_frame,text='8',font=('bold',15),width='5',command=lambda:ButtonCLick('8'))
button_8.place(x=80,y=5)

button_9 = Button(Button_frame,text='9',font=('bold',15),width='5',command=lambda:ButtonCLick('9'))
button_9.place(x=155,y=5)

button_divide = Button(Button_frame,text='/',font=('bold',15),width='5',command=lambda:ButtonCLick('/'))
button_divide.place(x=230,y=5)

button_4 = Button(Button_frame,text='4',font=('bold',15),width='5',command=lambda:ButtonCLick('4'))
button_4.place(x=5,y=50)

button_5 = Button(Button_frame,text='5',font=('bold',15),width='5',command=lambda:ButtonCLick('5'))
button_5.place(x=80,y=50)

button_6 = Button(Button_frame,text='6',font=('bold',15),width='5',command=lambda:ButtonCLick('6'))
button_6.place(x=155,y=50)

button_multiply = Button(Button_frame,text='x',font=('bold',15),width='5',command=lambda:ButtonCLick('*'))
button_multiply.place(x=230,y=50)

button_1 = Button(Button_frame,text='1',font=('bold',15),width='5',command=lambda:ButtonCLick('2'))
button_1.place(x=5,y=95)

button_2 = Button(Button_frame,text='2',font=('bold',15),width='5',command=lambda:ButtonCLick('2'))
button_2.place(x=80,y=95)

button_3 = Button(Button_frame,text='3',font=('bold',15),width='5',command=lambda:ButtonCLick('3'))
button_3.place(x=155,y=95)

button_minus = Button(Button_frame,text='-',font=('bold',15),width='5',command=lambda:ButtonCLick('-'))
button_minus.place(x=230,y=95)

button_0 = Button(Button_frame,text='0',font=('bold',15),width='5',command=lambda:ButtonCLick('0'))
button_0.place(x=5,y=140)

button_dot = Button(Button_frame,text='.',font=('bold',15),width='5',command=lambda:ButtonCLick('.'))
button_dot.place(x=80,y=140)

button_equal = Button(Button_frame,text='=',font=('bold',15),width='5',command=answer)
button_equal.place(x=155,y=140)

button_add = Button(Button_frame,text='+',font=('bold',15),width='5')
button_add.place(x=230,y=140)

root.mainloop()