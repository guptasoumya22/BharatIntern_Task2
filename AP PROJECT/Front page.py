from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='C:\\Users\\hp\\Downloads\\Bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12,padx=w/2.5)
Label(root,text="Online Bus Booking System",font='Arial 22 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=12)
Label(root,text="Name: Soumya Gupta",font='Arial 12 bold',fg='medium blue').grid(row=2,columnspan=12,pady=10)
Label(root,text="Er: 211b317",font='Arial 12 bold',fg='medium blue').grid(row=3,columnspan=12,pady=10)
Label(root,text="Mobile: 9770227599",font='Arial 12 bold',fg='medium blue').grid(row=4,columnspan=12,pady=10)
Label(root,text="Submitted to: Dr.Mahesh Kumar",font='Arial 17 bold',bg='light blue',fg='red').grid(row=5,columnspan=12,pady=10)
Label(root,text="Project Based Learning",font='Arial 12 bold',fg='red').grid(row=6,columnspan=12,pady=10)

root.mainloop()
