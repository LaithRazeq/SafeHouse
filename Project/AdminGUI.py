from tkinter import *
from TSHistory import thingspeak_read
from UsersDatabase import read_database


def addNewUser():
    print("ok")


def readHistory():
    log.set("")
    key = read_database(id_num)
    arr = thingspeak_read(key, "10")
    h= ""
    for x in arr:
        h+= x+'\n\n'
    log.set(h)

# Add new user window
def openNewUser():  
    # Toplevel object which will  
    # be treated as a new window 
    newUser = Toplevel(window)
    # sets the title of the 
    # Toplevel widget 
    newUser.title("Add User") 
    # sets the geometry of toplevel 
    newUser.minsize(1100,220)
    newUser.maxsize(1100,220)
    # A Label widget to show in toplevel 
    Label(newUser,  
          text ="Add a New User", font="none 16 bold").pack() 
    
    Label(newUser, text="Id", fg= "black", font= "none 12").place(x=20, y=45)
    iD = Entry(newUser, width=5)
    iD.pack()
    iD.place(x=40,y=50)
    
    Label(newUser, text="Name", fg= "black", font= "none 12").place(x=90, y=45)
    name = Entry(newUser, width=20)
    name.pack()
    name.place(x=140,y=50)
    
    Label(newUser, text="Address", fg= "black", font= "none 12").place(x=280, y=45)
    address = Entry(newUser, width=30)
    address.pack()
    address.place(x=350,y=50) 
    
    Label(newUser, text="Number", fg= "black", font= "none 12").place(x=550, y=45)
    num = Entry(newUser, width=15)
    num.pack()
    num.place(x=615,y=50)
    
    Label(newUser, text="Read", fg= "black", font= "none 12").place(x=720, y=45)
    num = Entry(newUser, width=20)
    num.pack()
    num.place(x=770,y=50)
    
    Label(newUser, text="Write", fg= "black", font= "none 12").place(x=900, y=45)
    num = Entry(newUser, width=20)
    num.pack()
    num.place(x=950,y=50)
     
    Label(newUser, text="Specs:", fg= "black", font= "none 14 bold").place(x=525, y=90)
    newcamera = IntVar()
    newmotion = IntVar()
    newbuzzer = IntVar()
    newfire = IntVar()
    newlock = IntVar()
    
    Checkbutton(newUser, text= "Camera", variable= newcamera, fg= "black", font= "none 14", width=10, height=2).place(x=290, y=115)
    Checkbutton(newUser, text= "Motion", variable= newmotion, fg= "black", font= "none 14", width=10, height=2).place(x=400, y=115)
    Checkbutton(newUser, text= "Buzzer", variable= newbuzzer, fg= "black", font= "none 14", width=10, height=2).place(x=510, y=115)
    Checkbutton(newUser, text= "Fire", variable= newfire, fg= "black", font= "none 14", width=10, height=2).place(x=620, y=115)
    Checkbutton(newUser, text= "Lock", variable= newlock, fg= "black", font= "none 14", width=10, height=2).place(x=730, y=115)
    
    submit = Button(newUser, text="Submit", fg= "black", font= "none 12 bold", width=10, height=1, command= addNewUser).place(x=500, y=170)
      

# Edit user window
def openEditUser():  
    # Toplevel object which will  
    # be treated as a new window 
    editUser = Toplevel(window)
    # sets the title of the 
    # Toplevel widget 
    editUser.title("Edit User") 
    # sets the geometry of toplevel 
    editUser.minsize(1100,220)
    editUser.maxsize(1100,220)
    # A Label widget to show in toplevel 
    Label(editUser,  
          text ="Edit an Existing User With Unique ID", font="none 16 bold").pack()
    
    Label(editUser, text="Id", fg= "black", font= "none 12").place(x=20, y=45)
    iD = Entry(editUser, width=5)
    iD.pack()
    iD.place(x=40,y=50)
    
    Label(editUser, text="Name", fg= "black", font= "none 12").place(x=90, y=45)
    name = Entry(editUser, width=20)
    name.pack()
    name.place(x=140,y=50)
    
    Label(editUser, text="Address", fg= "black", font= "none 12").place(x=280, y=45)
    address = Entry(editUser, width=30)
    address.pack()
    address.place(x=350,y=50) 
    
    Label(editUser, text="Number", fg= "black", font= "none 12").place(x=550, y=45)
    num = Entry(editUser, width=15)
    num.pack()
    num.place(x=615,y=50)
    
    Label(editUser, text="Read", fg= "black", font= "none 12").place(x=720, y=45)
    num = Entry(editUser, width=20)
    num.pack()
    num.place(x=770,y=50)
    
    Label(editUser, text="Write", fg= "black", font= "none 12").place(x=900, y=45)
    num = Entry(editUser, width=20)
    num.pack()
    num.place(x=950,y=50)
     
    Label(editUser, text="Specs:", fg= "black", font= "none 14 bold").place(x=525, y=90)
    newcamera = IntVar()
    newmotion = IntVar()
    newbuzzer = IntVar()
    newfire = IntVar()
    newlock = IntVar()
    
    Checkbutton(editUser, text= "Camera", variable= newcamera, fg= "black", font= "none 14", width=10, height=2).place(x=290, y=115)
    Checkbutton(editUser, text= "Motion", variable= newmotion, fg= "black", font= "none 14", width=10, height=2).place(x=400, y=115)
    Checkbutton(editUser, text= "Buzzer", variable= newbuzzer, fg= "black", font= "none 14", width=10, height=2).place(x=510, y=115)
    Checkbutton(editUser, text= "Fire", variable= newfire, fg= "black", font= "none 14", width=10, height=2).place(x=620, y=115)
    Checkbutton(editUser, text= "Lock", variable= newlock, fg= "black", font= "none 14", width=10, height=2).place(x=730, y=115)
    
    submit = Button(editUser, text="Submit", fg= "black", font= "none 12 bold", width=10, height=1, command= addNewUser).place(x=500, y=170)    



# Request History Window
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
    
    Label(history, text="Insert Desired Id", fg= "black", font= "none 12 bold").place(x=200, y=45)
    id_num = StringVar()
    iD = Entry(history, textvariable= id_num, width=5)
    iD.pack()
    iD.place(x=340,y=47)
    
    
    #History Labels     
    Label(history, textvariable=log, justify= LEFT, padx= 2, pady= 2, bg="grey").place(x=120, y=90)
    
    req = Button(history, text="Request", fg= "black", font= "none 12 bold", width=10, height=1, command= readHistory).place(x=400, y=40)
    
        
    

# Create main window
window = Tk()
window.minsize(300,300)
window.maxsize(300,300)
window.title("SafeHouse Admin")
window.configure( background="Black")
#Title
Label(window, text="ADMIN GUI", bg= "black", fg= "lime", font= "none 20 bold").place(x=75, y=20)
##ADD USER
submit = Button(window, text="Add New User", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= openNewUser).place(x=50, y=80)
##Edit USER
submit = Button(window, text=" Edit User ", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= openEditUser).place(x=50, y=140)
##Get USER History
submit = Button(window, text="Request History", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= openHistory).place(x=50, y=200)
log= StringVar()

window.mainloop()