
     import os
     from google.oauth2.service_account import Credentials
     from googleapiclient.discovery import build

     # Load credentials from JSON file
     credentials_filename = "credentials.json"
     credentials = Credentials.from_service_account_file(credentials_filename)

     # Create the service instance
     analytics = build('analyticsreporting', 'v4', credentials=credentials)
