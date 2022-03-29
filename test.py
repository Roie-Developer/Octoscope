import csv
import json
import webbrowser as html
import json_format

file_csv_name_global = "Octoscope_Configuration.xlsx"
file_json_name_global = "PAL6_Automation_100.0_2.0_BANDWIDTH_80_ADAPT_20220307-142516.json"

''' This is a parsing method:
    The method takes in a csv file path and output data into a json file path'''


class ParsingToJson(object):

    # Taking the csv file and creating a json file
    def __init__(self, file_csv_name: csv, file_json_name: json):
        self.json_data = {}
        self.file_csv_name = file_csv_name
        self.file_json_name = file_json_name
        self.json_obj = self.build_json_format()
        self.add_test_data(self.json_obj)
        self.dump_to_json_file()

    def start_html(self):
        html.open('/home/octoscope/Octoscope_New/new edited octo api/index.html')

    def dump_to_json_file(self):
        # Dump data as json to file
        with open(self.file_json_name, "w") as json_file:
            json.dump(self.json_data, json_file, indent=4)

    def build_json_format(self):
        my_json = json_format.RequiredJsonFormat()
        self.json_data = my_json.format()
        return my_json

    # Adding the data to the measurements section
    def add_test_data(self, json_obj):
        cnt = 0
        found = False
        with open(self.file_csv_name, "r") as csv_file:
            reader = csv.reader(csv_file)
            try:
                for row in reader:
                    if row == list():
                        pass
                    elif found:
                        json_obj.adding_measurement(row)
                    elif row[0] == "# RvR Data" or found:
                        found = True
            except Exception as e:
                print(f"Error was found {e.__str__()}")

    #  For debugging purposes
if __name__ == "__main__":
    ParsingToJson(file_csv_name_global, file_json_name_global)
    ParsingToJson(file_csv_name_global, file_json_name_global)
