import subprocess

def pushflie(): #push processing
    one = "/storage/emulated/0/Download"
    filepas = input("Specify the path of the file you want to send ")
    print("1."+one)
    print("2.Orher")
    devpas = input("Please select the path on the devices side ")
    if devpas == "1":
        print("Sending...")
        sendcm = "adb push" + " " + filepas + " " + one
        print(sendcm)
        sendcode = subprocess.call(sendcm)
        startpross()

def Connectdevice(): #Wireless back connection function
    print("ipAddress:port" )
    ip = input("Enter the ip address and port as follows " )
    print("connecting...")
    cm = "adb pair " + ip
    connectcode = subprocess.call(cm)
    print("done!")
    startpross()

def sysexit(): #end processing
    exitcm = "adb kill-server"
    killservercode = subprocess.call(exitcm)
    print("Stopping adb server")
    print("done!")
    print("by!")
    exit()

def devices():
    dcm = "adb devices"
    decicescode = subprocess.call(dcm)
    startpross()

def startpross(): #operation-accepted function
    print("1.Connect with wireless debugging")
    print("2.View Device List")
    print("3.Do a push")
    print("4.exit")
    con = input("Select the operation you want to perform ")
    if con == "1":
        Connectdevice()
    elif con == "2":
        devices()
    elif con == "3":
        pushflie()
    elif con == "4":
        sysexit()

#Starting up the adb server and calling the startpross function
print("starting adb server")
startcm = "adb start-server"
startservercode = subprocess.call(startcm)
print("done!")
print("Welcome to androidfilepush prototype Createbyuyori")
startpross()
