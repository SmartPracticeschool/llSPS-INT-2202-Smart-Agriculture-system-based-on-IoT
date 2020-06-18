import time
import sys
import ibmiotf.application
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "9y5mnq" #replace the ORG ID
deviceType = "smartagriculture"#replace the Device type wi
deviceId = "abhi123"#replace Device ID
authMethod = "token"
authToken = "12345678" #Replace the authtoken
            
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        T=50;
        H=32;
	ot=45
        #Send Temperature & Humidity to IBM Watson
        data = {'d':{ 'Temperature' : T, 'Humidity': H,'objTemp':ot }}
        #print data
        def myOnPublishCallback():
            print (data, "to IBM Watson")

        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
# Disconnect the device and application from the cloud
deviceCli.disconnect()
