class RequiredJsonFormat(object):
    ''' This class holds static values:
    1. start -> testResult -> testCases -> testParams -> AP
    2. start -> testResult -> testCases -> test_steps -> measurement
    3. '''

    def __init__(self):
        self.start = {"test_results": [], "wcs_sta1_info": "NA", "test_name": "MAC_Throughput",
                      "Setup_name": "TP3", "DUT_platform": "", "ID": "", "DUT_Build_Version": "NA"}

        self.start_testResult = {"test_cases": [], "test_comments": []}

        # In log link need to provide full path to file
        self.start_testResult_testCases = {"log_link": "NA", "test_params": {}, "test_steps": []}

        # All objects that are added should be inside this object
        self.start_testResult_testCases_testParams = {"AP": {}}

        self.start_testResult_testCases_testParams_AP = {"Direction": "NA", "Protocol": "NA", "Channel Mode": "NA",
                                                         "Regulatory Domain": "NA",
                                                         "Mode": "NA", "Channel": "NA"}

        self.test_cases = None

        self.dict_name_variable = [self.start, self.start_testResult, self.start_testResult_testCases,
                                   self.start_testResult_testCases_testParams,
                                   self.start_testResult_testCases_testParams_AP]

    # Formatting the json according to UTAF specs
    def format(self):
        try:
            dict_format = dict()
            dict_format.update(self.start)
            lis = dict_format.get("test_results")
            lis.append(self.start_testResult)
            [lis] = dict_format.get("test_results")
            lis = lis.get("test_cases")
            lis.append(self.start_testResult_testCases)
            [lis] = lis
            lis_1 = lis.get("test_params")
            lis_1.update(self.start_testResult_testCases_testParams)
            lis_1.get("AP").update(self.start_testResult_testCases_testParams_AP)
            lis_2 = lis.get("test_steps")
            self.test_cases = lis_2
            print("formatting is done")
            return dict_format
        except AttributeError:
            print("!!!!!! AttributeError !!!!!!!")
            return AttributeError
        except ValueError:
            print("!!!!!! ValueError !!!!!!!")
            return dict_format
        return None

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
                                                "test_name": "NA",
                                                "test_comments": [], "test_description": "NA"}
        try:
            measurement = start_testResult_testCases_testSteps["measurement"]
            measurement["Degree"] = row[1].replace(" ","")
            if row[2] != " 0":
                measurement["Attenuation0"] = "-" + row[2].replace(" ","")
            else:
                measurement["Attenuation0"] = row[2].replace(" ","")
            measurement["Throughput"] = row[3].replace(" ","")
            self.test_cases.append(start_testResult_testCases_testSteps)
        except Exception as e:
            print(e)
