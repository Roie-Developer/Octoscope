import csv
import json
import webbrowser as html
import json_format

file_csv_name_global = "Octoscope_Configuration.xlsx"
file_json_name_global = "PAL6_Automation_100.0_2.0_BANDWIDTH_80_ADAPT_20220307-142516.json"

''' This is a parsing method:
    The method takes in a csv file path and output data into a json file path'''

class ParsingToJson(object):

    def __init__(self, file_csv_name: csv, file_json_name: json):
        self.json_data = {}
        self.file2437_csv_name = file_csv_name
        self.file_json_name = file_json_name
        self.build_json_format()

    def parse(self):
        with open(self.file_csv_name, "r") as csv_file:
            reader = csv.reader(csv_file)
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
                        self.json_data["test_results"].append({st1[0]: st1[1]})
                    else:
                        st2 = row.split("(", 1)
                        self.json_data["test_results"].append({st2[0]: "(" + st2[1]})
        except IndexError as e:
            print(f"End of the first part: {e}")
        except Exception as e:
            print(f"Error happened in parse_test_info ... {e}")

    # TODO: improve methods
    def parse_data_section(self,csv_file):
        name_list = []
        flag = False
        # This loop will iterate over each line of data inside the csv file
        for row in csv_file:
            try:
                if str(row[0]) == "Test Run":
                    name_list = row
                    for name in row:
                        self.json_data["test_results"].append({name: []})
                elif str(row[0]) != "#":
                    #  This loop will iterate over each dictionary key and append test result to list value
                    for index, name in enumerate(name_list):
                        [my_data_values] = self.json_data.values()
                        [adding_data_to_json] = my_data_values[self.row_pos + index].values()
                        if row[0] == '#' or flag:
                            self.json_data["test_results"].append({name: []})
                            flag = True
                            print("here in data section reach avg parm")
                        elif flag:
                            pass
                        else:
                            adding_data_to_json.append(row[index])
            except IndexError as e:
                print(f"Error in while parsing data {e}")

    def start_html(self):
        html.open('/home/octoscope/Octoscope_New/new edited octo api/index.html')

    def dump_to_json_file(self):
        # Dump data as json to file
        with open(self.file_json_name, "w") as json_file:
            json.dump(self.json_data, json_file,indent=4)

    def build_json_format(self):
        my_json = json_format.RequiredJsonFormat()
        self.json_data = my_json.format()
        # print(self.json_data )
        self.dump_to_json_file()



# if __name__ == "__main__":
#     ParsingToJson(file_csv_name_global, file_json_name_global)
