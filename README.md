**Title:** Virtual Assistant (Scaler Task 1)

**Description:** It is a virtual assistant developed using Python. The virtual assistant speaks as well as writes its responses.

**Tasks the virtual assistant can perform:**
1. Open a webpage
2. Play a song on youtube
3. Tell weather or temperature of a place
4. Seach about anything on google
5. Tell today's date
6. Tell current time
7. Check internet speed
8. Check internet availability
9. Search latest news
10. Spell a word
11. Tell memory usage
12. Tell the user what all it can do

**Libraries Used:**
- SpeechRecognition: Library for performing speech recognition, with support for several engines and APIs, online and offline.
- pyttsx3: Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.
- pywhatkit: It is a python library that performs various functions like playing on youtube, searching on internet, sending a whatsapp message, converting images to handwriting etc.
- speedtest-cli: Command line interface for testing internet bandwidth using speedtest.net

**How to run:**
- This project uses Python 3.8.5
- The project dependencies are listed in requirements.txt file.
- Run the following command in command prompt: _pip install -r requirements.txt_
- Now run the project using the command: _python virtAssis.py_

**Important:**
In line 37 of the file virtAssis.py, replace "YOUR_API_KEY" with your api key from https://openweathermap.org/api
