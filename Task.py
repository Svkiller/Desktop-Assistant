import datetime
from logging.config import listen
import cv2
import numpy
import pywikihow
import requests
import os
import wikipedia
import wikipedia as googleScrap
import pywhatkit
import webbrowser
import psutil
import pyautogui
import time
import random
import pyjokes
import geocoder
import configure
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import pprint
import wolframalpha
import PyPDF2
from pywinauto import Application
from gtts import gTTS
from googletrans import Translator
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from bs4 import BeautifulSoup, Tag
from Speak import Say
from requests import get
from PIL import Image
from Listen import Listen
contacts = {
            "shubham":"shubhamvishwakarma579@gmail.com" ,
            "asifar":"ska46667@gmail.com",
            "shraddha":"shradhabadhe2393@gmail.com",
            "Namrta":"namrtalanjewar8@gmail.com",
            "suyog Ambi":"suyogambi2019@gmail.com"


        }

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def joke(tag):
    joke = pyjokes.get_jokes()
    Say(joke)


def get_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=2eb6115c6a5c4ed9b51ac08811800d78'
    # news api from https://newsapi.org/account
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=2eb6115c6a5c4ed9b51ac08811800d78'

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=2eb6115c6a5c4ed9b51ac08811800d78"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []

    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        Say(f"'today's {day[i]} news is:",{head[i]})

def loc(place):
    webbrowser.open("http://www.google.com/maps/place/" + place + "")
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    location = location.raw['address']
    target_loc = {'city': location.get('city', ''),
                   'state': location.get('state', ''),
                   'country': location.get('country', '')}

    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng

    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance), 2)

    return current_loc, target_loc, distance

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']

    return city, state,country

app_id =  "U45QX5-65J68GX3E9" #   wolframalpha API id used
def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        Say("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


def CloseApps(tag,query):
    Say("Ok sir , Wait a second")
    
    if "close youtube" in tag:
        os.system("TASKKILL /F /im msedge.exe")
    elif "close maps" in tag:
        os.system("TASKKILL /F /im msedge.exe")
    elif "close facebook" in tag:
        os.system("TASKKILL /F /im msedge.exe")
    elif "close instagram" in tag:
        os.system("TASKKILL /F /im msedge.exe")
    elif "close code" in tag:
        os.system("TASKKILL /F /im Code.exe")
    elif "close netbeans" in tag:
        os.system("TASKKILL /F /im netbeans64.exe")
    elif "close browser" in tag:
        os.system("TASKKILL /F /im msedge.exe")
    elif "close Google Chrome" in tag:
        os.system("TASKKILL /F /im chrome.exe")
    elif "close VLC player" in tag:
        os.system("TASKKILL /F /im vlc.exe")
    elif "close Picasa" in tag:
        os.system("TASKKILL /F /im Picasa3.exe")
    elif "close winamp" in tag:
        os.system("TASKKILL /F /im winamp.exe")
    elif "close notepad" in tag:
        os.system("TASKKILL /F /im notepad.exe")
    elif "close CMD" in tag:
        os.system("TASKKILL /F /im cmd.exe")

def NonInputExecution(tag):
    query = str()
    if "time" in tag:
        Time()
    elif "date" in tag:
        Date()
    elif "day" in tag:
        Day()

def InputExecution(tag,query):

    if "wikipedia" in tag:
        Say('searching wikipedia...')
        name = str(query).replace("who is","").replace("information of","").replace("wikipedia","").replace("about","")
        result = wikipedia.summary(name,5)
        Say("according to wikipedia")
        Say(result)

    elif "google" in tag:
        Say('searching google...')
        query = str(query).replace("google","")
        query = query.replace("search","")
        Say("acooording to google")
        pywhatkit.search(query)
    
    elif "open google" in tag:
        Say("sir , what should i search on google")
        cm = Listen()
        webbrowser.open(f"{cm}")
    
    elif "full form" in tag:
        query = query.replace("full form","")
        query = query.replace("full form of","")
        Say("This found on web")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,3)
            Say(result)
        except:
            Say("no data found")

    elif "open youtube" in tag:
        Say('opening youtube')
        query = str(query).replace("open youtube","")
        query = query.replace("youtube","")
        web = 'https://www.youtube.com/'
        webbrowser.open(web)
        Say("now you use youtube")
    
    elif "youtube search" in tag:
        query = str(query).replace("youtube","")
        query = query.replace("youtube search","")
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
    
    elif "play songs on youtube" in tag:
        Say("sir , which shuold i play on you tube")
        cm = Listen()
        pywhatkit.playonyt(f"{cm}")
    
    elif "open maps" in tag:
        Say("Opening maps")
        webbrowser.open('https://www.google.com/maps/place/Sinhgad+Institute+Of+Business+Administration+And+Research+(Sibar)/@18.4383961,73.895379,14.98z/data=!4m8!1m2!2m1!1sgoogle+maps!3m4!1s0x3bc2ea5467400001:0xe4d2d00190e0663!8m2!3d18.4412428!4d73.8955409')
    
    elif "website" in tag:
        query = str(query).replace("william","")
        query = query.replace("website","")
        web1 = 'https://www.google.com/results?search_query=' + query
        webbrowser.open(web1)
    
    elif "launch" in tag:
        name = str(query).replace("take command","")
        web2 = 'https://www.' + name + '.com'
        webbrowser.open(web2)
    
    elif "open facebook" in tag:
        Say("Opening facebook")
        query = str(query).replace("william","")
        query = query.replace("facebook","")
        web = 'https://www.facebook.com/results?search_query=' + query
        webbrowser.open(web)
    
    elif "open instagram" in tag:
        Say("Opening instagram")
        webbrowser.open('https://www.instagram.com/')
    
    elif "open vs code" in tag:
        Say('Opening Visual studio code')
        codePath ="C:\\Users\\ACER1\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
        os.startfile(codePath)
    
    elif "open netbeans" in tag:
        Say('Opening NetBeans')
        netPath ="C:\\Program Files\\NetBeans-12.6\\netbeans\\bin\\netbeans64.exe"
        os.startfile(netPath)
    
    elif "open file manager" in tag:
        Say('Opening ACER1 file')
        acerPath = "C:\\Users\\ACER1"
        os.startfile(acerPath)
    
    elif "open browser" in tag:
        Say('Opening Edge browser')
        edgePath ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\msedge.exe"
        os.startfile(edgePath)
    
    elif "open Google Chrome" in tag:
        Say('Opening Google Chrome browser')
        chromePath ="C:\\Program Files (x86)\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chromePath)
    
    elif "open VLC player" in tag:
        Say('Opening VLC player')
        vlcPath ="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
        os.startfile(vlcPath)
    
    elif "open Picasa" in tag:
        Say('Opening Picasa in system')
        picasaPath ="C:\\Program Files (x86)\\Google\\Picasa3\\Picasa3.exe"
        os.startfile(picasaPath)
    
    elif "open winamp" in tag:
        Say("Opening the application")
        winPath = "C:\\Program Files (x86)\\Winamp\\winamp.exe"
        os.startfile(winPath)
    
    elif "open whatsapp" in tag:
        Say("Opening the application")
        whatsPath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2210.10.0_x64_cv1g1gvanyjgm\\app\\WhatsApp.exe"
        os.startfile(whatsPath)

    elif "open stackoverflow" in tag:
        Say("Here you go to Stack Over flow.Happy coding")
        query = str(query).replace("open stackoverflow","")
        query = query.replace("stackoverflow","")
        web = 'https://www.stackoverflow.com/' + query
        webbrowser.open(web)
    
    elif "open camera" in tag:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam',img)
            k = cv2.waitKey(50)
            if k==27:
                break
        cap.release()
        cv2.destroyAllWindows()
    
    elif "open CMD" in tag:
        os.system("start cmd")
        
    elif "open notepad" in tag:
        os.system("start notepad")
    
    elif "activate how to do mod" in tag:
        Say("How to do mod is Activated please tell me what you want to know")
        from pywikihow import search_wikihow
        how = Listen()
        max_results = 1
        how_to = search_wikihow(how, max_results)
        assert len(how_to) == 1
        Say(how_to[0].summary)
    
    elif "battery" in tag:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        Say(f"sir our system have {percentage} percent battery left")
    
    elif "volume up" in tag:
        pyautogui.press("volumeup")
    elif "volume down" in tag:
        pyautogui.press("volumedown")
    elif "volume mute" in tag:
        pyautogui.press("volumemute")
    
    elif "ip address" in tag:
        ip = get('https://api.ipify.org').text
        Say(f"Your device IP address is {ip}")
    
    elif "take screenshot" in tag:
        Say("please tell me the name for this screenshot file")
        name = Listen()
        Say("please sir hold the screen for few seconds, i am taking scrennshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        Say("I am done sir the screenshot is saved in our folder. ")
    
    elif "read" in tag:
        Say("Please tell me the name of the file")
        name = Listen()
        Say("please sir hold ,i am fetching data")
        file = open(r'E:/DeskTop/' +f"{name}.pdf",'rb')
        pdfreader = PyPDF2.PdfFileReader(file)
        pages = pdfreader.getNumPages()
        Say("Number of the pages in this book are {pages}")
        Say("From which page i have to start reading ?")
        numPage = int(input("enter the number of pages"))
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        Say(text)
    
    elif "show screenshot" in tag:
        try:
            Say("screenshot name please ?")
            name = Listen()
            img = Image.open('E://DeskTop//' + f"{name}.png")
            img.show(img)
            Say("Here it is sir")
            time.sleep(2)

        except IOError:
            Say("Sorry sir, I am unable to display the screenshot")
    
    elif "switch the window" in tag:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

    elif "play music" in tag:
        mus_dir = r"C:\\Users\ACER1\\Music"
        songs = os.listdir(mus_dir)
        rd = random.choice(songs)
        for song in songs:
            if song.endswith('.mp3'):
                os.startfile(os.path.join(mus_dir, rd))
            else:
                Say("i cannot find a song")
                Say("sir , which song i play on you tube")
                cm = Listen()
                pywhatkit.playonyt(f"{cm}")

    elif "news" in tag:
        news_res = get_news()
        Say('Source: The Times Of India')
        Say('Todays Headlines are..')
        for index, articles in enumerate(news_res):
            pprint.pprint(articles['title'])
            Say(articles['title'])
            if index == len(news_res)-2:
                break
        Say('These were the top headlines, Have a nice day Sir!!..')
    
    elif "where is" in tag:
        place = query.split('where is ', 1)[1]
        current_loc, target_loc, distance = loc(place)
        city = target_loc.get('city', '')
        state = target_loc.get('state', '')
        country = target_loc.get('country', '')
        time.sleep(1)
        try:

            if city:
                res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                print(res)
                Say(res)

            else:
                res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                print(res)
                Say(res)

        except:
            res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
            Say(res)
        
    elif "current location" in tag:
        try:
            city, state, country = my_location()
            print(city, state, country)
            Say(
                f"You are currently in {city} city which is in {state} state and country {country}")
        except Exception as e:
            Say(
                "Sorry sir, I coundn't fetch your current location. Please try again")
    
    elif "send email" in tag:
        try:
            Say("Whom do you want to email sir ?")
            name = Listen()
            if name in contacts:
                send_to = contacts[name]
            else:
                Say("I coudn't find the requested person's email in my contact. Please try again with a different name")


            msg = MIMEMultipart()
            msg['From'] = 'Shubham Vishwakarma'
            msg['To'] = send_to
            Say("What is the subject sir ?")
            msg['Subject'] = Listen()
            Say("What is the message?,")
            message = Listen()
            msg.attach(MIMEText(message))

            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('vishwakarmashubham9436@gmail.com', 'ynignpdrdbepmjya')
            smtpserver.sendmail('vishwakarmashubham9436@gmail.com',send_to,msg.as_string())
            Say("Email has been successfully sent")

            smtpserver.quit()
        except:
            Say("Sorry sir. Couldn't send your mail. Please try again")
    
   
    elif "calculate" in tag:
        Say("what is the problem")
        question = Listen()
        answer = computational_intelligence(question)
        Say(answer)
    
    elif "save url" in tag:
        try:
            app = Application(backend='uia')
            app.connect(title_re=".*Chrome.*")
            dlg = app.top_window()
            url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
            print("Url", url)
            Say("please tell me the name for this url")
            name = Listen()
            time.sleep(3)
            with open("url.txt", "a") as f:
                f.write(f"{name} : {url}\n")
            Say("i am done sir")
        
        except:
            Say("i am not able to save")
    
    elif "shutdown" in tag:
        Say("Do you really want to shutdown")
        reply = Listen()
        if 'yes' in reply:
            os.system('shutdown /s /t 1')

    elif "restart" in tag:
        Say("Do you really want to restart")
        reply = Listen()
        if 'yes' in reply:
            os.system('shutdown /r /t 1')
    
    elif "sleep" in query:
            Say("Do you really want to sleep the system")
            reply = Listen()
            if 'yes' in reply:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "stop" in tag:
        Say("please enter any number to continue")
        k = int(input("enter a number:"))
        
    