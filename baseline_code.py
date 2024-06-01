
import os
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Set up credentials
key_file_location = 'path_to_your_service_account_key.json'
view_id = 'your_google_analytics_view_id'

credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, ['https://www.googleapis.com/auth/analytics.readonly'])
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Retrieve data from Google Analytics API
response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': view_id,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}],
                'dimensions': [{'name': 'ga:country'}]
            }
        ]
    }
).execute()

# Process and display data
for report in response.get('reports', []):
    rows = report.get('data', {}).get('rows', [])

    for row in rows:
        country = row.get('dimensions')[0]
        sessions = row.get('metrics')[0].get('values')[0]

        print(f'Country: {country}, Sessions: {sessions}')
