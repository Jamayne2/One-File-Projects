import smtplib
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
except:
    print("Did not get that")

def send_email():
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()
    server.login('email' ,'password')
    server.sendmail('sender_email',
                    'receiver_email',
                    'message')
