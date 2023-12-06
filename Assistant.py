import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import torch
import os
import datetime
import shutil
import time
import sys
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate 
from PyQt5.uic import loadUiType
from FinalUi1 import Ui_MainWindow
from PyQt5.QtWidgets import QPushButton

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#----------------------------------
Name = "Desktop-Assistance"

from Listen import Listen
from Speak import Say
from Task import CloseApps, InputExecution, get_news, joke, loc, my_location, news
from Task import NonInputExecution

def Pass(pass_inp):
    password = "python"
    passss = str(password)
    if passss == str(pass_inp):
        Say("Access Granted .")
        import Assistant

    else:
        Say("Access denied .")


if __name__=="__main__":
    Say("This Particular File Is Password Protected .")
    Say("Kindly provide The Password to Access .")
    passsss = Listen()
    Pass(passsss)
    Say("Please Provide The Correct Password to Access .")
    Say("This Is The Last Chance , Please Provide The Correct Password to Access .")
    passsss = input(": Enter The Password :")
    Pass(passsss)

def startup():
    Say("Initializing Assitant")
    Say("Starting all systems applications")
    Say("Installing and checking all drivers")
    Say("Caliberating and examining all the core processors")
    Say("Checking the internet connection")
    Say("Wait a moment sir")
    Say("All drivers are up and running")
    Say("All systems have been activated")
    Say("Now I am online")

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=00 and hour<=12:
        Say("Good Morning! sir")

    elif hour>=12 and hour<=17:
        ("Good Afternoon! sir")  

    else:
        Say("Good Evening! sir")
    Say("I am Desktop Assitant . may i help you")

def ussername():
    Say("What should i call you sir")
    uname = Listen()
    Say("Welcome Mister")
    Say(uname)
    columns = shutil.get_terminal_size().columns
        
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
        
    Say("How can i Help you, Sir")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        
        self.Task()

    def Task(self):

        # startup()
        # wish()
        # ussername()

        while(True):
    
            sentence = Listen()
            result = str(sentence)

            if sentence =="bye":
                exit()
            elif sentence =="exit":
                exit()
            
            sentence = tokenize(sentence)
            X = bag_of_words(sentence,all_words)
            X = X.reshape(1,X.shape[0])
            X = torch.from_numpy(X).to(device)

            output = model(X)

            _ , predicted =torch.max(output,dim=1)

            tag = tags[predicted.item()]
            
            probs = torch.softmax(output,dim=1)
            prob = probs[0][predicted.item()]

            if prob.item() > 0.75:
                for intent in intents['intents']:
                    if tag == intent["tag"]:
                        reply = random.choice(intent["responses"])
                        if "time" in reply:
                            NonInputExecution(reply)
                        elif "date" in reply:
                            NonInputExecution(reply)
                        elif "day" in reply:
                            NonInputExecution(reply)

                        elif "joke" in reply:
                            joke(reply)


                        elif "news" in reply:
                            InputExecution(reply,result)
                        elif "where is" in reply:
                            InputExecution(reply,result)
                        elif "current location" in tag:
                            InputExecution(reply,result)
                        elif "wikipedia" in reply:
                            InputExecution(reply,result)
                        elif "google" in reply:
                            InputExecution(reply,result)
                        elif "open google" in tag:
                            InputExecution(reply,result)
                        elif "full form" in tag:
                            InputExecution(reply,result)
                        elif "open youtube" in reply:
                            InputExecution(reply,result)
                        elif "youtube search" in reply:
                            InputExecution(reply,result)
                        elif "play songs on youtube" in reply:
                            InputExecution(reply,result)
                        elif "open maps" in reply:
                            InputExecution(reply,result)
                        elif "website" in reply:
                            InputExecution(reply,result)
                        elif "launch" in reply:
                            InputExecution(reply,result)
                        elif "open facebook" in reply:
                            InputExecution(reply,result)
                        elif "open instagram" in reply:
                            InputExecution(reply,result)
                        elif "open vs code" in reply:
                            InputExecution(reply,result)
                        elif "open netbeans" in reply:
                            InputExecution(reply,result)
                        elif "open file manager" in reply:
                            InputExecution(reply,result)
                        elif "open browser" in reply:
                            InputExecution(reply,result)
                        elif "open Google Chrome" in reply:
                            InputExecution(reply,result)
                        elif "open VLC player" in reply:
                            InputExecution(reply,result)
                        elif "open picasa" in reply:
                            InputExecution(reply,result)
                        elif "open winamp" in reply:
                            InputExecution(reply,result)
                        elif "open stack overflow" in reply:
                            InputExecution(reply,result)
                        elif "open camera" in reply:
                            InputExecution(reply,result)
                        elif "open CMD" in reply:
                            InputExecution(reply,result)
                        elif "open notepad" in reply:
                            InputExecution(reply,result)
                        elif "activate how to do mod" in reply:
                            InputExecution(reply,result)
                        elif "battery" in reply:
                            InputExecution(reply,result)
                        elif "volume up" in reply:
                            InputExecution(reply,result)
                        elif "volume down" in reply:
                            InputExecution(reply,result)
                        elif "volume mute" in reply:
                            InputExecution(reply,result)
                        elif "ip address" in reply:
                            InputExecution(reply,result)
                        elif "take screenshot" in reply:
                            InputExecution(reply,result)
                        elif "show screenshot" in tag:
                            InputExecution(reply,result)
                        elif "read" in tag:
                            InputExecution(reply,result)
                        elif "switch the window" in reply:
                            InputExecution(reply,result)
                        elif "play music" in reply:
                            InputExecution(reply,result)
                        elif "send email" in reply:
                            InputExecution(reply,result)
                        elif "calculate" in tag:
                            InputExecution(reply,result)
                        elif "save url" in tag:
                            InputExecution(reply,result)

                        elif "shutdown" in reply:
                            InputExecution(reply,result)
                        elif "restart" in reply:
                            InputExecution(reply,result)
                        elif "sleep" in reply:
                            InputExecution(reply,result)
                        elif "stop" in reply:
                            InputExecution(reply,result)
                        
                        elif "close youtube" in tag:
                            CloseApps(reply,result)
                        elif "close maps" in tag:
                            CloseApps(reply,result)
                        elif "close facebook" in tag:
                            CloseApps(reply,result)
                        elif "close instagram" in tag:
                            CloseApps(reply,result)
                        elif "close code" in tag:
                            CloseApps(reply,result)
                        elif "close netbeans" in tag:
                            CloseApps(reply,result)
                        elif "close browser" in tag:
                            CloseApps(reply,result)
                        elif "close Google Chrome" in tag:
                            CloseApps(reply,result)
                        elif "close VLC player" in tag:
                            CloseApps(reply,result)
                        elif "close Picasa" in tag:
                            CloseApps(reply,result)
                        elif "close winamp" in tag:
                            CloseApps(reply,result)
                        elif "close notepad" in tag:
                            CloseApps(reply,result)
                        elif "close CMD" in tag:
                            CloseApps(reply,result)
                        
                                
                        else:
                            Say(reply)
    
startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def run(self):
        self.Task
    

    def startTask(self):
        self.ui.movie = QtGui.QMovie(r"C:/Users/ACER1/Downloads/extra gui/Code_Template.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"C:/Users/ACER1/Downloads/JARVIS-master/JARVIS-master/Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"C:/Users/ACER1/Downloads/extra gui/B.G_Template_1.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"C:/Users/ACER1/Downloads/voicereg/Siri.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

if __name__=="__main__":
    Say("This Particular File Is Password Protected .")
    Say("Kindly provide The Password to Access .")
    passsss = Listen()
    Pass(passsss)
    Say("Please Provide The Correct Password to Access .")
    Say("This Is The Last Chance , Please Provide The Correct Password to Access .")
    passsss = input(": Enter The Password :")
    Pass(passsss)


