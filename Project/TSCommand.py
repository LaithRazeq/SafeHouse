import urllib.request
import requests



# Define a function that will post on server every 15 Seconds

def thingspeak_write(arm,lock,cam,buzz,move, key):
    isArmed = arm
    isLocked = lock
    isCamera = cam
    isBuzzer = buzz
    isMotion = move
    URl='https://api.thingspeak.com/update?api_key='
    KEY= key
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(isArmed,isLocked,isCamera,isBuzzer,isMotion)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def read_data_thingspeak(key):
    URL='https://api.thingspeak.com/channels/1227483/feeds.json?api_key='
    KEY= key
    HEADER='&results=1'
    NEW_URL=URL+KEY+HEADER

    get_data=requests.get(NEW_URL).json()

    data=get_data['feeds']

    t=[]
    for x in data:
        t.append(x['field1'])
        t.append(x['field2'])
        t.append(x['field3'])
        t.append(x['field4'])
        t.append(x['field5'])               
    return t
