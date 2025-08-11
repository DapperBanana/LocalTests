
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Set up the credentials
credentials = Credentials(
    'YOUR_ACCESS_TOKEN',
    refresh_token='YOUR_REFRESH_TOKEN',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    token_uri='https://oauth2.googleapis.com/token',
)

# Create a Google Analytics service object
service = build('analyticsreporting', 'v4', credentials=credentials)

# Select the Google Analytics view to query
VIEW_ID = 'YOUR_VIEW_ID'

# Query parameters
date_range = {'startDate': '2022-01-01', 'endDate': '2022-01-31'}
metrics = [{'expression': 'ga:sessions'}]
dimensions = [{'name': 'ga:country'}]

# Query the Google Analytics API
response = service.reports().batchGet(
    body={
        'reportRequests': [{
            'viewId': VIEW_ID,
            'dateRanges': [date_range],
            'metrics': metrics,
            'dimensions': dimensions
        }]
    }
).execute()

# Print the results
for report in response.get('reports', []):
    print('Report data:')
    for row in report.get('data', {}).get('rows', []):
        country = row.get('dimensions')[0]
        sessions = row.get('metrics')[0].get('values')[0]
        print(f'{country}: {sessions} sessions')
