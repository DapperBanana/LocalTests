
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path/to/your/keyfile.json'
VIEW_ID = 'your_view_id'

# Create a service object
credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
service = build('analyticsreporting', 'v4', credentials=credentials)

# Get user behavior data
response = service.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'yesterday'}],
                'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:pageviews'}],
                'dimensions': [{'name': 'ga:pagePath'}],
            }
        ]
    }
).execute()

# Parse and display the data
data = response['reports'][0]['data']['rows']

df = pd.DataFrame(data)
df.columns = ['Page Path', 'Sessions', 'Pageviews']

print(df)
