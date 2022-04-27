import csv
import json
import webbrowser as html
import json_format_model
import pandas as pd
import os

# For debugging
file_json_path_global = "PAL6_Automation_100.0_2.0_BANDWIDTH_80_ADAPT_20220307-142516.json"
csv_testing_file_1 = "./Testing_Purposes/PAL6_Automation_100.0_2.0_BANDWIDTH_80_ADAPT_20220424-105755.csv"
csv_testing_file_2 = "./Testing_Purposes/PAL6_Automation_100.0_2.0_BANDWIDTH_80_ADAPT_20220424-110148.csv"
json_testing_file_1 = "Testing_Purposes/PAL6_Automation_100.0_2.0_BANDWIDTH_80_ADAPT_20220424-105755.json"
json_testing_file_2 = "Testing_Purposes/PAL6_Automation_100.0_2.0_BANDWIDTH_80_ADAPT_20220424-110148.json"

''' This is a parsing method:
    The method takes in a csv file path and output data into a json file path'''


class ParsingToJson(object):
    args_counter = 0

    # Taking the csv file and creating a json file
    def __init__(self, file_csv_path: csv, file_json_path: json, automation_csv_data, config_csv_row_index_cnt):
        # TODO - self.automation_csv_data may not be used locally need to verify
        self.automation_csv_data = automation_csv_data
        self.json_data = {}
        self.config_csv_row_index_cnt = config_csv_row_index_cnt
        self.name = file_csv_path
        self.file_csv_path = self.name
        self.file_json_path = file_json_path
        self.json_obj = self.build_json_format()
        self.add_test_data()
        self.json_obj.add_dut_data_to_json(automation_csv_data,config_csv_row_index_cnt)
        self.dump_to_json_file()

    # TODO - open HTML tab for automation
    def start_html(self):
        html.open('/home/octoscope/Octoscope_New/new edited octo api/index.html')

    # Dump data as json to file
    def dump_to_json_file(self):
        with open(self.file_json_path, "w") as json_file:
            json.dump(self.json_data, json_file, indent=4)

    #  TODO - NEEDS TO PROMPT A MESSAGE BOX TO ASK IF USER WISHES TO UPLOAD TEST
    #     os.system(f'curl --noproxy "*" -X POST -H "Content-Type: application/json" -d @{self.file_json_path}  http://10.189.245.253:3001/api/addsuite')

    def build_json_format(self):
        my_json = json_format_model.RequiredJsonFormat(self)
        self.json_data = my_json.format()
        return my_json

    # Adding the data to the measurements section
    def add_test_data(self):
        found = False
        with open(self.file_csv_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            try:
                for row in reader:
                    if row == list():
                        pass
                    elif found:
                        self.json_obj.adding_test_results(row)
                    elif row[0] == "Step Index" or found:
                        found = True
            except Exception as e:
                print(f"Error was found {e.__str__()}")


if __name__ == "__main__":
    ParsingToJson(csv_testing_file_1, json_testing_file_1, pd.read_excel("Octoscope_Configuration.xlsx"))
    ParsingToJson(csv_testing_file_2, json_testing_file_2, pd.read_excel("Octoscope_Configuration.xlsx"))
