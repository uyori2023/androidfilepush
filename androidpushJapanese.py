import subprocess

def pushflie(): #push関数
    one = "/storage/emulated/0/Download"
    filepas = input("送信したいファイルのパスを入力してください ")
    print("1."+one)
    print("2.その他")
    devpas = input("保存したいデバイス側のパスを選択してください ")
    if devpas == "1":
        print("送信しています")
        sendcm = "adb push" + " " + filepas + " " + one
        print(sendcm)
        sendcode = subprocess.call(sendcm)
        startpross()

def Connectdevice(): #ワイヤレスデバック接続関数
    print("ipアドレス:ポート" )
    ip = input("ipアドレスとポートを上記のように入力してください ")
    print("接続しています")
    cm = "adb pair " + ip
    connectcode = subprocess.call(cm)
    print("完了!")
    startpross()

def sysexit(): #終了処理
    exitcm = "adb kill-server"
    killservercode = subprocess.call(exitcm)
    print("adbサーバーを停止しています")
    print("完了!")
    exit()

def devices():
    dcm = "adb devices"
    decicescode = subprocess.call(dcm)
    startpross()

def startpross(): #操作受付関数
    print("1.ワイヤレスデバックでデバイスと接続")
    print("2.デバイス一覧を表示")
    print("3.pushを行う")
    print("4.終了")
    con = input("行いたい操作を選択してください ")
    if con == "1":
        Connectdevice()
    elif con == "2":
        devices()
    elif con == "3":
        pushflie()
    elif con == "4":
        sysexit()

#adbサーバーの起動と開始処理
print("adbサーバーを起動しています")
startcm = "adb start-server"
startservercode = subprocess.call(startcm)
print("完了!")
print("androidfilepushprototypeへようこそ！ 作者うよりみ")
startpross()
