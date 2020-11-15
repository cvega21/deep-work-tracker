import datetime as dt
import config
from api_calls import toggl_api as toggl


class DeepWorkData:
    def __init__(self):
        self.total_work_mins = 0
        self.total_deep_work_mins = 0
        self.pct = 0

    def create_data(self, params):
        # returns list with select data for records over specified deep work threshold
        report_data = toggl.toggl_api_caller(params)
        deep_work_records = []

        for record in report_data:
            # convert ms to seconds, add to total counter
            duration_in_mins = record["dur"] / 60000
            self.total_work_mins += duration_in_mins

            # if record is deep work, appends record to list
            if duration_in_mins > config.deep_work_threshold_in_mins:
                date = dt.datetime.fromisoformat(record["start"]).date()
                self.total_deep_work_mins += duration_in_mins
                current_record = {"duration_in_mins": duration_in_mins,
                                    "name": record["description"],
                                    "project": record["project"],
                                    "deep_work_bool": True,
                                    "date": date}
                deep_work_records.append(current_record)

        self.pct = self.total_deep_work_mins / self.total_work_mins
        return deep_work_records

    def summary(self):
        total_work_hours = round(self.total_work_mins / 60, 2)
        total_deep_work_hours = round(self.total_deep_work_mins / 60, 2)
        print("Deep Work threshold set at: " + str(config.deep_work_threshold_in_mins) + " mins.")
        print("You logged a total of " + str(total_deep_work_hours) + " deep work hours. ")
        print("You logged a total of " + str(total_work_hours) + " work hours. ")
        print("Deep work made up " + "{0:.2%}".format(self.pct) + " of your total work.")


def main():
    print("Welcome to Toggl API's Deep Work Tracker!")
    print("")
    print("The default time frame to generate a report is: " + str(toggl.default_start_date)
          + " to " + str(toggl.default_end_date))
    action = input("Enter 1 to create a report from this time frame. Enter 2 to change time frame.\n")
    deep_work_report = DeepWorkData()

    if action == "1":
        deep_work_report.create_data(toggl.default_api_call_params)
        print("Time Period: " + toggl.calc_time_period(toggl.default_start_date,toggl.default_end_date))
        deep_work_report.summary()

    elif action == "2":
        custom_api_call_params = toggl.change_dates()
        print("Time Period: " + toggl.calc_time_period(custom_api_call_params["since"], custom_api_call_params["until"]))
        deep_work_report.create_data(custom_api_call_params)
        deep_work_report.summary()

    else:
        print("Error. Type 1 or 2")
        return


main()
