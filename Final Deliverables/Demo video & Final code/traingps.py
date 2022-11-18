import wiotp.sdk.device 
import time 
import random 
myConfig = { 
    "identity": { 
        "orgId": "iqhx38", 
        "typeId": "iot", 
        "deviceId":"iot" 
    },
    "auth": {
        "token": "714019106015" 
    }
 }

def myCommandCallback (cmd):
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
                                                                   
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None) 
client.connect()
                                                                   
def pub (data):
    client.publishEvent(eventId="status", msgFormat="json", data=myData,onPublish=None)
    print ("Published data Successfully: %s", myData) 
while True: 
    myData={'name': 'Ernakulam Exp', 'lat': 10.9973, 'lon': 76.9664} 
    pub (myData)
    print("Coimbatore station")
    time.sleep (4)
    myData={'name': 'Ernakulam Exp', 'lat': 13.0827, 'lon': 80.2755} 
    pub(myData)
    print("Chennai MGR station")
    time.sleep(4)
    myData={'name': 'Ernakulm Exp', 'lat': 16.5180, 'lon': 80.6195} 
    pub (myData)
    print("Vijayawada station")
    time.sleep (5) 
    myData={'name': 'Ernakulam Exp', 'lat': 20.266762, 'lon': 85.843425} 
    pub (myData)
    print("Bhubaneswar station")
    time.sleep (3) 
    myData={'name': 'Ernakulam Exp', 'lat': 22.5839, 'lon': 88.3434} 
    pub (myData)
    print("Howrah station")
    time.sleep (5) 
    client.commandCallback = myCommandCallback 
client.disconnect ()
