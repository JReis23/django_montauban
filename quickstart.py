from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    calendar_list_entry = service.calendarList().get(calendarId='primary').execute()
    if calendar_list_entry['accessRole']:
        startTime = datetime.strptime(input("Please enter in the start time for the event in this format: (ex. September 02, 2018, 09:00PM) "), '%B %m, %Y, %I:%M%p').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        endTime = datetime.strptime(input("Please enter in the end time for the event in this format: (es. September 03, 2018, 11:25AM) "), '%B %m, %Y, %I:%M%p').strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        event = {    
            'summary': input("What's the name of the event? "),    # You can put inputs like this in dictionaries - it's stored in the key value directly, so there's no reason why not to. Continue to do this for all the information    # you need in the event, except for the times, which are already done    
            'location': 'Paris',    
            'description': 'test',    
            'start': {        
                'dateTime': startTime,        
                'timeZone': 'Europe/Paris',    
        },  'end': {        
            'dateTime': endTime,        
            'timeZone': 'Europe/Paris',    
        }
        
    ,}

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"The event has been created! View it at {event.get('htmlLink')}!")