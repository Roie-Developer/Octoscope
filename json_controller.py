import csv
import json
import time
import os
import webbrowser as html
import json_format_model
import pandas as pd
from selenium import webdriver
import os

''' This is A parsing method:
    The method takes in a csv file path and output data into a json file path'''


class ParsingToJson(object):
    args_counter = 0
    # Taking the csv file and creating a json file
    def __init__(self, file_csv_path: csv, file_json_path: json, automation_csv_data,csv_row_index,
                 octobox, passing_data_from_gui):
        # self.restart_pal6()
        self.octobox = octobox
        self.automation_csv_data = automation_csv_data
        self.json_data = {}
        self.name = file_csv_path
        self.file_csv_path = self.name
        self.file_json_path = file_json_path
        self.gui_data = passing_data_from_gui
        self.json_obj = self.build_json_format()
        self.add_test_data()
        self.add_gui_test_data()
        self.json_obj.add_dut_data_to_json(automation_csv_data, csv_row_index)
        # self.learning_octobox()
        ''' def automation_end_process() - argument index: (All options output A csv file)
            Passing 0 - Creates A JSON file
            Passing 1 - Uploads the test to DB
            Passing 2 - Upload test to DB and creates A JSON file
            Passing 3 - Does nothing with the automation results
        '''
        if self.gui_data["load_test"] :
            self.automation_end_process(2)
        else:
            self.automation_end_process(0)



    # TODO - Change file directory of chrome - driver
    @staticmethod
    def restart_pal6(self):
        print("Restarting PAL 6 ")
        driver = None
        try:
            driver = webdriver.Chrome(
                executable_path='/home/octoscope/Octoscope_New/new edited octo api/RESTful API/chromedriver.exe')
            driver.get('http://localhost:5000/testbed-components#x')
            driver.find_element_by_id('systemResetTooltip_169.254.27.1').click()
        except Exception as e:
            print(f'In "def restart_pal6" restart was made with exception: {e}')
            os.system(f"/home/octoscope/Octoscope_New/new edited octo api/RESTful API/chromedriver.exe")
            driver = webdriver.Chrome(
                executable_path='/home/octoscope/Octoscope_New/new edited octo api/RESTful API/chromedriver.exe')
            driver.get('http://localhost:5000/testbed-components#x')
            driver.find_element_by_id('systemResetTooltip_169.254.27.1').click()
        finally:
            driver.close()
            # Sleep - waiting for pal6 to end restart - time measured to load pal6 is 1.5 minute
            print("Start sleeping for 120s, waiting for PAL6 to restart")
            time.sleep(60 * 2)


    # TODO - open HTML tab for automation
    def start_html(self):
        html.open('/home/octoscope/Octoscope_New/new edited octo api/index.html')

    # Dump data as json to file
    def dump_to_json_file(self):
        with open(self.file_json_path, "w") as json_file:
            json.dump(self.json_data, json_file, indent=4)
            #  TODO - NEEDS TO PROMPT A MESSAGE BOX TO ASK IF USER WISHES TO UPLOAD TEST
            # os.system(
            # f'curl --noproxy "*" -X POST -H "Content-Type: application/json" -d @{self.file_json_path} http://10.189.245.114:3001/api/addsuite'

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
                print(f'In  def add_test_data error occurred {e}')

    def add_gui_test_data(self):
        self.json_obj.adding_GUI_data_to_json(self.gui_data)



    # Self learning - can delete once finished
    def learning_octobox(self):
        try:
            print(f'This is attenuator - readAll: {self.octobox.attenuator.readAll()}')
        except Exception as e:
            print(f'In  def learning_octobox error occurred {e}')

    def automation_end_process(self, output=3):
        if output == 0:  # creates a json file
            self.dump_to_json_file()
        elif output == 1:  # upload json to database
            pass
            os.system(f'curl --noproxy "*" -X POST -H "Content-Type: application/json" -d @{self.file_json_path} http://10.189.245.115/api/addsuite')
        elif output == 2:  # upload and create a file
            self.dump_to_json_file()
            os.system(f'curl --noproxy "*" -X POST -H "Content-Type: application/json" -d @{self.file_json_path} http://10.189.245.115/api/addsuite')
        else:  # no action is taken once the test has finished - only csv file will be created
            return None
