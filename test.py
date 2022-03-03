import csv
import json
import re

''' This is a parsing method:
    The method takes in a csv file path and output data into a json file path'''

class ParsingToJson():

    def __init__(self, file_csv_name: csv, file_json_name: json):
            self.json_data = {"data": []}
            self.file_csv_name = file_csv_name
            self.file_json_name = file_json_name
            self.row_pos = 0

    def parse(self):
        with open(self.file_csv_name, "r") as csv_file:
            index = 0
            reader = csv.reader(csv_file)
            print(f"This is the index after {index}")
            self.parse_test_info(reader)
            self.parse_data_section(reader)
        self.dump_to_json_file()

    def parse_test_info(self, csv_file):
        try:
            for row in csv_file:
                if row[0][0] == "#":
                    self.row_pos += 1
                    row = " ".join(row)
                    if row.__contains__(":"):
                        st1 = row.split(":", 1)
                        self.json_data["data"].append({st1[0]: st1[1]})
                    else:
                        st2 = row.split("(", 1)
                        self.json_data["data"].append({st2[0]: "(" + st2[1]})
        except IndexError as e:
            print(f"End of the first part: {e}")
        except Exception as e :
            print(f"Error happened in parse_test_info ... {e}")

    def parse_data_section(self,csv_file):
        name_list = []
        row_pos_starting_value = self.row_pos
        # This loop will iterate over each line of data inside the csv file
        for row in csv_file:
            try:
                if str(row[0]) == "Test Run":
                    name_list = row
                    for name in row:
                        self.json_data["data"].append({name: []})
                elif str(row[0]) != "#":
                    #  This loop will iterate over each dictionary key and append test result to list value
                    for index, name in enumerate(name_list):
                        [my_data_values] = self.json_data.values()
                        [adding_data_to_json] = my_data_values[self.row_pos + index].values()
                        adding_data_to_json.append(row[index])
            except IndexError as e:
                print(f"Error in while parsing data {e}")

    def dump_to_json_file(self):
        # Dump data as json to file
        with open(self.file_json_name, "w") as json_file:
            json.dump(self.json_data, json_file, indent=4)
