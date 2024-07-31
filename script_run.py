
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# Set up Google Analytics API credentials
KEY_FILE_LOCATION = 'path_to_service_account_key_file.json'
VIEW_ID = 'your_view_id'

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Query Google Analytics API for user behavior data
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

# Print out the user behavior data
print('User behavior data for the last 7 days:')
for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        date = row.get('dimensions')[0]
        users = row.get('metrics')[0].get('values')[0]

        print(f'{date}: {users} users')

