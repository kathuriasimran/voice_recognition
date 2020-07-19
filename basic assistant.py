import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print("LISTENING....")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        if(text.find(".com")<0):
            text=text+".com"
        
        print("OPENING "+text)
        url = text

        webbrowser.register('chrome',
	        None,
	        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)

    except:
        print("sorry try again")