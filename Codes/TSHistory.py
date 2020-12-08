"""
This file contains the functions which writes and reads from the TS History 
Channel. 

Author(s): Ahmed Abdelrazik 
Co-Author(s): Laith Abdelrazeq
Last Modified: 8-DEC-2020
"""
import urllib.request
import json
import requests
import threading
import datetime

#Reading current date & time
soso = datetime.datetime.now()
d=(str(soso.year)+'-'+str(soso.month)+'-'+str(soso.day))
t=(str(soso.hour)+':'+str(soso.minute)+':'+str(soso.second))

def thingspeak_write_h(id_num:int, date:str, time:str, sensor_type:str, save_location:str, write_key:str)->int:
    '''
    Returns 1 if successful, this function writes the parameters entered to the TS History Channel.
    '''    
    URL ='https://api.thingspeak.com/update?api_key='
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(val1, val2, val3, val4, val5)
    NEW_URL=URL+write_key+HEADER
   
    data= urllib.request.urlopen(NEW_URL)
    return 1
 




def thingspeak_read_h(read_key:str,id_num: str, num_entries:str)->str:
    '''
    Returns an array of arrays of strings, this function takes in read key and
    the id_num which is the channel id and uses this to read from the TS History
    Channel, the function returns an array with lenght of the num_entries 
    specified.
    '''     
    URL = 'https://api.thingspeak.com/channels/'+id_num+'/feeds.json?api_key='
    HEADER='&results='
    NEW_URL=URL+read_key+HEADER+num_entries

    get_data=requests.get(NEW_URL).json()
     
    #Parsing JSON   
    field_1=get_data['feeds']
    
    t=[]
    for x in field_1:
        temp = []
        temp.append(x['field1'])
        temp.append(x['field2'])
        temp.append(x['field3'])
        temp.append(x['field4'])
        temp.append(x['field5'])
        t.append(temp)
    return t # returns array of arrays with the data from thingspeak channel

   
