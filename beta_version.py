
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path_to_json_file_downloaded_from_google_cloud_platform'
VIEW_ID = 'your_google_analytics_view_id'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    KEY_FILE_LOCATION, SCOPES)

analytics = build('analyticsreporting', 'v4', credentials=credentials)

response = analytics.reports().batchGet(
    body={
        'reportRequests': [{
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
            'metrics': [{'expression': 'ga:sessions'}]
        }]
    }
).execute()

for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        print('Sessions:', row['metrics'][0]['values'][0])
