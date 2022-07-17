# import time
from tkinter import *
# import math
# import folium
#from PIL import Image, ImageTk
# import os
# import serial
# import threading as thr
# _PORT_ = '/dev/ttyUSB0'
# first12=0
# last6=0
# _END_FLAG_=0

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("705x650")  # Screen Size
        self.window.resizable(0, 0)
        self.window.title("ALFA-ETA-HYPER")  # Pencere ismi
        self.window.iconname("ALFA-ETA-HYPER")
        self.window.config(background="white")
        photo = PhotoImage(file="Images/logo.png")  # app icon
        self.window.iconphoto("false", photo)
        self.pressure = Pressure(self)
        self.temperature = Temperature(self)
        self.speed = Speed(self)
        self.acc = Acceleration(self)
        self.location = Location(self)
        self.logo = Logo(self)
        self.maneuver = Maneuver(self)
        self.power = Power(self)
        # self.readData = thr.Thread(target=self.readAndParseDATA)
        # self.readData.start()

        
    # def connectUSB(self):
    #     ser = serial.Serial(
    #         # Serial Port to read the data from
    #         port=_PORT_,
    #         #Rate at which the information is shared to the communication channel
    #         baudrate=9600,
    #         #Applying Parity Checking (none in this case)
    #         parity=serial.PARITY_NONE,
    #         # Pattern of Bits to be read
    #         stopbits=serial.STOPBITS_ONE,
    #         # Total number of bits to be read
    #         bytesize=serial.EIGHTBITS,
    #         # Number of serial commands to accept before timing out
    #         timeout=1
    #     )
    #     return ser
    # def readAndParseDATA(self):
    #     while(getFlag() == 0):
    #         try:
    #             self.serialCon = self.connectUSB()
    #         except serial.SerialException:
    #             time.sleep(3)
    #             pass
    #         else:
    #             while(getFlag()==0):
    #                 x = self.serialCon.readline()
    #                 #print(x)
    #                 datas=str(x).split(":")
    #                 paket = datas[0][2:4]
    #                 if paket == '1':  # Battery 0 - 12
    #                     paket1(self,datas[1])
    #                 if paket == '2':  # Battery 12 - 18  + Left -Right Signal +Motor +Leakage Signal+Amper+Volt+pil Temp. 
    #                     paket2(self, datas[1])
    #                 if paket == '3':# direksiyon + konum
    #                     paket3(self, datas[1])
    #             self.serialCon.close()
class Logo:
    def __init__(self, obj):
        self.logoCanvas = Canvas(obj.window, height=145, width=145, background="blue", highlightthickness=3)
        self.photo = PhotoImage(file="Images/logo.png")
        self.logoCanvas.create_image(75,74, image=self.photo, anchor=CENTER)
        self.logoCanvas.place(x=450, y=340)
        #self.numberCanvas = Canvas(obj.window, height=100, width=150, background="white", highlightthickness=0)
        # self.numberPhoto = PhotoImage(file="Images/44.png")
        # self.numberCanvas.create_image(75, 50, image=self.numberPhoto, anchor=CENTER)
        # self.numberCanvas.place(x=275, y=410)
class Pressure:
    def __init__(self, obj):
        self.pressureCanvas = Canvas(obj.window, height=25, width=300,background="white", highlightthickness=1)
        self.pressureCanvas.place(x=0, y=0)
        self.p_txt = self.pressureCanvas.create_text(60, 15, fill="black", text="Pressure: ", font=('Helvetica 16 bold'))
        self.value_txt = self.pressureCanvas.create_text(200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        # self.imageCanvas = Canvas(obj.window, height=300, width=300,background="red", highlightthickness=1)
        # self.imageCanvas.place(x=400, y=0)

class Power:
    def __init__(self, obj):
        self.powerCanvas = Canvas(obj.window, height=150, width=140, background="white", highlightthickness=1)
        self.powerCanvas.place(x=150, rely=1,anchor=SW)
        self.photo = PhotoImage(file="Images/bolt.png")
        self.powerCanvas.create_image(25, 0, image=self.photo, anchor=NW)
        self.p_txt = self.powerCanvas.create_text(10, 90, fill="black", text="      Power\nConsumption", font=('Helvetica 14 bold'),anchor=NW)
        self.value_txt = self.powerCanvas.create_text(70, 140, fill="black", text="0", font=('Helvetica 14 roman'),anchor=CENTER)
class Temperature:
    def __init__(self, obj):
        # self.thermometer = [PhotoImage(
        #     file='Images/thermometer_ok.png'), PhotoImage(file='Images/thermometer_bad.png')]
        self.p1Canvas = Canvas(obj.window, height=25, width=300, background="white", highlightthickness=1)
        # self.p1Canvas.create_image(25, 26, image=self.temperaturemeter[0], anchor=CENTER)
        self.p1 = self.p1Canvas.create_text(
            100, 15, fill="black", text="P1 - Temperature: ", font=('Helvetica 16 bold'))
        self.p1 = self.p1Canvas.create_text(200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.p1Canvas.place(x=0, y=25)
        self.p2Canvas = Canvas(
            obj.window, height=25, width=300, background="white", highlightthickness=1)
        # self.p2Canvas.create_image(25, 26, image=self.temperaturemeter[0], anchor=CENTER)
        self.p1 = self.p2Canvas.create_text(
            100, 15, fill="black", text="P2 - Temperature: ", font=('Helvetica 16 bold'))
        self.p1 = self.p2Canvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.p2Canvas.place(x=0, y=50)
        
class Speed:
    def __init__(self, obj):
        #SPEED Canvas
        self.xCanvas = Canvas(obj.window, height=25, width=300, background="white", highlightthickness=1)
        self.xCanvas.place(x=0, y=75)
        self._X_ = self.xCanvas.create_text(60, 15, fill="black", text="X-Speed: ", font=('Helvetica 16 bold'))
        self._X_Speed = self.xCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.yCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.yCanvas.place(x=0, y=100)
        self._Y_ = self.yCanvas.create_text(60, 15, fill="black", text="Y-Speed: ", font=('Helvetica 16 bold'))
        self._Y_Speed = self.yCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.zCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.zCanvas.place(x=0, y=125)
        self._Z_ = self.zCanvas.create_text(
            60, 15, fill="black", text="Z-Speed: ", font=('Helvetica 16 bold'))
        self._Z_Speed = self.zCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        # self.imageCanvas = Canvas(obj.window, height=300, width=300,background="red", highlightthickness=1)
        # self.imageCanvas.place(x=400, y=0)
        # self.speedometer = PhotoImage(file='Images/speedometer.png')
        # self.speedCanvas.create_image(
        #     103, 52, image=self.speedometer, anchor=CENTER)
        # coord = 2, 200, 200, 2
        # self.speedCanvas.create_arc(coord, start=0, extent=180, width=2)
        #SPEED Arrow
        # self.speedArrow = self.speedCanvas.create_line(
        #     100, 100, 0, 100, arrow=LAST, width=5, fill="blue")
        # self.angle = 90
        # self.speedTxt = self.speedCanvas.create_text(
        #     100, 65, fill="black", text="0", font=('Helvetica 20 bold'))

class Acceleration:
    def __init__(self, obj):
        self.xCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.xCanvas.place(x=0, y=150)
        self._X_ = self.xCanvas.create_text(
            60, 15, fill="black", text="X-Acc: ", font=('Helvetica 16 bold'))
        self._X_Acc = self.xCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.yCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.yCanvas.place(x=0, y=175)
        self._Y_ = self.yCanvas.create_text(
            60, 15, fill="black", text="Y-Acc: ", font=('Helvetica 16 bold'))
        self._Y_Acc = self.yCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.zCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.zCanvas.place(x=0, y=200)
        self._Z_ = self.zCanvas.create_text(
            60, 15, fill="black", text="Z-Acc: ", font=('Helvetica 16 bold'))
        self._Z_Acc = self.zCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
class Location:
    def __init__(self, obj):
        self.xCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.xCanvas.place(x=0, y=225)
        self._X_ = self.xCanvas.create_text(
            60, 15, fill="black", text="X-Loc: ", font=('Helvetica 16 bold'))
        self._X_Loc = self.xCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.yCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.yCanvas.place(x=0, y=250)
        self._Y_ = self.yCanvas.create_text(
            60, 15, fill="black", text="Y-Loc: ", font=('Helvetica 16 bold'))
        self._Y_Loc = self.yCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.zCanvas = Canvas(obj.window, height=25, width=300,
                              background="white", highlightthickness=1)
        self.zCanvas.place(x=0, y=275)
        self._Z_ = self.zCanvas.create_text(
            60, 15, fill="black", text="Z-Loc: ", font=('Helvetica 16 bold'))
        self._Z_Loc = self.zCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
class Maneuver:
    def __init__(self, obj):
        #roll, pitch ve yaw
        self.pitchCanvas = Canvas(obj.window, height=25, width=300,
                                background="white", highlightthickness=1)
        self.pitchCanvas.place(x=0, y=225)
        self._Pitch_ = self.pitchCanvas.create_text(
            60, 15, fill="black", text="Pitch: ", font=('Helvetica 16 bold'))
        self._Pitch_Deg = self.pitchCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.rollCanvas = Canvas(obj.window, height=25, width=300,
                                background="white", highlightthickness=1)
        self.rollCanvas.place(x=0, y=250)
        self._Roll_ = self.rollCanvas.create_text(
            60, 15, fill="black", text="Roll: ", font=('Helvetica 16 bold'))
        self._Roll_Deg = self.rollCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.yawCanvas = Canvas(obj.window, height=25, width=300,
                                background="white", highlightthickness=1)
        self.yawCanvas.place(x=0, y=275)
        self._Yaw_ = self.yawCanvas.create_text(
            60, 15, fill="black", text="Yaw: ", font=('Helvetica 16 bold'))
        self._Yaw_Deg = self.yawCanvas.create_text(
            200, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        
# class Location:
#     def __init__(self, obj):
#         self.location = [40.806649, 29.359085]  # x,y
#         self.locationCanvas = Canvas(obj.window, height=25, width=300,
#                                      background="white", highlightthickness=1)
#         self.locationCanvas.place(x=400, y=300)
#         self._X_ = self.locationCanvas.create_text(
#             20, 15, fill="black", text="X: ", font=('Helvetica 16 bold'))
#         self._Y_ = self.locationCanvas.create_text(
#             160, 15, fill="black", text="Y: ", font=('Helvetica 16 bold'))
#         self._X_Loc = self.locationCanvas.create_text(
#             40, 15, fill="black", text=str(self.location[0]), font=('Helvetica 14 roman'), anchor=W)
#         self._Y_Loc = self.locationCanvas.create_text(
#             180, 15, fill="black", text=str(self.location[1]), font=('Helvetica 14 roman'), anchor=W)
#         self.imageCanvas = Canvas(obj.window, height=300, width=300,background="red", highlightthickness=1)
#         self.imageCanvas.place(x=400, y=0)
               
#     def changeLoc(self, obj, locs):
#         self.location = locs
#         self.locationCanvas.delete(self._X_Loc)
#         self.locationCanvas.delete(self._Y_Loc)
#         self._X_Loc = self.locationCanvas.create_text(
#             40, 15, fill="black", text=str(locs[0]), font=('Helvetica 14 roman'), anchor=W)
#         self._Y_Loc = self.locationCanvas.create_text(
#             180, 15, fill="black", text=str(locs[1]), font=('Helvetica 14 roman'), anchor=W)
#         obj.window.update()
# def changeSpeed(obj):
#     for i in range(0, 80):
#         updateSpeed(obj, i)
#     for i in range(80, 40, -1):
#         updateSpeed(obj, i)
#     for i in range(40, 100):
#         updateSpeed(obj, i)
#     for i in range(100, 0, -1):
#         updateSpeed(obj, i)
# def changeLoc(obj):
#     updateLoc(obj, [40.807712, 29.355991])
# def updateLoc(obj,loc):
#     obj.location.changeLoc(obj, loc)
# def updateSpeed(obj, speed=0):
#     if (obj.speedometer.angle < 270) or (obj.speedometer.angle > 90):
#         obj.speedometer.angle = 90 + 1.8*speed
#         #obj.speedometer.angle += 1.8
#         x = 100 - 100*math.sin(math.radians(obj.speedometer.angle))
#         y = 100 + 100*math.cos(math.radians(obj.speedometer.angle))
#         obj.speedometer.speedCanvas.delete(obj.speedometer.speedTxt)
#         obj.speedometer.speedCanvas.delete(obj.speedometer.speedArrow)
#         obj.speedometer.speedTxt = obj.speedometer.speedCanvas.create_text(100, 65, fill="black", text=str(
#             int((obj.speedometer.angle-90)/1.8)), font=('Helvetica 20 bold'))
#         obj.speedometer.speedArrow = obj.speedometer.speedCanvas.create_line(
#             100, 100, 0 + x, y, arrow=LAST, width=5, fill="blue")
#     obj.window.update()

# def colorPicker(charge):
#     if charge < 20:
#         return "#A10000"
#     elif charge < 40:
#         return "#C25F00"
#     elif charge < 60:
#         return "#E2BE00"
#     elif charge < 80:
#         return "#AAB900"
#     else:
#         return "#71B400"
# def exit_func(obj):
#     setFlag(1)
#     obj.readData.join()
#     obj.mapThread.join()
#     obj.window.destroy()
# def getFlag():
#     global _END_FLAG_
#     return _END_FLAG_    
# def setFlag(i):
#     global _END_FLAG_
#     _END_FLAG_=1
    
# def paket1(obj, datas):
#     sum=0
#     arr= datas.split("\\")[0].split(",")
#     for i in range(0, 2):
#         for j in range(0,5):
#             updateBattery(obj.allBatteries[i][j], int(arr[(5*i)+j]))
#             sum+=int(arr[(5*i)+j])
#     for i in range(0, 2):
#         updateBattery(obj.allBatteries[2][i], int(arr[10+i]))
#         sum += int(arr[10+i])
#     global first12,last6
#     first12=sum
#     updateBattery(obj.mainBattery,(first12+last6)/18)
    
# def paket2(obj, datas):
#     sum=0
#     arr= datas.split("\\")[0].split(",")
#     for i in range(3):
#         updateBattery(obj.allBatteries[2][2+i], int(arr[i]))
#         sum += int(arr[i])
#     for i in range(3):
#         updateBattery(obj.allBatteries[3][i], int(arr[i+3]))
#         sum+=int(arr[i+3])
#     global last6,first12
#     last6=sum
#     updateBattery(obj.mainBattery, (first12+last6)/18)
#     sag=int(arr[6])
#     sol = int(arr[7])
#     kacak = int(arr[8])
#     mot = int(arr[9])
#     amp = int(arr[10])
#     volt = int(arr[11])
#     sicaklik = float(arr[12])
#     changeSignals(obj, [amp,volt,mot, sol, sag, sicaklik,kacak])
#     updateSpeed(obj, int(arr[13]))
    
# def paket3(obj, datas):
#     arr= datas.split("\\")[0].split(",")
#     updateSteer(obj, float(arr[0]))
#     updateLoc(obj, [float(arr[1]), float(arr[2])])

if __name__ == '__main__':
    app = App()
    # app.window.bind("<Up>", lambda event, obj=app: changeSpeed(obj))
    # app.window.bind("<Left>", lambda event, obj=app: changeBattery(obj))
    # app.window.bind("<BackSpace>", lambda event, obj=app: changeSig(obj))
    # app.window.bind("<Down>", lambda event, obj=app: changeLoc(obj))
    # app.window.bind("<Right>", lambda event, obj=app: changeSteer(obj))
    # app.window.protocol('WM_DELETE_WINDOW', lambda obj= app: exit_func(obj))
    app.window.mainloop()
