from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
root=Tk()
root.geometry('800x460+300+100')
root.resizable(0,0)

#describeing a font wherever we want to use
my_font = Font(family="Segoe Script",size=25,weight='bold')

#creating main frame inside main frame have two frame one wil be button frame and another list frame
main_frame=Frame(root,bg='cyan')
main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(width=790,height=460)

text_label=Label(main_frame,text='Enter Your To Do Things :',font=('Terminal,bold',13),bg='cyan')
text_label.place(x=2,y=10)

#list frame
list_frame=Frame(main_frame,bg='cyan')
list_frame.place(x=200,y=60,width=590,height=400)

#creating list box
my_list=Listbox(list_frame,font=my_font,width=25,height=7,bg='cyan',bd=0,fg='#464646',highlightthickness=0,selectbackground="#a6a6a6",activestyle='none')
my_list.pack(padx=20,side='left',fill='both')

#creating scroll bar
my_scrollbar = Scrollbar(list_frame)
my_scrollbar.place(x=573,y=0,height=400)

#add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#creating entry part to add items to the list
my_entry=Entry(main_frame,font=('Times_New_Roman',24),width=31,bd=5)
my_entry.place(x=220,y=0)

#button function frame
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)
def cross_off_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    # get rid of selection bar
    my_list.selection_clear(0,END)
def uncross_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    # get rid of selection bar
    my_list.selection_clear(0,END)

def delete_crossed_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count,"fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count+=1

#creating menu block
my_menu=Menu(root)
root.config(menu=my_menu)

#function define
def save_list():
    file_name=filedialog.asksaveasfilename(initialdir="E:\data",title="Save File", filetypes=(("Dat Files","*.dat"),("All Files","*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f'{file_name}.dat'
        #delete crossed off items before saving 
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count,"fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count+=1
        #grab all the stuff from the list
        stuff= my_list.get(0,END)
        #open the file
        output_file=open(file_name,'wb')
        #actuall add the stuff to the file
        pickle.dump(stuff,output_file)
def open_list():
    file_name=filedialog.askopenfilename(initialdir="E:\data",title="Save File", filetypes=(("Dat Files","*.dat"),("All Files","*.*")))
    if file_name:
        #delete currently open list
        my_list.delete(0,END)
        #open the file
        input_file = open(file_name,'rb')
        #load data from the file
        stuff= pickle.load(input_file)
        #output stuff to the scree
        for item in stuff:
            my_list.insert(END,item)
def delete_list():
    my_list.delete(0,END)

#add items to the menu
file_menu= Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
# addding  drop down items
file_menu.add_command(label="save list",command=save_list)
file_menu.add_command(label="open list",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="clear list",command=delete_list)

#button frame
button_frame=Frame(main_frame,bg='cyan')
button_frame.place(x=0,y=60,width=200,height=400)
#add some button in the button frame
delete_button=Button(button_frame,width=18,text='Delete item',font=('bold',15),bd=0,bg='red',fg='light gray',command=delete_item)
add_button=Button(button_frame,width=18,text='Add item',font=('bold',15),bg='red',fg='light gray',bd=0,command=add_item)
cross_off_button=Button(button_frame,width=18,text='Cross off item',font=('bold',15),bg='red',fg='light gray',bd=0,command=cross_off_item)
uncross_button=Button(button_frame,width=18,text='uncross item',font=('bold',15),bg='red',fg='light gray',bd=0,command=uncross_item)
delete_crossed_button=Button(button_frame,width=18,text='Delete Crossed item',font=('bold',15),bg='red',fg='light gray',bd=0,command=delete_crossed_item)
add_button.place(x=0,y=50)
cross_off_button.place(x=0,y=100)
uncross_button.place(x=0,y=150)
delete_button.place(x=0,y=200)  
delete_crossed_button.place(x=0,y=250)

root.mainloop()