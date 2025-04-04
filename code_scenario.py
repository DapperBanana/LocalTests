
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Analytics API credentials
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path/to/service_account_key.json'
VIEW_ID = 'your_view_id'

# Authenticate with Google Analytics API
credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Get user behavior data for a specific website
response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:users'}, {'expression': 'ga:sessions'}],
            }
        ]
    }
).execute()

# Parse and print the user behavior data
for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        users = row.get('metrics', [])[0]['values'][0]
        sessions = row.get('metrics', [])[0]['values'][1]
        print(f'Users: {users}, Sessions: {sessions}')
