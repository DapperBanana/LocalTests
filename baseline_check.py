
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your credentials JSON file downloaded from the Google Developers Console
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
# Scopes required to access the Google Analytics API
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
# ID of the Google Analytics view you want to analyze
VIEW_ID = 'ga:<VIEW_ID>'
