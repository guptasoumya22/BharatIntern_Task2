from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='C:\\Users\\hp\\Downloads\\Bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=3,padx=w/2.5)

def check_booking():
    frame=Frame(root,highlightbackground='Black',highlightthickness=2,height=100,width=500)
    frame.grid(row=4,columnspan=5)
Label(frame,text='Passenger',font='Arial 10').grid(row=5,column=0)
Label(frame,text='Gender:',font='Arial 10').grid(row=5,column=1)
Label(root,text="Online Bus Booking System",font='Arial 20 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=3,pady=10)
Label(root,text="Check Your Booking",bg='green2',fg='green4',font='Arial 15 bold').grid(row=2,column=0,columnspan=3,pady=10)
Label(root,text="Enter Your Mobile No: ",font='Arial 10',width=15).grid(row=3,column=0,pady=10)
a=Entry(root)
a.grid(row=3,column=1)
Button(root,text="Check Booking",font='Arial 10',command=check_booking).grid(row=3,column=2)

root.mainloop()
