import speech_recognition as specRec
import pyttsx3
import pywhatkit
import os, psutil
import sys
import webbrowser
import python_weather
import asyncio
import requests, json
import datetime
import pytz 
import speedtest
import socket




def speakUp(text):
    engine.say(text)
    engine.runAndWait()

def listenToUser():
    command = input()

    # try:
    #     with specRec.Microphone() as source:
    #         speakUp('How may I help you?')
    #         print('Listening...')
    #         voice = listener.listen(source)
    #         command = listener.recognize_google(voice)
    #         command = command.lower()
    #         print(command)
    # except:
    #     pass
    return command

def getWeather(city_name):
    api_key = "646366064ca35686ff19c4ff1b000418"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
   
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        tempInCel = current_temperature - 273.15
        return tempInCel
    else:
        print("City Not Found")

def checkInternetConnection():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False  

def runVirtualAssistant():
    print('Your command: ', end='')
    command = listenToUser()
    #print(command)

    #open webpage
    if 'open' in command:
        command = command.replace('open', '')
        webpage = command.strip()
        entireLink = 'https://' + webpage + '.com'
        speak = 'Opening ' + webpage
        print('Virtual Assistant: ', speak)
        speakUp(speak)
        webbrowser.open(entireLink, new=1)
    
    #play song on YouTube
    if 'play' in command:
        song = command.replace('play', '')
        speak = 'Playing ' + song
        print('Virtual Assistant: ', speak)
        speakUp(speak) 
        pywhatkit.playonyt(song)
        
    #get weather
    if 'weather' in command or 'temperature' in command:
        command = command.replace('get', '')
        command = command.replace('weather', '')
        command = command.replace('temperature', '')
        command = command.replace('of', '')
        command = command.replace('tell', '')
        command = command.replace('me', '')
        command = command.replace('please', '')
        command = command.replace('what', '')
        command = command.replace('is', '')
        command = command.replace('the', '')
        city = command.strip()
        tempOfCity = round(getWeather(city), 2)
        speak = 'Temperature of ' + city + ' is ' + str(tempOfCity) + ' degree Celcius.'
        print('Virtual Assistant: ', speak)
        speakUp(speak)

    #search on google
    if 'about' in command:
        command = command.replace('tell', '')
        command = command.replace('me', '')
        command = command.replace('about', '')
        speak = 'Searching on Google...'
        print('Virtual Assistant: ', speak)
        speakUp(speak)
        pywhatkit.search(command)
    
    #tell todays date
    if 'date' in command:
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        monthNames = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        fullDate = str(current_time.day) + ' ' + str(monthNames[current_time.month]) + ' ' + str(current_time.year)
        speak = 'Todays date is ' + fullDate
        print('Virtual Assistant: ', speak)
        speakUp(speak)

    #tell current time
    if 'time' in command:
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        fullTime = str(current_time.hour) + ':' + str(current_time.minute)
        speak = 'Time now is ' + fullTime
        print('Virtual Assistant: ', speak)
        speakUp(speak)
    
    #tell internet speed and availability
    if 'internet' in command:

        #for speed
        if 'speed' in command:
            speakUp('Running speed test. Please wait for a while!')
            st = speedtest.Speedtest()
            downSpeed = round(st.download()/10000000, 2)
            upSpeed = round(st.upload()/10000000, 2)
            speak = 'Download speed is' + ' ' + str(downSpeed) + ' mbps' + ' and upload speed is ' + str(upSpeed) + ' mbps'
            print('Virtual Assistant: ', speak)
            speakUp(speak)

        #for internet availability
        elif 'connection' in command or 'availability' in command or 'available' in command:
            intCon = checkInternetConnection()
            if(intCon):
                speak = 'Internet connection is available.'
            else:
                speak = 'Internet connection is not available.'
            print('Virtual Assistant: ', speak)
            speakUp(speak)
    
    #get news
    if 'news' in command:
        speak = 'Searching for latest news...'
        print('Virtual Assistant: ', speak)
        speakUp(speak)
        pywhatkit.search(command)

    #spell a word
    if 'spell' in command:
        command = command.replace('spell', '')
        command = command.replace('the', '')
        command = command.replace('word', '')
        word = command.strip()
        wordArr = [char for char in word]
        ans = ""
        for i in wordArr:
            ans += i
            ans += ' '
        speak = 'Spelling of ' + word + ' is ' + ans
        print('Virtual Assistant: ', speak)
        speakUp(speak)

    #tell memory consumption
    if 'memory' in command:
        process = psutil.Process(os.getpid())
        memUs = process.memory_info().rss
        speak = 'Memory usage is' + ' ' + str(memUs) + ' ' + 'bytes.'
        print('Virtual Assistant: ', speak)
        speakUp(speak)

    #tell everything it can do
    if 'what can you do' in command:
        speak = 'I can do lots of things like \nOpen a webpage, \nPlay a song on youtube, \nTell weather or temperature of a place, \nSeach about anything on google, \nTell todays date, \nTell current time, \nCheck internet speed, \nCheck internet availability, \nSearch latest news, \nSpell a word, \nTell memory usage.'
        print('Virtual Assistant: ', speak)
        speakUp(speak)

               

#main
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
listener = specRec.Recognizer()


while(True):
    print()
    s = input("Shall we proceed?(Y/N): ")
    if(s=='N' or s=='n'):
        print('Quitting virtual assistant!')
        break
    else:
        runVirtualAssistant()



    