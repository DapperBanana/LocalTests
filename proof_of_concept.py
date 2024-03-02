
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Set up credentials
SERVICE_ACCOUNT_FILE = 'service-account.json'
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Set up Analytics API
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Get user behavior data
response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': 'xxxxxxxx',  # Replace with your Google Analytics view ID
                'dateRanges': [{'startDate': '2021-01-01', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:users'}, {'expression': 'ga:sessions'}],
                'dimensions': [{'name': 'ga:date'}]
            }
        ]
    }
).execute()

# Print user behavior data
for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        date = row.get('dimensions')[0]
        users = row.get('metrics')[0]['values'][0]
        sessions = row.get('metrics')[0]['values'][1]
        print(f'Date: {date} - Users: {users} - Sessions: {sessions}')
