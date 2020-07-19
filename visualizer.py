from tkinter import *
from tkinter import ttk
import numpy as np
import work

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.config(bg='#990033')


#variables
selected_alg = StringVar()

def drawData(canvas,process,downShift,upShift):
    p="p",process
    canvas.create_rectangle(upShift, process*100 , downShift, (process*100)+20, fill="#666633")
    canvas.create_text(20, process*100, anchor=SW, text=p )  
def clear():
    cap.clear()
    ded.clear()
    per.clear()
    a_t.clear()
    b_t.clear()
global cap
global ded
global per
global a_t
global b_t
cap = []
ded = []
per = []
a_t = []
b_t = []

def Schedule(master, delay):
    master.withdraw()
    Start_Algo(cap, per, ded, delay)
    master.destroy()
    
def Start_Algo(capacity, period, deadline,delay):
    size=int(sizeEntry.get())
    if(algMenu.get()=='Earliest DeadLine First'):
        work.edf(capacity,deadline,period,size,drawData,delay,canvas,root)
    if algMenu.get() == 'Rate Monotonic Scheduling':
        work.rms(capacity,period,size,drawData,delay,canvas,root)
    if(algMenu.get() == 'Deadline Monotonic Scheduling'):
        work.dms(capacity, deadline, period, size, drawData, delay, canvas, root)
    if(algMenu.get() == 'Round Robin'):
        work.rr(a_t, b_t, size, drawData, delay, canvas, root)
    if (algMenu.get() == 'Shortest Job First(premptive)'):
        work.sjfp(a_t, b_t, size, drawData, delay, canvas, root)
    if(algMenu.get() == 'Shortest Job First(Non premptive)'):
        work.sjfnp(a_t, b_t, size, drawData, delay, canvas, root)


def Enter():
    cap.clear()
    ded.clear()
    per.clear()
    canvas.delete("all")
    size=int(sizeEntry.get())
    string=selected_alg.get()
    master=Tk()    
    master.config(bg='#990033')
    frame = Frame(master, width= 600, height=1000, bg='#990033')
    frame.grid(row=0, column=0, padx=10, pady=5)
    
    if string=='Earliest DeadLine First':
        master.title("Earliest DeadLine First");

        Label(frame, text="Capacity" ,bg='#990033',foreground='white').grid(row=0, column=1, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            p='process',i+1
            Label(frame, text=p ,bg='#990033',foreground='black').grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
            cap.append(Entry(frame))
            cap[i].grid(row=i+1,column=1,padx=5,pady=5)
    
        Label(frame, text="DeadLine" ,bg='#990033',foreground='white').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            ded.append(Entry(frame))
            ded[i].grid(row=i+1,column=2,padx=5,pady=5)
    
        Label(frame, text="Period" ,bg='#990033',foreground='white').grid(row=0, column=3, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            per.append(Entry(frame))
            per[i].grid(row=i+1,column=3,padx=5,pady=5)
    
        speedScale = Scale(master,from_=0.1,to=5.0,length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Delay in Sec [s]")
        speedScale.grid(row=size+2, column=0, padx=5, pady=5)
        Button(master, text="Schedule", command =lambda:Schedule(master,speedScale.get()) , bg='grey').grid(row=size+3, column=0, padx=5, pady=5)
            
    
    if string=='Rate Monotonic Scheduling':
        master.title("Rate Monotonic Scheduling");

        Label(frame, text="Capacity" ,bg='#990033',foreground='white').grid(row=0, column=1, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            p='process',i+1
            Label(frame, text=p ,bg='#990033',foreground='black').grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
            cap.append(Entry(frame))
            cap[i].grid(row=i+1,column=1,padx=5,pady=5)
    
        Label(frame, text="Period" ,bg='#990033',foreground='white').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            per.append(Entry(frame))
            per[i].grid(row=i+1,column=2,padx=5,pady=5)
       
        speedScale = Scale(master,from_=0.1,to=5.0,length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Delay in Sec [s]")
        speedScale.grid(row=size+1, column=0, padx=5, pady=5)
        Button(master, text="Schedule", command =lambda:Schedule(master,speedScale.get()) , bg='grey').grid(row=size+2, column=0, padx=5, pady=5)
        
    if string=='Deadline Monotonic Scheduling':
        master.title("Deadline Monotonic Scheduling");

        Label(frame, text="Capacity" ,bg='#990033',foreground='white').grid(row=0, column=1, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            p='process',i+1
            Label(frame, text=p ,bg='#990033',foreground='black').grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
            cap.append(Entry(frame))
            cap[i].grid(row=i+1,column=1,padx=5,pady=5)
    
        Label(frame, text="DeadLine" ,bg='#990033',foreground='white').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            ded.append(Entry(frame))
            ded[i].grid(row=i+1,column=2,padx=5,pady=5)
    
        Label(frame, text="Period" ,bg='#990033',foreground='white').grid(row=0, column=3, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            per.append(Entry(frame))
            per[i].grid(row=i+1,column=3,padx=5,pady=5)
    
        speedScale = Scale(master,from_=0.1,to=5.0,length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Delay in Sec [s]")
        speedScale.grid(row=size+2, column=0, padx=5, pady=5)
        Button(master, text="Schedule", command =lambda:Schedule(master,speedScale.get()) , bg='grey').grid(row=size+3, column=0, padx=5, pady=5)
                    
 
    if string=='Round Robin':
        master.title("Round Robin");

        Label(frame, text="Arrival time" ,bg='#990033',foreground='white').grid(row=0, column=1, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            p='process',i+1
            Label(frame, text=p ,bg='#990033',foreground='black').grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
            a_t.append(Entry(frame))
            a_t[i].grid(row=i+1,column=1,padx=5,pady=5)
    
        Label(frame, text="Burst time" ,bg='#990033',foreground='white').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            b_t.append(Entry(frame))
            b_t[i].grid(row=i+1,column=2,padx=5,pady=5)
       
        speedScale = Scale(master,from_=0.1,to=5.0,length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Delay in Sec [s]")
        speedScale.grid(row=size+1, column=0, padx=5, pady=5)
        Button(master, text="Schedule", command =lambda:Schedule(master,speedScale.get()) , bg='grey').grid(row=size+2, column=0, padx=5, pady=5)
        

    if string=='Shortest Job First(premptive)':
        clear()
        master.title("Shortest Job First");

        Label(frame, text="Arrival time" ,bg='#990033',foreground='white').grid(row=0, column=1, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            p='process',i+1
            Label(frame, text=p ,bg='#990033',foreground='black').grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
            a_t.append(Entry(frame))
            a_t[i].grid(row=i+1,column=1,padx=5,pady=5)
    
        Label(frame, text="Burst time" ,bg='#990033',foreground='white').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            b_t.append(Entry(frame))
            b_t[i].grid(row=i+1,column=2,padx=5,pady=5)
       
        speedScale = Scale(master,from_=0.1,to=5.0,length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Delay in Sec [s]")
        speedScale.grid(row=size+1, column=0, padx=5, pady=5)
        Button(master, text="Schedule", command =lambda:Schedule(master,speedScale.get()) , bg='grey').grid(row=size+2, column=0, padx=5, pady=5)
     
    if string=='Shortest Job First(Non premptive)':
        clear()
        master.title("Shortest Job First");

        Label(frame, text="Arrival time" ,bg='#990033',foreground='white').grid(row=0, column=1, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            p='process',i+1
            Label(frame, text=p ,bg='#990033',foreground='black').grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
            a_t.append(Entry(frame))
            a_t[i].grid(row=i+1,column=1,padx=5,pady=5)
    
        Label(frame, text="Burst time" ,bg='#990033',foreground='white').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        for i in range(0,size):
            b_t.append(Entry(frame))
            b_t[i].grid(row=i+1,column=2,padx=5,pady=5)
       
        speedScale = Scale(master,from_=0.1,to=5.0,length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Delay in Sec [s]")
        speedScale.grid(row=size+1, column=0, padx=5, pady=5)
        Button(master, text="Schedule", command =lambda:Schedule(master,speedScale.get()) , bg='grey').grid(row=size+2, column=0, padx=5, pady=5)
               
#frame / base lauout
UI_frame = Frame(root, width= 220, height=300, bg='#990033')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=400, height=600, bg='#CCCC99')
canvas.grid(row=0, column=2, padx=10, pady=5)
#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='#990033',fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Earliest DeadLine First', 'Rate Monotonic Scheduling' , 'Deadline Monotonic Scheduling' ,'Round Robin', 'Shortest Job First(premptive)' , 'Shortest Job First(Non premptive)'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

#process
Label(UI_frame, text="Number Of Process ", bg='#990033',fg='white').grid(row=1, column=0, padx=5, pady=10, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=10, sticky=W)
Button(UI_frame, text="Enter", command = Enter , bg='grey').grid(row=2, column=0, padx=5, pady=5)

root.mainloop()

