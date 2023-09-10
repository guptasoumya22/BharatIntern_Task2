from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='C:\\Users\\hp\\Downloads\\Bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=11,padx=w/2.5)
Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=11,pady=2)
Label(root,text='Enter Journey Details',font='Arial 15',fg='Green3',bg='Pale Green').grid(row=3,column=0,columnspan=11,pady=2)
Label(root,text="To",font='Arial 10').grid(row=5,column=1)
a=Entry(root)
a.grid(row=5,column=2)
Label(root,text="From",font='Arial 10').grid(row=5,column=3)
b=Entry(root)
b.grid(row=5,column=4)
Label(root,text="Journey Date",font='Arial 10').grid(row=5,column=5)
c=Entry(root)
c.grid(row=5,column=6)

def booking_proceed():
    Label(root,text='Fill Passenger Details to Book the bus ticket',font='Arial 18',fg='Red',bg='Sky Blue').grid(row=9,columnspan=11,pady=5)
    Label(root,text='Name',font='Arial 10').grid(row=11,column=0)
    Entry(root).grid(row=11,column=1)
    Label(root,text='Gender',font='Arial 10',width=5).grid(row=11,column=2)
    c=StringVar()
    c.set('Male')
    OptionMenu(root,c,'Male','Female').grid(row=11,column=3)
    Label(root,text='No.of seats',font='Arial 10',width=8).grid(row=11,column=4)
    Entry(root,width=5).grid(row=11,column=5)
    Label(root,text='Mobile No.',font='Arial 10',width=10).grid(row=11,column=6)
    Entry(root).grid(row=11,column=7)
    Label(root,text='Age',font='Arial 10',width=5).grid(row=11,column=8)
    Entry(root,width=5).grid(row=11,column=9)
    Button(root,text='Book Seat',font='Arial 10',bg='Pale Green').grid(row=11,column=10)

def show_bus():
    Label(root,text="Select Bus",fg='green4',font='Arial 10').grid(row=7,column=1)
    Label(root,text="Operator",fg='green4',font='Arial 10').grid(row=7,column=2)
    Label(root,text="Bus Type",fg='green4',font='Arial 10').grid(row=7,column=3)
    Label(root,text="Available Capacity",fg='green4',font='Arial 10').grid(row=7,column=4)
    Label(root,text="Fare",fg='green4',font='Arial 10').grid(row=7,column=5)
    Button(root,text='Bus1',font='Arial 10',fg='Black',bg='Pale Green').grid(row=8,column=1)
    Button(root,text="Proceed to Book",bg='Pale Green',command=booking_proceed,font='Arial 10').grid(row=8,column=6,pady=10)

def book_seat():
    Label(

Button(root,text="Show Bus",command=show_bus,font='Arial 10',bg='Sea Green').grid(row=5,column=7)
home=PhotoImage(file='C:\\Users\\hp\\Documents\\AP PROJECT\\home.png')
Label(root,image=home,bg='Green').grid(row=5,column=8,pady=2)

root.mainloop()
