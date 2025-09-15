
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Set up the credentials
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path/to/your/credentials.json'
VIEW_ID = 'your_view_id'

credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)

# Create a service object
service = build('analyticsreporting', 'v4', credentials=credentials)

# Get the top 10 pages by pageviews
response = service.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:pageviews'}],
                'dimensions': [{'name': 'ga:pagePath'}],
                'orderBys': [{'fieldName': 'ga:pageviews', 'sortOrder': 'DESCENDING'}],
                'pageSize': 10
            }
        ]
    }
).execute()

# Print the results
for report in response.get('reports', []):
    for row in report.get('data', {}).get('rows', []):
        page_path = row.get('dimensions')[0]
        page_views = int(row.get('metrics')[0].get('values')[0])
        print(f'{page_path}: {page_views} pageviews')
