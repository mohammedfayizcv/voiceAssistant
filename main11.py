import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
# arduino library
import serial
import time
    
# ser = serial.Serial('COM11', 9600)  # Change 'COM3' to your Arduino's port

openai.api_key="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"

completion=openai.Completion()

print('checked')


def Reply(question):
    prompt=f'fayiz:{question}\n Odin'
    response=completion.create(prompt=prompt,engine="text-davinci-002")
    answer=response.choices[0].text.strip()
    return answer



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("Hello how are you, may I help you?")
 
def takeComment():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listernig...")
        r.pause_threshold =1
        audio=r.listen(source)
    try:
        querry=r.recognize_google(audio, language='en-in')
        print("fayiz said: {} \n ".format(querry))
    except Exception as e:
        print("say it again....")
        return "None"
    return querry
    
if __name__=='__main__':
    while True:
        querry=takeComment().lower()
        print(querry)
        ans=Reply(querry)
        print(ans)
        speak(ans)
        # # Sending commands to Arduino based on recognized speech
        # if 'servo' in querry:
        #     ser.write(b'S')  # Sending 'S' for servo control
        #     time.sleep(1)  # Optional delay
        # elif 'LED' in querry:
        #     ser.write(b'L')  # Sending 'L' for LED control
        #     time.sleep(1)  # Optional delay
        if 'bye' in querry:
            speak("bye have a good day")
            break
        
# ser.close()