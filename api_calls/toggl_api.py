import requests
import datetime as dt
import config


def get_workspace_id():
    # by default, retrieves first workspace id from Toggl
    workspaces = requests.get(config.WORKSPACES_URL, auth=config.HTTP_BASIC_AUTH_CREDS)
    workspaces = workspaces.json()
    return workspaces[0]["id"]


# defines request parameters required by API, as well as explicitly defines default end and start date
default_end_date = dt.date.today()
default_start_date = default_end_date - dt.timedelta(days=6)
default_api_call_params = {"user_agent": "python",
                           "workspace_id": get_workspace_id(),
                           "since": default_start_date,
                           "until": default_end_date}


def calc_time_period(start, end):
    time_period = str(start) + " to " + str(end)
    return time_period


def change_dates():
    # creates new params
    new_params = default_api_call_params
    start_date = input("Enter start date: (YYYY-MM-DD)\n")
    end_date = input("Enter end date: (YYYY-MM-DD)\n")
    new_params["since"] = start_date
    new_params["until"] = end_date
    return new_params


def toggl_api_caller(api_call_params):
    # uses URI and auth credentials from config.py file
    detailed_report = requests.get(config.DETAILED_REPORTS_URL,
                                   auth=config.HTTP_BASIC_AUTH_CREDS,
                                   params=api_call_params)
    detailed_report = detailed_report.json()
    return detailed_report["data"]