import urllib.request
import json
import requests
import threading
import datetime
soso = datetime.datetime.now()
d=(str(soso.year)+'-'+str(soso.month)+'-'+str(soso.day))
t=(str(soso.hour)+':'+str(soso.minute)+':'+str(soso.second))

def thingspeak_write(id_num:int, date:str, time:str, sensor_type:str, save_location:str, is_notified:int, write_key:str):
    
    val1=id_num
    val2=date   
    val3=time
    val4=sensor_type
    val5=save_location
    val6=is_notified
    URL ='https://api.thingspeak.com/update?api_key='
    KEY= write_key
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}'.format(val1, val2, val3, val4, val5, val6)
    NEW_URL=URL+KEY+HEADER
   
    data= urllib.request.urlopen(NEW_URL)
 




def thingspeak_read(read_key:str, num_entries:str)->str:
    URL = 'https://api.thingspeak.com/channels/1162635/feeds.json?api_key='
    KEY= read_key
    HEADER='&results='
    NEW_URL=URL+KEY+HEADER+num_entries
   
    
    get_data=requests.get(NEW_URL).json()
    
    channel_id=get_data['channel']['id']
    
    field_1=get_data['feeds']
    
    t=[]
    for x in field_1:
        temp=""
        temp+="ID: "
        temp+=(str(x['field1']))
        temp+=", Date: "
        temp+=(str(x['field2']))
        temp+=", Time: "
        temp+=(str(x['field3']))
        temp+=", Sensor: "
        temp+=(str(x['field4']))
        temp+=", Video_location: "
        temp+=(str(x['field5']))        
        t.append(temp)       
    return t 
    
  