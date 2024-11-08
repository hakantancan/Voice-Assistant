from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser


r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        r.adjust_for_ambient_noise(source, duration=0.5)  
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice


def response(voice):
    if "merhaba" in voice:
        speak("Sana da merhaba")
    if "selam" in voice:
        speak("sana 2 kere selam olsun")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    if "görüşürüz" in voice:
        speak("görüşmek üzere")
        exit()
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"
        
        elif today == "Tuesday":
            today = "Salı"
         
        elif today == "Wednesday":
            today = "Çarşamba"
            
        elif today == "Thursday":
            today = "Perşembe"
            
        elif today == "Friday":
            today = "Cuma"
            
        elif today == "Saturday":
            today = "Cumartesi"
            
        elif today == "Sunday":
            today = "Pazar"
            
        speak("Bugün günlerden:" + today)
        
    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: ", "Bir bakayım: ", "Saat"]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

        
    if "google'da ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}.".format(search)
        webbrowser.get().open(url)
        speak("{} için Google'da bulabildiklerimi listeliyorum".format(search))
        
    
    
    
        
    if "uygulama" in voice:
        speak("Hangi uygulamayı açmamı istersin?")
        runApp = record()
        
       
        if runApp:
            runApp = runApp.lower()
            
            if "league of legends" in runApp:
                os.startfile(r"C:\Riot Games\Riot Client\RiotClientServices.exe")
                speak("İstediğiniz uygulamayı çalıştırıyorum")
                
            elif "Visual Studio" in runApp:
                os.startfile(r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe")
                speak("İstediğiniz uygulamayı çalıştırıyorum")
                
            else:
                speak("Bu uygulamayı bulamadım.")
        else:
            speak("Uygulama ismi almadım.")
            
    if "not al" in voice:
        speak("Dosya ismi ne olsun?")
        txtFile = record() + ".txt"
        speak("Ne kaydetmek istiyorsun?")
        theText = record()
        f = open(txtFile,"w",encoding="utf-8")
        f.writelines(theText)
        f.close()
            

def speak(text):
    tts = gTTS(text=text, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)  
    try:
        playsound(file)  
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        if os.path.exists(file):  
            os.remove(file)


speak("Merhaba Hakan")



while True:
    print("Asistan: Dinliyorum...")
    voice = record()
    if voice:
        voice = voice.lower()
        print(f"Kullanıcı: {voice}")
        response(voice)
    time.sleep(1)  
