
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up credentials
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path/to/your/credentials.json'
VIEW_ID = '12345678'

credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=SCOPES)

# Create the Analytics service object
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Get data from Google Analytics
def get_analytics_data(analytics, view_id):
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                    'metrics': [{'expression': 'ga:users'}],
                    'dimensions': [{'name': 'ga:source'}]
                }
            ]
        }
    ).execute()

response = get_analytics_data(analytics, VIEW_ID)
data = response['reports'][0]['data']['rows']

# Analyze user behavior
for row in data:
    source = row['dimensions'][0]
    users = int(row['metrics'][0]['values'][0])

    print(f"Source: {source}, Users: {users}")
