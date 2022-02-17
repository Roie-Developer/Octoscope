import csv
import json

''' This is a parsing method:
    The method takes in a csv file path and output data into a json file path'''

class ParsingToJson():
    count = True
    def __init__(self, file_csv_name : csv, file_json_name : json):
        print(f"This is file_json_name type: {file_json_name}")
        if self.count:
            self.json_data = {"names": []}
            self.json_test_result = {"results": []}
            self.file_csv_name = file_csv_name
            self.file_json_name = file_json_name
            self.count = False

    def parse(self):
        with open(self.file_csv_name, "r") as csv_file:
            reader = csv.reader(csv_file)
            name_list = []
            for row in reader:
                try:
                    if row[0][0] == "#":
                        row = " ".join(row)
                        if row.__contains__(":"):
                            st1 = row.split(":", 1)
                            self.json_data["names"].append({st1[0]: st1[1]})
                            print(self.json_data)
                        else:
                            st2 = row.split("(", 1)
                            self.json_data["names"].append({st2[0]: "(" + st2[1]})
                    else:
                        if str(row[0]) == "Test Run":
                            name_list = row
                            for name in row:
                                self.json_test_result["results"].append({name: []})
                        else:
                            pos = 0
                            for name in name_list:
                                print(f"Here is json_result[]")
                                self.json_test_result["result"][name].append(row[pos])
                                pos += 1
                except IndexError as e:
                    print(f"End of the first part: {e}")
                except Exception as e:
                    print(f"Finished writing data: {e}")
                    break
        # Dump data as json to file
        with open(self.file_json_name, "w") as json_file:
            json.dump(self.json_data, json_file, indent=4)
            json.dump(self.json_test_result, json_file, indent=4)
