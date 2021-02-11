from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import tkinter as tk

print('moduler är importerade')


height = 550
width = 950

app = tk.Tk()


app.title('Mail Client')
canvas = tk.Canvas(app, height=height, width=width)
canvas.pack()


frame = tk.Frame(app, bg='lightgray')
frame.place(relwidth=1, relheight=1)

print('tkinter är redo')

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
        print('pickle token är redo')
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

# Funktioner
def subjectClick(event):
    subjectBox.delete(0, 'end')

def recieverClick(event):
    recieverBox.delete(0, 'end')

def textClick(event):
    textBox.delete('1.0', 'end')

def sendButton(event):
    message = textBox.get('1.0', 'end')
    subject = subjectBox.get()
    reciever = recieverBox.get()

    print('Nu klickades knappen')

    mail = ('me', reciever, subject, message)
    send_message(service, 'me', mail)
    print('Skickat!')


def send_message(service, user_id, message):
    try:
        print('nu ska ett meddelande skickas')    
        message = (service.users().messages().send(userId='me', body=message).execute())
        print ('Message Id: %s') % message['id']
        print('Nu ska meddelandet skickas')
        return message
    except Exception as error:
        print ('An error occurred: %s') % error

# Här skriver man meddelandet
textBox = tk.Text(app)
textBox.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.25)
textBox.config(font =  ('Sans', 11))
textBox.insert('1.0', 'Message')
textBox.bind('<Button-1>', textClick)


# Skriver in ämnet i denna entry
subjectBox = tk.Entry(app)
subjectBox.place(relwidth=0.30, relheight=0.05, relx=0.55, rely=0.15)
subjectBox.insert(0, 'Subject')
subjectBox.bind('<Button-1>', subjectClick)


# I denna entry fyller man i epostadressen
recieverBox = tk.Entry(app)
recieverBox.place(relwidth=0.30, relheight=0.05, relx= 0.15, rely=0.15)
recieverBox.insert(0, 'E-mail')
recieverBox.bind('<Button-1>', recieverClick)

# Knappen som skickar meddelandet
button = tk.Button(app, text='Skicka', bg='white')
button.place(relheight=0.10, relwidth=0.15, relx=0.7, rely=0.80)
button.config(font = ('Sans', 14, 'bold'))
button.bind('<Button-1>', sendButton)

print('GUIn är redo')

app.mainloop()