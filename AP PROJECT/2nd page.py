from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='C:\\Users\\hp\\Downloads\\Bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w/2.5)
Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,columnspan=10)
Label(root,text='',font='Arial 20').grid(row=2,columnspan=10,pady=40)
Button(root,text='Seat Booking',command=root.bell,font='Arial 20',bg='Pale Green').grid(row=3,column=1,padx=80)
Button(root,text='Check Booked Seat',command=root.bell,font='Arial 20',bg='Dark Green').grid(row=3,column=3,padx=80,pady=20)
Button(root,text='Add Bus Detail',command=root.bell,font='Arial 20',bg='Green').grid(row=3,column=2,padx=100)
Label(root,text='For Admins Only',font='Arial 15',fg='Red').grid(row=4,column=3)

root.mainloop()
