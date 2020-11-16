from tkinter import *
from TSHistory import thingspeak_read
from TSCommand import thingspeak_write



ID = 1162635
READ_KEY="XXNMKPPU1BIUDEHT"
WRITE_KEY="0SRNSG4FBAVGI7TR"


# Functions
def systemUpToDate():
    label.set("System Status: Up to date")
    thingspeak_write(isArmed.get(), isLocked.get(), isCamera.get(), isBuzzer.get(), isMotion.get(), WRITE_KEY)
    
def systemNotUpToDate():
    label.set("System Status: NOT up to date")
    
def readHistory():
    openHistory()
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
window.minsize(520,500)
window.maxsize(520,500)

#Title
Label(window, text="Welcome to your SafeHouse", bg= "black", fg= "lime", font= "none 20 bold").place(x=65, y=10)

##SYSTEM STATUS
#Subtitle
label = StringVar()
label.set("System Status: Up to date")
status = Label(window, textvariable=label, bg= "black", fg= "lime", font= "none 15 bold").place(x=125, y=60)

#Adding checkbuttons
isArmed = IntVar()
isLocked = IntVar()
isCamera = IntVar()
isBuzzer = IntVar()
isMotion = IntVar()
Checkbutton(window, text= "Arm", variable= isArmed, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=100)
Checkbutton(window, text= "Lock", variable= isLocked, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=160)
Checkbutton(window, text= "Camera", variable= isCamera, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=220)
Checkbutton(window, text= "Buzzer", variable= isBuzzer, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=280)
Checkbutton(window, text= "Motion", variable= isMotion, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=340)

#Adding submit button
submit = Button(window, text="Update System Status", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemUpToDate).place(x=50, y=420)


##SYSTEM HISTORY BUTTON
def openHistory():  
    # Toplevel object which will  
    # be treated as a new window 
    history = Toplevel(window)
    # sets the title of the 
    # Toplevel widget 
    history.title("User History") 
    # sets the geometry of toplevel 
    history.minsize(700,220)
    # A Label widget to show in toplevel 
    Label(history,  
          text ="Pull History of User With Unique ID", font="none 16 bold").pack()
    
    #History Labels     
    Label(history, textvariable=log, justify= LEFT, padx= 2, pady= 2, bg="grey").place(x=120, y=90)
log = StringVar()    
submit = Button(window, text="Request History", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= readHistory).place(x=270, y=420)


window.mainloop()