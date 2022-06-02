import datetime
import re


class RequiredJsonFormat(object):
    ''' This class holds static values:
    1. start -> testResult -> testCases -> testParams -> AP
    2. start -> testResult -> testCases -> test_steps -> measurement
    3. '''

    def __init__(self, json_controller):
        self.json_controller = json_controller
        self.start = {"test_results": [], "wcs_sta1_info": "NA", "test_name": "MAC_RVR",
                      "Setup_name": "Octoscope", "DUT_platform": "NA", "ID": "", "DUT_Build_Version": "NA",
                      "test_type": "MAC_RVR"}
        self.start_testResult = {"test_cases": [], "test_comments": [], "test_type": "MAC_RVR"}
        # In log link need to provide full path to file
        self.start_testResult_testCases = {"log_link": f"{self.json_controller.file_json_path}".replace('/', '\\'),
                                           "test_params": {}, "test_steps": [], "test_type": "MAC_RVR"}
        # All objects that are added should be inside this object
        self.start_testResult_testCases_testParams = {"AP": {}, "test_type": "MAC_RVR"}
        self.start_testResult_testCases_testParams_AP = {"Direction": "NA", "Protocol": "NA", "Channel Mode": "NA",
                                                         "Regulatory Domain": "NA", "Protocol": "NA", "Band": "NA", "Security":"NA",
                                                         "Mode": "NA", "Channel": "NA"}
        self.test_cases = None
        self.start["ID"] = datetime.datetime.now().strftime("%d%m%Y%H%M%S_Octoscope")
        self.dict_name_variable = [self.start, self.start_testResult, self.start_testResult_testCases,
                                   self.start_testResult_testCases_testParams,
                                   self.start_testResult_testCases_testParams_AP]
        self.dict_format = dict()

    # Formatting the json according to UTAF specs
    def format(self) -> dict:
        try:
            self.dict_format.update(self.start)
            lis = self.dict_format.get("test_results")
            lis.append(self.start_testResult)
            [lis] = self.dict_format.get("test_results")
            lis = lis.get("test_cases")
            lis.append(self.start_testResult_testCases)
            [lis] = lis
            lis_1 = lis.get("test_params")
            lis_1.update(self.start_testResult_testCases_testParams)
            lis_1.get("AP").update(self.start_testResult_testCases_testParams_AP)
            lis_2 = lis.get("test_steps")
            self.test_cases = lis_2
        except AttributeError:
            print("!!!!!! AttributeError !!!!!!!")
        except ValueError:
            print("!!!!!! ValueError !!!!!!!")
        finally:
            return self.dict_format

    # Adding test result to JSON for each row
    def adding_test_results(self, row):
        # Validation if row is not valid return
        if row is None or row == [] or row.__len__ == 0:
            return
        # All objects that are added should be inside this object
        start_testResult_testCases_testSteps = {"log_link": "NA", "time_started": "NA", "test_params": "NA",
                                                "grade": "NA",
                                                "test_type": "NA",
                                                "QCID": "NA",
                                                "measurement": {"Attenuation0": "NA", "Throughput": "NA",
                                                                "Degree": "NA"}, "time_ended": "NA", "time": "NA",
                                                "test_name": "MAC_RVR",
                                                "test_comments": [], "test_description": "NA", "test_type": "MAC_RVR"}
        try:
            # Adding to measurement manually - each number in row is important to keep the order
            measurement = start_testResult_testCases_testSteps["measurement"]
            measurement["Degree"] = row[1].replace(" ", "")
            if row[2] != " 0":
                measurement["Attenuation0"] = "-" + row[2].replace(" ", "")
            else:
                measurement["Attenuation0"] = row[2].replace(" ", "")
            measurement["Throughput"] = row[3].replace(" ", "")
        except Exception as e:
            print(e)
        finally:
            self.test_cases.append(start_testResult_testCases_testSteps)

    def add_dut_data_to_json(self, csv_data, csv_row_index):
        try:
            #  Starting the parsing
            # Adding test name
            self.dict_format["test_name"] = csv_data["TEST NAME"][csv_row_index]
            # Adding client as pal6
            self.dict_format["wcs_sta1_info"] = csv_data["Client"][csv_row_index]
            # Adding channel
            self.dict_format["test_results"][0]['test_cases'][0]['test_params']['AP']['Channel'] = int(
                csv_data["Channel"][csv_row_index])
            # adding channel mode = bandwidth
            [bandwidth_value] = re.findall(r'\d+', csv_data["BANDWIDTH"][csv_row_index])
            self.dict_format["test_results"][0]['test_cases'][0]['test_params']['AP']['Channel Mode'] = bandwidth_value+"MHz"
            # Adding Channel mode = network mode AX, AC etc
            [channel_mode_reg] = re.findall(r'(?<=_)\w+',csv_data["WIFi_INTERFACE"][csv_row_index])
            self.dict_format["test_results"][0]['test_cases'][0]['test_params']['AP']['Mode'] = channel_mode_reg
            # Radio 2.5 and 5G adding
            [radio_type_reg] = re.findall(r'(?<=_)\w+',csv_data["RADIO_TYPE"][csv_row_index])
            self.dict_format["test_results"][0]['test_cases'][0]['test_params']['AP']['Band'] = radio_type_reg+"GHz"
            # Security type WPA2 etc
            [radio_type_reg] = re.findall(r'(?<=_)\w+', csv_data["Security"][csv_row_index])
            self.dict_format["test_results"][0]['test_cases'][0]['test_params']['AP']['Security'] = radio_type_reg
        except Exception as e:
            print(e)