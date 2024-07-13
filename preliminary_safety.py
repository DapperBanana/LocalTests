
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path/to/json-key-file.json'
VIEW_ID = 'your-view-id'

credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=SCOPES)

analytics = build('analyticsreporting', 'v4', credentials=credentials)

response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}]
            }
        ]
    }
).execute()

for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        sessions = row.get('metrics', [])[0].get('values', [])[0]
        print('Number of sessions in the last 7 days: %s' % sessions)
