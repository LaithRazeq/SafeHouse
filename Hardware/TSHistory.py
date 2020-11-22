import urllib.request
import json
import requests
import threading
import datetime
soso = datetime.datetime.now()
d=(str(soso.year)+'-'+str(soso.month)+'-'+str(soso.day))
t=(str(soso.hour)+':'+str(soso.minute)+':'+str(soso.second))

def thingspeak_write(id_num:int, date:str, time:str, sensor_type:str, save_location:str, write_key:str):
    
    val1=id_num
    val2=date   
    val3=time
    val4=sensor_type
    val5=save_location
    URL ='https://api.thingspeak.com/update?api_key='
    KEY= write_key
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(val1, val2, val3, val4, val5)
    NEW_URL=URL+KEY+HEADER
   
    data= urllib.request.urlopen(NEW_URL)
 




def thingspeak_read(read_key:str,id_num: str, num_entries:str)->str:
    URL = 'https://api.thingspeak.com/channels/'+id_num+'/feeds.json?api_key='
    KEY= read_key
    HEADER='&results='
    NEW_URL=URL+KEY+HEADER+num_entries
    
    
    get_data=requests.get(NEW_URL).json()
    
    
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
    return t 

   
ID = '1162635' # TS History ID

READ_KEY="XXNMKPPU1BIUDEHT" # TS History Read Key
WRITE_KEY="0SRNSG4FBAVGI7TR"# TS Command Write Key
WRITE_KEY_H="Y10RFX27NP5XFP5L"

last_history_entry = thingspeak_read(READ_KEY, ID, "1")