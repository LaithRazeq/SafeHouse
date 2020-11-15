import urllib.request

def thingspeak_post():
    val1="2023"
    val2="3.0"
    val3="123"
    URL = 'https://api.thingspeak.com/update?api_key='
    KEY= 'IOOAC36UJI0C2JFI'
    HEADER='&field1={}&field2={}&field3={}'.format(val1, val2, val3)
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)
    
    data= urllib.request.urlopen(NEW_URL)
    
thingspeak_post()