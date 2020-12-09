"""
This file contains the functions which writes, reads and edits the locally saved
'users.db' sql database.

Author(s): Azizul Hasan, Ahmed Abdelrazik
Co-Author(s): Laith Abdelrazeq
Last Modified: 8-DEC-2020
"""
import sqlite3


def write_database(id_num:str , name:str , address:str , phone:str , readKey:str , writeKey:str , specs:str):
    '''
    This function writes to users.db which is a local sql database saved locally.
    '''
    dbconnect = sqlite3.connect("users.db");
    dbconnect.row_factory = sqlite3.Row;
    cursor = dbconnect.cursor();
    cursor.execute('''INSERT INTO users values(?, ?, ?, ?, ?, ?, ?);''', (id_num, name, address, phone, readKey, writeKey, specs));
    dbconnect.commit();
    dbconnect.close();


def read_database(id_num:str)->str:
    '''
    Returns the read key using the corrosponding id_num param entered.
    '''
    dbconnect = sqlite3.connect("users.db");
    dbconnect.row_factory = sqlite3.Row;
    cursor = dbconnect.cursor();
    cursor.execute('SELECT * FROM users WHERE ID = ?', (id_num,));
    for row in cursor:
        return(row['readKey']);
    
    
def edit_database(id_num:str , name:str , address:str , phone:str , readKey:str , writeKey:str , specs:str):
    '''
    This function compares id_num param to the id number colmun in users.db 
    and edits this row based on the other param.
    '''
    dbconnect = sqlite3.connect("users.db");
    dbconnect.row_factory = sqlite3.Row;
    cursor = dbconnect.cursor();
    cursor.execute('DELETE FROM users WHERE ID = ?',(id_num,))
    dbconnect.commit()
    dbconnect.close()
    write_database(id_num, name, address, phone, readKey, writeKey, specs)
    
