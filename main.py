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
        self.window.geometry("575x475")  # Screen Size
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
        # self.logo = Logo(self)
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
        self.logoCanvas.place(x=350, y=250)
class Pressure:
    def __init__(self, obj):
        self.pressureCanvas = Canvas(obj.window, height=150, width=150,background="white", highlightthickness=1)
        self.pressureCanvas.place(x=200, rely=0,anchor=NW)
        self.photo = PhotoImage(file="Images/press.png")
        self.pressureCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.txtCanvas = Canvas(obj.window, height=25, width=150, background="white", highlightthickness=1)
        self.p_txt = self.txtCanvas.create_text(60, 15, fill="black", text="Pressure: ", font=('Helvetica 14 bold'))
        self.value_txt = self.txtCanvas.create_text(120, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.txtCanvas.place(x=200, y=150,anchor=NW)
class Power:
    def __init__(self, obj):
        self.powerCanvas = Canvas(obj.window, height=150, width=140, background="white", highlightthickness=1)
        self.powerCanvas.place(x=271, rely=1,anchor=SW)
        self.photo = PhotoImage(file="Images/bolt.png")
        self.powerCanvas.create_image(25, 0, image=self.photo, anchor=NW)
        self.p_txt = self.powerCanvas.create_text(10, 90, fill="black", text="      Power\nConsumption", font=('Helvetica 13 bold'),anchor=NW)
        
        self.pCanvas = Canvas(obj.window, height=25, width=140, background="white", highlightthickness=1)
        self.pCanvas.place(x=271, rely=1, anchor=SW)
        self.value_txt = self.pCanvas.create_text(70,16, fill="black", text="0", font=('Helvetica 14 roman'), anchor=CENTER)
class Temperature:
    def __init__(self, obj):
        self.temperatureCanvas = Canvas(obj.window, height=120, width=120, background="white", highlightthickness=1)
        self.temperatureCanvas.place(x=150, y=425, anchor=SW)
        self.photo = PhotoImage(file="Images/thermo.png")
        self.temperatureCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.p1Canvas = Canvas(obj.window, height=25, width=120, background="white", highlightthickness=1)
        self.p1 = self.p1Canvas.create_text(40, 15, fill="black", text="P1: ", font=('Helvetica 14 bold'))
        self.p1_val = self.p1Canvas.create_text(80, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.p1Canvas.place(x=150, y=450, anchor=SW)
        
        self.p2Canvas = Canvas(obj.window, height=25, width=120, background="white", highlightthickness=1)
        self.p2 = self.p2Canvas.create_text(40, 15, fill="black", text="P2: ", font=('Helvetica 14 bold'))
        self.p2_val = self.p2Canvas.create_text(80, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.p2Canvas.place(x=150, rely=1, anchor=SW)
class Speed:
    def __init__(self, obj):
        self.speedCanvas = Canvas(obj.window, height=140, width=160, background="white", highlightthickness=1)
        self.speedCanvas.place(relx=0, rely=0, anchor=NW)
        self.photo = PhotoImage(file="Images/3d_acc.png")
        self.speedCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.xCanvas = Canvas(obj.window, height=25, width=160, background="white", highlightthickness=1)
        self.xCanvas.place(x=0, y=140)
        self._X_ = self.xCanvas.create_text(60, 15, fill="black", text="X-Speed: ", font=('Helvetica 14 bold'))
        self._X_Speed = self.xCanvas.create_text(120, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NW)
        
        self.yCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.yCanvas.place(x=0, y=165)
        self._Y_ = self.yCanvas.create_text(60, 15, fill="black", text="Y-Speed: ", font=('Helvetica 14 bold'))
        self._Y_Speed = self.yCanvas.create_text(120, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NW)
        
        self.zCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.zCanvas.place(x=0, y=190)
        self._Z_ = self.zCanvas.create_text(60, 15, fill="black", text="Z-Speed: ", font=('Helvetica 14 bold'))
        self._Z_Speed = self.zCanvas.create_text(120, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NW)
class Acceleration:
    def __init__(self, obj):
        self.accelerationCanvas = Canvas(obj.window, height=140, width=160, background="white", highlightthickness=1)
        self.accelerationCanvas.place(relx=0, y=400,anchor=SW)
        self.photo = PhotoImage(file="Images/3d_acc.png")
        self.accelerationCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        ###
        self.xCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.xCanvas.place(relx=0, y=425, anchor=SW)
        self._X_ = self.xCanvas.create_text(60, 15, fill="black", text="X-Acc: ", font=('Helvetica 14 bold'))
        self._X_Acc = self.xCanvas.create_text(120, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        self.yCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.yCanvas.place(x=0, y=450, anchor=SW)
        self._Y_ = self.yCanvas.create_text(60, 15, fill="black", text="Y-Acc: ", font=('Helvetica 14 bold'))
        self._Y_Acc = self.yCanvas.create_text(120, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        self.zCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.zCanvas.place(relx=0, rely=1, anchor=SW)
        self._Z_ = self.zCanvas.create_text(60, 15, fill="black", text="Z-Acc: ", font=('Helvetica 14 bold'))
        self._Z_Acc = self.zCanvas.create_text(120, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
class Location:
    def __init__(self, obj):
        self.locationCanvas = Canvas(obj.window, height=150, width=160,background="white", highlightthickness=1)
        self.locationCanvas.place(relx=1, rely=0,anchor=NE)
        self.photo = PhotoImage(file="Images/3d_loc.png")
        self.locationCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.xCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.xCanvas.place(relx=1, y=150,anchor=NE)
        self._X_ = self.xCanvas.create_text(60, 15, fill="black", text="X-Loc: ", font=('Helvetica 14 bold'))
        self._X_Loc = self.xCanvas.create_text(120, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NE)
        
        self.yCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.yCanvas.place(relx=1, y=175,anchor=NE)
        self._Y_ = self.yCanvas.create_text(60, 15, fill="black", text="Y-Loc: ", font=('Helvetica 14 bold'))
        self._Y_Loc = self.yCanvas.create_text(120, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NE)
        
        self.zCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.zCanvas.place(relx=1, y=200,anchor=NE)
        self._Z_ = self.zCanvas.create_text(60, 15, fill="black", text="Z-Loc: ", font=('Helvetica 14 bold'))
        self._Z_Loc = self.zCanvas.create_text(120, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NE)
class Maneuver:
    def __init__(self, obj):
        self.maneuverCanvas = Canvas(obj.window, height=160, width=160,background="white", highlightthickness=1)
        self.maneuverCanvas.place(relx=1, y=400,anchor=SE)
        self.photo = PhotoImage(file="Images/force.png")
        self.maneuverCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.pitchArr = self.maneuverCanvas.create_line(41,105,130,130, arrow=LAST, width=3, fill="green")
        self.rollArr = self.maneuverCanvas.create_line(41,105,130,70, arrow=LAST, width=3, fill="red")
        self.yawArr = self.maneuverCanvas.create_line(41, 105, 41,20, arrow=LAST, width=3, fill="blue")
        #roll, pitch ve yaw
        self.yawCanvas = Canvas(obj.window, height=25, width=160, background="white", highlightthickness=1)
        self.yawCanvas.place(relx=1, y=425, anchor=SE)
        self._Yaw_ = self.yawCanvas.create_text(60, 15, fill="black", text="Yaw: ", font=('Helvetica 14 bold'))
        self._Yaw_Deg = self.yawCanvas.create_text(120, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=E)
                
        self.rollCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.rollCanvas.place(relx=1, y=450, anchor=SE)
        self._Roll_ = self.rollCanvas.create_text(60, 15, fill="black", text="Roll: ", font=('Helvetica 14 bold'))
        self._Roll_Deg = self.rollCanvas.create_text(120, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=E)
        
        self.pitchCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.pitchCanvas.place(relx=1, rely=1, anchor=SE)
        self._Pitch_ = self.pitchCanvas.create_text(60, 15, fill="black", text="Pitch: ", font=('Helvetica 14 bold'))
        self._Pitch_Deg = self.pitchCanvas.create_text(120, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=E)
        
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
    
if __name__ == '__main__':
    app = App()
    # app.window.bind("<Up>", lambda event, obj=app: changeSpeed(obj))
    # app.window.bind("<Left>", lambda event, obj=app: changeBattery(obj))
    # app.window.bind("<BackSpace>", lambda event, obj=app: changeSig(obj))
    # app.window.bind("<Down>", lambda event, obj=app: changeLoc(obj))
    # app.window.bind("<Right>", lambda event, obj=app: changeSteer(obj))
    # app.window.protocol('WM_DELETE_WINDOW', lambda obj= app: exit_func(obj))
    app.window.mainloop()
