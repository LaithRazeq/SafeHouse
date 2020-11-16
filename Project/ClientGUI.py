from tkinter import *
from TSHistory import thingspeak_read
from TSCommand import thingspeak_write



ID = 1
READ_KEY="XXNMKPPU1BIUDEHT"
WRITE_KEY="2RPJIJYO785ETAE7"


# Functions
def systemUpToDate():
    label.set("System Status: Up to date")
    thingspeak_write(ID,isArmed, isLocked, isCamera, isBuzzer, isMotion, WRITE_KEY)
    
def systemNotUpToDate():
    label.set("System Status: NOT up to date")
    
def readHistory():
    log.set("")
    arr = thingspeak_read(READ_KEY, "10")
    history= ""
    for x in arr:
        history+= x+'\n\n'
    log.set(history)
   

# Create main window
window = Tk()
window.title("SafeHouse")
window.configure( background="Black")

#Seting window's size
window.geometry("1000x1000")

#Title
Label(window, text="Welcome to your SafeHouse", bg= "black", fg= "lime", font= "none 20 bold").place(x=325, y=10)

##SYSTEM STATUS
#Subtitle
label = StringVar()
label.set("System Status: Up to date")
status = Label(window, textvariable=label, bg= "black", fg= "lime", font= "none 15 bold").place(x=150, y=80)

#Adding checkbuttons
isArmed = IntVar()
isLocked = IntVar()
isCamera = IntVar()
isBuzzer = IntVar()
isMotion = IntVar()
Checkbutton(window, text= "Arm", variable= isArmed, bg="lime", fg= "black", font= "none 12 bold", width=10, height=2, command= systemNotUpToDate).place(x=200, y=150)
Checkbutton(window, text= "Lock", variable= isLocked, bg="lime", fg= "black", font= "none 12 bold", width=10, height=2, command= systemNotUpToDate).place(x=200, y=210)
Checkbutton(window, text= "Camera", variable= isCamera, bg="lime", fg= "black", font= "none 12 bold", width=10, height=2, command= systemNotUpToDate).place(x=200, y=270)
Checkbutton(window, text= "Buzzer", variable= isBuzzer, bg="lime", fg= "black", font= "none 12 bold", width=10, height=2, command= systemNotUpToDate).place(x=200, y=330)
Checkbutton(window, text= "Motion", variable= isMotion, bg="lime", fg= "black", font= "none 12 bold", width=10, height=2, command= systemNotUpToDate).place(x=200, y=390)

#Adding submit button
submit = Button(window, text="Update System Status", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemUpToDate).place(x=161, y=500)


##SYSTEM HISTORY
#subtitle
Label(window, text="System History", bg="black", fg="lime", font="none 15 bold").place(x=675, y=80)

#History Labels
log= StringVar()
log.set("")
historyLog=Label(window, textvariable=log, width=62, height=22, justify= LEFT, padx= 2, pady= 2, wraplength=420,bg="grey").place(x=520, y=135)


#Get History Button
submit = Button(window, text="Request History", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= readHistory).place(x=650, y=500)


window.mainloop()