from tkinter import *
import socket
import time
import threading as thr
_END_FLAG_ = 0

_HOST_ = '192.168.1.56'  # The server's hostname or IP address
_PORT_ = 5005  # The port used by the server

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("575x475")  # Screen Size
        self.window.resizable(0, 0) 
        self.window.title("ALFA ETA-H")  # Pencere ismi
        self.window.iconname("ALFA ETA-H")
        self.window.config(background="white")
        photo = PhotoImage(file="Images/logo.png")  # app icon
        self.window.iconphoto("false", photo)
        self.logo = Logo(self)
        self.pressure = Pressure(self)
        self.temperature = Temperature(self)
        self.speed = Speed(self)
        self.acc = Acceleration(self)
        self.location = Location(self)
        self.maneuver = Maneuver(self)
        self.power = Power(self)
        self.stop_button = Stop_Button(self)
        self.socket = self.create_socket()
        
        self.conn, self.addr = -1, -1
        self.readData = thr.Thread(target=self.readAndParseDATA)
        self.readData.start()
        self.data = ""

    def create_socket(self):
        server_socket = socket.socket()  # get instance
        server_socket.bind((_HOST_, _PORT_)) # bind host address and port together
        server_socket.listen(2)
        return server_socket

    def readAndParseDATA(self):
        self.socket.settimeout(5)
        while(getFlag() == 0):
            try:
                print("Socket Timeout is 5 sec.")
                print("Waiting for client...")
                self.conn, self.addr = self.socket.accept()  # accept new connection
                print("Connection from: " + str(self.addr))
            except socket.timeout:
                print("\n5 sec. over - No Client")
                print("Checking again...\n")
                time.sleep(1)
                pass
            else:    
                while(getFlag() == 0):
                    try:
                        self.conn.sendall(b"ping")# Eğer gönderemezse(Raspberry bağlantisi kesilirse) exception verir
                        time1 = time.time()
                        # eğer gönderebiliyorsa bağlantıda sorun yok demektir.
                        data = self.conn.recv(1024).decode()
                        time2 = time.time()
                        print(time2-time1)
                        print("Received Data: " + str(data))
                        self.data = data.split(",")
                        changeAll(app)
                        pass  # While a devam eder
                    except:
                        print("CONNECTION LOST")
                        break # while dan cikar tekrar bağlanti bekler
                    
                self.conn.close()  # close the connection

class Stop_Button:
    def __init__(self, obj):
        self.canvas = Canvas(obj.window, height=75, width=75, background="red", highlightthickness=2)
        self.photo = PhotoImage(file="Images/button.png")
        self.canvas.create_image(2,2, image=self.photo, anchor=NW)
        self.canvas.place(x=160, y=200)
class Logo:
    def __init__(self, obj):
        self.logoCanvas = Canvas(obj.window, height=145, width=145, background="blue", highlightthickness=0)
        self.photo = PhotoImage(file="Images/logo.png")
        self.logoCanvas.create_image(75,74, image=self.photo, anchor=CENTER)
        self.logoCanvas.place(x=250, y=175)
class Pressure:
    def __init__(self, obj):
        self.pressureCanvas = Canvas(obj.window, height=150, width=150,background="white", highlightthickness=1)
        self.pressureCanvas.place(x=200, rely=0,anchor=NW)
        self.photo = PhotoImage(file="Images/press.png")
        self.pressureCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.txtCanvas = Canvas(obj.window, height=25, width=150, background="white", highlightthickness=1)
        self.p_txt = self.txtCanvas.create_text(5, 15, fill="black", text="Pressure:     Bar", font=('Helvetica 14 bold'),anchor=W)
        self.value_txt = self.txtCanvas.create_text(90, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
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
        self.value_txt = self.pCanvas.create_text(70,16, fill="black", text="0 W", font=('Helvetica 14 roman'), anchor=CENTER)
class Temperature:
    def __init__(self, obj):
        self.temperatureCanvas = Canvas(obj.window, height=120, width=120, background="white", highlightthickness=1)
        self.temperatureCanvas.place(x=150, y=425, anchor=SW)
        self.photo = PhotoImage(file="Images/thermo.png")
        self.temperatureCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.p1Canvas = Canvas(obj.window, height=25, width=120, background="white", highlightthickness=1)
        self.p1 = self.p1Canvas.create_text(15, 15, fill="black", text="P1:          \N{DEGREE SIGN}C", font=('Helvetica 14 bold'), anchor=W)
        self.p1_val = self.p1Canvas.create_text(50, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.p1Canvas.place(x=150, y=450, anchor=SW)
        
        self.p2Canvas = Canvas(obj.window, height=25, width=120, background="white", highlightthickness=1)
        self.p2 = self.p2Canvas.create_text(15, 15, fill="black", text="P2:          \N{DEGREE SIGN}C", font=('Helvetica 14 bold'), anchor=W)
        self.p2_val = self.p2Canvas.create_text(50, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        self.p2Canvas.place(x=150, rely=1, anchor=SW)
class Speed:
    def __init__(self, obj):
        self.speedCanvas = Canvas(obj.window, height=140, width=160, background="white", highlightthickness=1)
        self.speedCanvas.place(relx=0, rely=0, anchor=NW)
        self.photo = PhotoImage(file="Images/3d_acc.png")
        self.speedCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.xCanvas = Canvas(obj.window, height=25, width=160, background="white", highlightthickness=1)
        self.xCanvas.place(x=0, y=140)
        self._X_ = self.xCanvas.create_text(5,5, fill="black", text="X-Speed:         m/s", font=('Helvetica 14 bold'),anchor=NW)
        self._X_Speed = self.xCanvas.create_text(90, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NW)
        
        self.yCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.yCanvas.place(x=0, y=165)
        self._Y_ = self.yCanvas.create_text(5,5, fill="black", text="Y-Speed:         m/s", font=('Helvetica 14 bold'),anchor=NW)
        self._Y_Speed = self.yCanvas.create_text(90, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NW)
        
        self.zCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.zCanvas.place(x=0, y=190)
        self._Z_ = self.zCanvas.create_text(5,5, fill="black", text="Z-Speed:         m/s", font=('Helvetica 14 bold'),anchor=NW)
        self._Z_Speed = self.zCanvas.create_text(90, 5, fill="black", text="0", font=('Helvetica 14 roman'), anchor=NW)
class Acceleration:
    def __init__(self, obj):
        self.accelerationCanvas = Canvas(obj.window, height=140, width=160, background="white", highlightthickness=1)
        self.accelerationCanvas.place(relx=0, y=400,anchor=SW)
        self.photo = PhotoImage(file="Images/3d_acc.png")
        self.accelerationCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        ###
        self.xCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.xCanvas.place(relx=0, y=425, anchor=SW)
        self._X_ = self.xCanvas.create_text(5,5, fill="black", text="X-Acc:          m/s2", font=('Helvetica 14 bold'),anchor=NW)
        self._X_Acc = self.xCanvas.create_text(70, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        self.yCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.yCanvas.place(x=0, y=450, anchor=SW)
        self._Y_ = self.yCanvas.create_text(5,5, fill="black", text="Y-Acc:          m/s2", font=('Helvetica 14 bold'),anchor=NW)
        self._Y_Acc = self.yCanvas.create_text(70, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        self.zCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.zCanvas.place(relx=0, rely=1, anchor=SW)
        self._Z_ = self.zCanvas.create_text(5,5, fill="black", text="Z-Acc:          m/s2", font=('Helvetica 14 bold'),anchor=NW)
        self._Z_Acc = self.zCanvas.create_text(70, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
class Location:
    def __init__(self, obj):
        self.locationCanvas = Canvas(obj.window, height=150, width=160,background="white", highlightthickness=1)
        self.locationCanvas.place(relx=1, rely=0,anchor=NE)
        self.photo = PhotoImage(file="Images/3d_loc.png")
        self.locationCanvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.xCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.xCanvas.place(relx=1, y=150,anchor=NE)
        self._X_ = self.xCanvas.create_text(5, 15, fill="black", text="X-Loc:              m", font=('Helvetica 14 bold'),anchor=W)
        self._X_Loc = self.xCanvas.create_text(70, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        self.yCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.yCanvas.place(relx=1, y=175,anchor=NE)
        self._Y_ = self.yCanvas.create_text(5, 15, fill="black", text="Y-Loc:              cm", font=('Helvetica 14 bold'),anchor=W)
        self._Y_Loc = self.yCanvas.create_text(70, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        self.zCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.zCanvas.place(relx=1, y=200,anchor=NE)
        self._Z_ = self.zCanvas.create_text(5, 15, fill="black", text="Z-Loc:              cm", font=('Helvetica 14 bold'),anchor=W)
        self._Z_Loc = self.zCanvas.create_text(70, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
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
        self._Yaw_ = self.yawCanvas.create_text(17, 15, fill="black", text=" Yaw:             \N{DEGREE SIGN}", font=('Helvetica 14 bold'),anchor=W)
        self._Yaw_Deg = self.yawCanvas.create_text(80, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
                
        self.rollCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.rollCanvas.place(relx=1, y=450, anchor=SE)
        self._Roll_ = self.rollCanvas.create_text(15, 15, fill="black", text="  Roll:             \N{DEGREE SIGN}", font=('Helvetica 14 bold'),anchor=W)
        self._Roll_Deg = self.rollCanvas.create_text(80, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
        
        self.pitchCanvas = Canvas(obj.window, height=25, width=160,background="white", highlightthickness=1)
        self.pitchCanvas.place(relx=1, rely=1, anchor=SE)
        self._Pitch_ = self.pitchCanvas.create_text(15, 15, fill="black", text="Pitch:             \N{DEGREE SIGN}", font=('Helvetica 14 bold'),anchor=W)
        self._Pitch_Deg = self.pitchCanvas.create_text(80, 15, fill="black", text="0", font=('Helvetica 14 roman'), anchor=W)
  
def updatePressure(obj, value):
    obj.txtCanvas.delete(obj.value_txt)
    obj.value_txt = obj.txtCanvas.create_text(90, 15, fill="black", text=value[8], font=('Helvetica 14 roman'), anchor=W)
def changePressure(obj):
    updatePressure(obj.pressure, obj.data)
    obj.window.update()

def updatePower(obj, value):
    obj.pCanvas.delete(obj.value_txt)
    obj.value_txt = obj.pCanvas.create_text(70, 16, fill="black", text=value+" W", font=('Helvetica 14 roman'), anchor=CENTER)
def changePower(obj):
    updatePower(obj.power, obj.data[12])
    obj.window.update()

def updateLocation(obj, value):
    obj.xCanvas.delete(obj._X_Loc)
    obj._X_Loc = obj.xCanvas.create_text(70, 15, fill="black", text=value[9], font=('Helvetica 14 roman'), anchor=W)

    obj.yCanvas.delete(obj._Y_Loc)
    obj._Y_Loc = obj.yCanvas.create_text(70, 15, fill="black", text=value[10], font=('Helvetica 14 roman'), anchor=W)

    obj.zCanvas.delete(obj._Z_Loc)
    obj._Z_Loc = obj.zCanvas.create_text(70, 15, fill="black", text=value[11], font=('Helvetica 14 roman'), anchor=W)
def changeLocation(obj):
    updateLocation(obj.location, [*obj.data])
    obj.window.update()

def updateAcceleration(obj, value):
    obj.xCanvas.delete(obj._X_Acc)
    obj._X_Acc = obj.xCanvas.create_text(70, 15, fill="black", text=value[3], font=('Helvetica 14 roman'), anchor=W)

    obj.yCanvas.delete(obj._Y_Acc)
    obj._Y_Acc = obj.yCanvas.create_text(70, 15, fill="black", text=value[4], font=('Helvetica 14 roman'), anchor=W)

    obj.zCanvas.delete(obj._Z_Acc)
    obj._Z_Acc = obj.zCanvas.create_text(70, 15, fill="black", text=value[5], font=('Helvetica 14 roman'), anchor=W)
def changeAcceleration(obj):
    updateAcceleration(obj.acc, [*obj.data])
    obj.window.update()

def updateSpeed(obj, value):
    obj.xCanvas.delete(obj._X_Speed)
    obj._X_Speed = obj.xCanvas.create_text(90, 5, fill="black", text=value[0], font=('Helvetica 14 roman'), anchor=NW)

    obj.yCanvas.delete(obj._Y_Speed)
    obj._Y_Speed = obj.yCanvas.create_text(90, 5, fill="black", text=value[1], font=('Helvetica 14 roman'), anchor=NW)

    obj.zCanvas.delete(obj._Z_Speed)
    obj._Z_Speed = obj.zCanvas.create_text(90, 5, fill="black", text=value[2], font=('Helvetica 14 roman'), anchor=NW)
def changeSpeed(obj):
    updateSpeed(obj.speed, [*obj.data])
    obj.window.update()

def updateTemperature(obj, value):
    obj.p1Canvas.delete(obj.p1_val)
    obj.p1_val = obj.p1Canvas.create_text(50, 15, fill="black", text=value[6], font=('Helvetica 14 roman'), anchor=W)

    obj.p2Canvas.delete(obj.p2_val)
    obj.p2_val = obj.p2Canvas.create_text(50, 15, fill="black", text=value[7], font=('Helvetica 14 roman'), anchor=W)
def changeTemperature(obj):
    updateTemperature(obj.temperature, [*obj.data])
    obj.window.update()

def updateManeuver(obj, value):
    obj.yawCanvas.delete(obj._Yaw_Deg)
    obj._Yaw_Deg = obj.yawCanvas.create_text(80, 15, fill="black", text=value[13], font=('Helvetica 14 roman'), anchor=W)

    obj.rollCanvas.delete(obj._Roll_Deg)
    obj._Roll_Deg = obj.rollCanvas.create_text(80, 15, fill="black", text=value[14], font=('Helvetica 14 roman'), anchor=W)

    obj.pitchCanvas.delete(obj._Pitch_Deg)
    obj._Pitch_Deg = obj.pitchCanvas.create_text(80, 15, fill="black", text=value[15], font=('Helvetica 14 roman'), anchor=W)
def changeManeuver(obj):
    updateManeuver(obj.maneuver, [*obj.data])
    obj.window.update()
    
def changeAll(obj):
    changePower(obj)
    changePressure(obj)
    changeLocation(obj)
    changeAcceleration(obj)
    changeSpeed(obj)
    changeTemperature(obj)
    changeManeuver(obj)
     
def exit_func(obj):
    setFlag(1)
    obj.readData.join()
    print("Closing...")
    obj.window.destroy()
def getFlag():
    global _END_FLAG_
    return _END_FLAG_    
def setFlag(i):
    global _END_FLAG_
    _END_FLAG_=1
    
def stop_signal(obj):
    if obj.conn !=-1:
        print("STOP")
        obj.conn.send("stop".encode())
    else:
        print("No Client")

if __name__ == '__main__':
    
    app = App()
    #app.window.bind("<Up>", lambda event, obj=app: changeAll(obj))
    app.stop_button.canvas.bind("<Button-1>", lambda event, obj=app:stop_signal(obj))
    app.window.protocol('WM_DELETE_WINDOW', lambda obj= app: exit_func(obj))
    app.window.mainloop()
