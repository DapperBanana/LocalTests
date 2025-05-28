
from apiclient.discovery import build
from google.auth import compute_engine
import pandas as pd

def initialize_analyticsreporting():
    credentials = compute_engine.Credentials()
    return build('analyticsreporting', 'v4', credentials=credentials)

def get_report(analytics, view_id, start_date, end_date):
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
                    'metrics': [{'expression': 'ga:users'}],
                    'dimensions': [{'name': 'ga:date'}]
                }
            ]
        }  
    ).execute()

def print_report(response):
    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
        
        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                print(header + ': ' + dimension)

            for i, values in enumerate(dateRangeValues):
                print('Date range (' + str(i) + ')')
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    print(metricHeader.get('name') + ': ' + value)

if __name__ == '__main__':
    analytics = initialize_analyticsreporting()
    view_id = 'YOUR_VIEW_ID'
    start_date = '2021-01-01'
    end_date = '2021-01-31'
    response = get_report(analytics, view_id, start_date, end_date)
    print_report(response)
