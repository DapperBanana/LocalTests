
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Analytics API credentials
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path/to/your/credentials.json'
VIEW_ID = 'your-view-id'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    KEY_FILE_LOCATION, SCOPES)

# Build the Google Analytics service
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Query Google Analytics API for user behavior data
response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:avgSessionDuration'}],
                'dimensions': [{'name': 'ga:pagePath'}],
                'orderBys': [{'fieldName': 'ga:sessions', 'sortOrder': 'DESCENDING'}],
            }
        ]
    }
).execute()

# Process and analyze the user behavior data
for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        page_path = row.get('dimensions')[0]
        sessions = row.get('metrics')[0].get('values')[0]
        avg_session_duration = row.get('metrics')[0].get('values')[1]

        print(f'Page path: {page_path}')
        print(f'Sessions: {sessions}')
        print(f'Average session duration: {avg_session_duration}')
