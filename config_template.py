# change API_TOKEN to your api key. Password is the correct one
API_TOKEN = "insert your key here"
PASSWORD = "api_token"
HTTP_BASIC_AUTH_CREDS = (API_TOKEN, PASSWORD)

# toggl API URI's to retrieve workspace id and detailed reports
WORKSPACES_URL = "https://api.track.toggl.com/api/v8/workspaces"
DETAILED_REPORTS_URL = "https://api.track.toggl.com/reports/api/v2/details"

# tasks above this threshold are classified as 'deep work'; 55 minutes by default
deep_work_threshold_in_mins = 60
