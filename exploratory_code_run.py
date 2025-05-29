
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Set up credentials
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path/to/your/credentials.json'
VIEW_ID = 'your_view_id'

credentials = Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)

# Authenticate and create the service object
if not credentials.valid:
    credentials.refresh(Request())

analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Get user behavior data
response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:users'}],
                'dimensions': [{'name': 'ga:date'}]
            }
        ]
    }
).execute()

# Parse and print the user behavior data
for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        date = row['dimensions'][0]
        users = row['metrics'][0]['values'][0]
        print(f'Date: {date}, Users: {users}')
