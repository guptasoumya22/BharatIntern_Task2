from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='C:\\Users\\hp\\Downloads\\Bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12,padx=w/2.5)
Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=12)
Label(root,text='Add Bus Details',font='Arial 18',fg='Green',bg='Sky Blue').grid(row=2,columnspan=12,pady=20)
Label(root,text='Bus ID',font='Arial 10').grid(row=3,column=0)
Entry(root).grid(row=3,column=1)
Label(root,text='Bus Type',font='Arial 10').grid(row=3,column=2)
a=StringVar()
a.set('Bus Type')
OptionMenu(root,a,'AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1').grid(row=3,column=3)
Label(root,text='Capacity',font='Arial 10').grid(row=3,column=4)
Entry(root).grid(row=3,column=5)
Label(root,text='Fare Rs',font='Arial 10').grid(row=3,column=6)
Entry(root).grid(row=3,column=7)
Label(root,text='Operator ID',font='Arial 10').grid(row=3,column=8)
Entry(root).grid(row=3,column=9)
Label(root,text='Route ID',font='Arial 10').grid(row=3,column=10)
Entry(root).grid(row=3,column=11)
Button(root,text='Add Bus',font='Arial 10',bg='Pale Green').grid(row=4,column=6,pady=40)
Button(root,text='Edit Bus',font='Arial 10',bg='Pale Green').grid(row=4,column=7)
home=PhotoImage(file='C:\\Users\\hp\\Documents\\AP PROJECT\\home.png')
Button(root,image=home,font='Arial 10',bg='Pale Green').grid(row=4,column=8)

root.mainloop()




