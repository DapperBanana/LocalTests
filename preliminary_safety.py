
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path_to_your_json_key_file.json'
VIEW_ID = 'your_view_id'

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
            }]
    }
).execute()

print('Sessions:', response['reports'][0]['data']['totals'][0]['values'][0])
