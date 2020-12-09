# SafeHouse
The SafeHouse is our innovative project designed to keep you safe. This is an RPI based project. This readme file will discuss how to get started with using the SafeHouse.

Getting Started:
1.  Install tkinter library: All GUI are made using tkinter. All the GUI files could run on a computer or an RPI.
2.  Install sqllite3: The UsersDatabase.py file uses this library.
3.  Install requests library: The TSCommand.py & TSHistory.py both use this library.
4.  Install the folder Codes from the repo on the laptop/computer and on the RPI.
5.  Setup two ThingSpeak Channels. One Channel will be called History the other one is the Command channel.
6.  Before running the ClientGUI.py, you will need to go in the file and modify ID, READ_KEY and WRITE_KEY. The ID is the History channel ID, the READ_KEY is the History Channel read key, and the WRITE_KEY is the Command channel write key.
7.  Now the Client GUI is setup you can run the GUI by running the script and clicking 1 to start the GUI. This GUI should run on your laptop/computer (could run on an RPI as well).
8.  The Client GUI has two main functionalites which are to control the hardware on the RPI(you will need to setup the Controller.py first) and by reading history from the TS History Channel, you can specify how many history logs you would like to see (History needs to be recorded first) 
9.  Before running the Controller.py, you need to have all the hardware and connect them appropriatly, Each of the Hardware files will say which Pin on the RPI it should be connected to. You will also need to go in the file and modify ID, READ_KEY and WRITE_KEY. The ID is the Command channel ID, the READ_KEY is the Command Channel read key, and the WRITE_KEY is the History channel write key.
10. Now the RPI is setup you can run the controller by running the script and clicking 1 to start, it needs to run on the RPI.
11. The main functionality of the Controller script is to run all the hardware and integrate all the hardware scripts and take action upon the activation and triggering of the sensors.
12. The AdminGUI.py doesn't need any modifications to work. However, to be able to use all its features you will need to setup the sql database "users.db" which will contain the all the information regarding the clients, all the fields can be seen when you click on the "Add New User" button, all the fields should be of type string(Text).
13. To run the Admin GUI run the script and click 1 to start. This GUI should run on a laptop/computer(could run on an RPI as well)
14. The main functioniality of the AdminGUI is to add a new users to the locally saved sql database "users.db", or edit exisiting users from the same database using their ID, or requesting the history of a specific user using their ID.


Well Done, you have now setup the SafeHouse. If you would like to test all the files a Testing class has been developed using the unittest framework, just run the unitTests.py on the RPI and you could easily check if all the functions are working properly if not a comment will be printed out specifying which function caused the error. 

ENJOY THE SAFEHOUSE!