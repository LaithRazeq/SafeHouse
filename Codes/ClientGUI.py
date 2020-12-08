"""
This file runs the Client GUI and all its functionalities, to start run the 
script and enter 1 to start or 0 to exit. This file could run on a computer or a
RPI.

Author(s): Ahmed Abdelrazik, Laith Abdelrazeq 
Co-Author(s): NA
Last Modified: 8-DEC-2020
"""
from tkinter import *
from TSHistory import thingspeak_read_h
from TSCommand import thingspeak_write_c

##ThingSpeak Channels' Information 

ID = '1162635' # TS History ID
READ_KEY="XXNMKPPU1BIUDEHT" # TS History Read Key
WRITE_KEY="0SRNSG4FBAVGI7TR"# TS Command Write Key


## Functions

def systemUpToDate()->int:
    '''
    Returns 1 if successful, this function updates the system status label and 
    writes to the TS Command Channel. 
    '''
    thingspeak_write_c(isArmed.get(), isLocked.get(), isCamera.get(), isBuzzer.get(), isMotion.get(), isFlame.get(), WRITE_KEY)
    label.set("System Status: Up to date")
    return 1
    

    
def systemNotUpToDate()->int:
    '''
    Returns 1 if successful, this function updates the system status label. 
    '''
    label.set("System Status: NOT up to date")
    return 1
    
    
   

def readHistory()->int:
    '''
    Returns 1 if successful, This function reads the TS History channel and 
    updates the log variable which is later on showed in the GUI, this function 
    uses TS History.py file.
    '''
    log.set("")
    arr = thingspeak_read_h(READ_KEY,ID, num_entries.get())
    history= ""
    for x in arr:
        for i in range(5):
            temp=""
            temp+="ID: "
            temp+=(str(x[0]))
            temp+=", Date: "
            temp+=(str(x[1]))
            temp+=", Time: "
            temp+=(str(x[2]))
            temp+=", Sensor: "
            temp+=(str(x[3]))
            temp+=", Video_location: "
            temp+=(str(x[4]))              
        history+= temp +'\n\n'
    log.set(history)
    return 1
   

## GUI

# Create main window
window = Tk()
window.title("SafeHouse")
window.configure( background="Black")

#Seting window's size
window.minsize(520,560)
window.maxsize(520,560)

#Title
Label(window, text="Welcome to your SafeHouse", bg= "black", fg= "lime", font= "none 20 bold").place(x=65, y=10)

#SYSTEM STATUS
#System Status Subtitle
label = StringVar()
label.set("System Status: Up to date")
system_status = Label(window, textvariable=label, bg= "black", fg= "lime", font= "none 15 bold").place(x=125, y=60)


#Adding checkbuttons
isArmed = IntVar()
isLocked = IntVar()
isCamera = IntVar()
isBuzzer = IntVar()
isMotion = IntVar()
isFlame = IntVar()
Checkbutton(window, text= "Arm", variable= isArmed, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=100)
Checkbutton(window, text= "Lock", variable= isLocked, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=160)
Checkbutton(window, text= "Camera", variable= isCamera, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=220)
Checkbutton(window, text= "Buzzer", variable= isBuzzer, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=280)
Checkbutton(window, text= "Motion", variable= isMotion, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=340)
Checkbutton(window, text= "Flame", variable= isFlame, bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemNotUpToDate).place(x=135, y=400)

#Adding submit button
submit = Button(window, text="Update System Status", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= systemUpToDate).place(x=50, y=480)


#REQUEST HISTORY BUTTON
def openHistory():
    '''
    This function creates a new window when the "Request History" button is clicked.
    '''         
    # Toplevel object which will be treated as a new window 
    history = Toplevel(window)
    
    # sets the title of the Toplevel widget 
    history.title("User History") 
    
    # sets the geometry of toplevel 
    history.minsize(700,220)
    
    # A Label widget to show in toplevel 
    Label(history,  text ="Select Number of History Entries", font="none 16 bold").pack()
    
    # Option meneu for choosing number of entries  
    OptionMenu(history, num_entries, "1","5", "10","15","20").place(x=300, y=30)
    
    #History Labels     
    Label(history, textvariable=log, justify= LEFT, padx= 1, pady= 1, bg="grey").place(x=120, y=70)
    Button(history, text="Request", fg= "black", font= "none 12 bold", width=10, height=1, command= readHistory).place(x=360, y=30)
        
    
#Get Request History BUTTON
#Initilaizing all variables and drop menus
num_entries = StringVar()
log = StringVar()    
submit = Button(window, text="Request History", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= openHistory).place(x=270, y=480)


## Main Script

x = int(input("To start system press 1/ Press 0 to quit: "))
if x==1:
    window.mainloop()
else:
    print("bye")