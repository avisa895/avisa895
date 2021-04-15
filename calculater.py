from tkinter import *

window=Tk()
window.geometry('300x400')
window.resizable(width=False , height=False)
window.title('calculater')
window.configure(bg='red')


global entry_1
global entry_2
global entry_4

frame_1=Frame(window , bg='blue' , width=300 , height=100)
frame_1.pack(side=TOP)
frame_2=Frame(window , bg='yellow' , width=300 , height=100)
frame_2.pack(side=TOP)
frame_3=Frame(window , bg='red' , width=300 , height=100)
frame_3.pack(side=TOP)
frame_4=Frame(window , bg='orange' , width=300 , height=100)
frame_4.pack(side=TOP)

lab_1=Label(window , text='enter number_1' , fg='black' , bg='blue')
lab_1.place(x=50 , y=10)
entry_1=Entry(window , width=20)
entry_1.place(x=50 , y=30)

lab_2=Label(window , text='enter number_2' , fg='black' , bg='yellow')
lab_2.place(x=50 , y=110)
entry_2=Entry(window , width=20)
entry_2.place(x=50 , y=130)

but_1=Button(window , text='+' , bg='white' , width=5 , command=lambda:add())
but_1.place(x=20 , y=220)
but_2=Button(window , text='-' , bg='white' , width=5 , command=lambda:minus())
but_2.place(x=70 , y=220)
but_3=Button(window , text='*' , bg='white' , width=5 , command=lambda:multiple())
but_3.place(x=120 , y=220)
but_4=Button(window , text='/' , bg='white' , width=5 , command=lambda:divide())
but_4.place(x=170 , y=220)


lab_4=Label(window , text='result is :' , bg='orange' , fg='black')
lab_4.place(x=50 , y=310)
entry_4=Entry(window , width=20)
entry_4.place(x=50 , y=330)


def add():
    data_1=entry_1.get()
    data_2=entry_2.get()
    entry_4.delete(0,END)
    if data_1.isdigit() and data_2.isdigit():
        data_result=int(data_1)+int(data_2)
        entry_4.insert(END , data_result)
        entry_4.get()
    
    else:
        print('you cant carry out add')
        


def minus():
    data_1=entry_1.get()
    data_2=entry_2.get()
    entry_4.delete(0 , END)
    if data_1.isdigit() and data_2.isdigit():
        data_result=int(data_1)-int(data_2)
        entry_4.insert(END , data_result)
        entry_4.get()
    
    else:
        print('you cant carry out minus')


def multiple():
    data_1=entry_1.get()
    data_2=entry_2.get()
    entry_4.delete(0 , END)
    if data_2.isdigit() and data_1.isdigit():
        data_result=int(data_1)*int(data_2)
        entry_4.insert(END , data_result)
        entry_4.get()
    
    else:
        print('you cant carry out multiple')



def divide():
    data_1=entry_1.get()
    data_2=entry_2.get()
    entry_4.delete(0 , END)
   

    if not (data_1.isdigit() and data_2.isdigit()):
        print('you cant carry out division')

    
    elif data_2=='0':
        print('you cant divide digit on zero')
        



    elif data_1.isdigit() and data_2.isdigit():
        data_result=int(data_1)/int(data_2)
        entry_4.insert(END , data_result)
        entry_4.get()
















        

    




















window.mainloop()













