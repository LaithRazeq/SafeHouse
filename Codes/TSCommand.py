"""
This file contains the functions which writes and reads from the TS Command 
Channel. 

Author(s): Azizul Hasan
Co-Author(s): Ahmed Abdelrazik 
Last Modified: 8-DEC-2020
"""
import urllib.request
import requests



def thingspeak_write_c(isArmed:int, isLocked:int, isCamera:int, isBuzzer:int, isMotion:int, isFlame:int, write_key:str)-> int:
    '''
    Returns 1 if successful, this function writes the parameters entered to the TS Command Channel.
    '''
    URl='https://api.thingspeak.com/update?api_key='
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}'.format(isArmed,isLocked,isCamera,isBuzzer,isMotion, isFlame)
    NEW_URL=URl+write_key+HEADER
    data=urllib.request.urlopen(NEW_URL)
    return 1
    

def thingspeak_read_c(read_key:str, id_num:str)->str:
    '''
    Returns an array of strings, this function takes in read key and the id_num 
    which is the channel id and uses this to read from the TS Command Channel.
    '''    
    URL='https://api.thingspeak.com/channels/'+id_num+'/feeds.json?api_key='
    HEADER='&results=1'
    NEW_URL=URL+read_key+HEADER

    get_data=requests.get(NEW_URL).json()

    data=get_data['feeds']

    t=[]
    for x in data:
        t.append(x['field1'])
        t.append(x['field2'])
        t.append(x['field3'])
        t.append(x['field4'])
        t.append(x['field5'])               
        t.append(x['field6'])                       
    return t #returns an array with most recent data in the TS Channel
