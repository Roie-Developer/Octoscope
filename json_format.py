class RequiredJsonFormat(object):
    ''' This class holds static values:
    1. start -> testResult -> testCases -> testParams -> AP
    2. start -> testResult -> testCases -> test_steps -> measurement
    3. '''

    def __init__(self):
        self.start = {"test_results": [], "wcs_sta1_info": "NA", "test_name": "MAC_Throughput",
                      "Setup_name": "TP3", "DUT_platform": "", "ID": "", "DUT_Build_Version": ""}

        self.start_testResult = {"test_cases": [], "test_comments": []}

        # In log link need to provide full path to file
        self.start_testResult_testCases = {"log_link": "", "test_params": {}, "test_steps": []}

        # All objects that are added should be inside this object
        self.start_testResult_testCases_testParams = {"AP": {}}

        self.start_testResult_testCases_testParams_AP = {"Direction": "NA", "Protocol": "NA", "Channel Mode": "NA",
                                                         "Regulatory Domain": "NA",
                                                         "Mode": "NA", "Channel": "NA"}

        # All objects that are added should be inside this object
        self.start_testResult_testCases_testSteps = {"log_link": "", "time_started": "", "test_params": "",
                                                     "grade": "NA",
                                                     "test_type": "",
                                                     "QCID": "NA",
                                                     "measurement": {}, "time_ended": "", "time": "", "test_name": "",
                                                     "test_comments": [], "test_description": ""}

        # All objects that are added should be inside this object - holds test indict_formation
        self.measurement = { "Attenuation0": "","Throughput": "",}

        self.append_measurements = None

        self.dict_name_variable = [self.start, self.start_testResult, self.start_testResult_testCases,
                                   self.start_testResult_testCases_testParams,
                                   self.start_testResult_testCases_testParams_AP,
                                   self.start_testResult_testCases_testSteps,
                                   self.measurement]

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
            lis_2.append(self.start_testResult_testCases_testSteps)
            self.append_measurements = lis_2
            [lis_2] = lis_2
            lis_2.get("measurement").update(self.measurement)
            print("formatting is done")
            return dict_format
        except AttributeError:
            print("!!!!!! AttributeError !!!!!!!")
            return AttributeError
        except ValueError:
            print("!!!!!! ValueError !!!!!!!")
            return dict_format
        return None


    def adding_measurement(self,row_measurement):
        print(row_measurement)




