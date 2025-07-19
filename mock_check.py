
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# Define the scope and credentials
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'your_credentials_file.json'
VIEW_ID = 'your_view_id'

# Authenticate with the Google Analytics API
credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Get the date range for the last 7 days
end_date = datetime.now().date()
start_date = end_date - timedelta(days=7)

# Query the Google Analytics API to retrieve the total number of sessions for the last 7 days
response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': start_date.strftime('%Y-%m-%d'), 'endDate': end_date.strftime('%Y-%m-%d')}],
                'metrics': [{'expression': 'ga:sessions'}]
            }
        ]
    }
).execute()

# Print the total number of sessions
print('Total sessions for the last 7 days:', response['reports'][0]['data']['totals'][0]['values'][0])
