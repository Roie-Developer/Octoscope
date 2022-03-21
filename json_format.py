
class RequiredJsonFormat(object):
    ''' This class holds static values:
    1. start -> testResult -> testCases -> testParams -> AP
    2. start -> testResult -> testCases -> test_steps -> measurement
    3. '''

    start = {"test_results": [], "wcs_sta1_info": "NA", "test_name": "MAC_Throughput",
             "Setup_name": "TP3", "DUT_platform": "", "ID": "", "DUT_Build_Version": ""}

    start_testResult = {"test_cases": [], "test_comments": []}

    # In log link need to provide full path to file
    start_testResult_testCases = {"log_link": "", "test_params": {}, "test_steps": []}

    # All objects that are added should be inside this object
    start_testResult_testCases_testParams = {"AP": {}}

    start_testResult_testCases_testParams_AP = {"Direction": "NA", "Protocol": "NA", "Channel Mode": "NA",
                                                "Regulatory Domain": "NA",
                                                "Mode": "NA", "Channel": "NA"}

    # All objects that are added should be inside this object
    start_testResult_testCases_testSteps = {"log_link": "", "time_started": "", "test_params": "", "grade": "NA",
                                            "test_type": "",
                                            "QCID": "NA",
                                            "measurement": {}, "time_ended": "", "time": "", "test_name": "",
                                            "test_comments": [], "test_description": ""}

    # All objects that are added should be inside this object - holds test indict_formation
    measurement = {"Phy Rate Transmit Stat": "NA", "Aeroflex Channel": "NA",
                   "PowerAntSelectionBwCp": "NA",
                   "Cpu All": "NA", "RSSI RX3": "", "Power Selection": "NA", "PER": "NA", "Pass/Fail": "NA",
                   "Variance Iteration": "NA",
                   "TX Power [dbm]": "NA", "RX Threshold": "NA", "Forced Rate": "NA", "BF bitmap": "NA",
                   "Network Protocol": "NA",
                   "Number Of Antennas": "NA", "Phy Rate Receive Stat": "NA", "Traffic Direction": "NA",
                   "Serial Number": "NA",
                   "BF Mode": "NA", "Fix Power": "NA", "Open Loop Mode": "NA", "Remark": "NA", "Attenuation0": "",
                   "Attenuation1": "",
                   "Attenuation2": "", "Attenuation3": "", "STBC": "NA", "20/40Co-Existence": "NA", "MU MIMO": "NA",
                   "RA Protection": "NA",
                   "Throughput": "NA", "LDPC": "NA", "RA Index": "NA", "Test Protocol": "NA", "Colum Number": "NA",
                   "EPM Measure Ant 2": "NA",
                   "EPM Measure Ant 3": "NA", "EPM Measure Ant 0": "NA", "EPM Measure Ant 1": "NA", "TXOP AMPTU": "NA",
                   "RSSI RX2": "NA", "RSSI RX1": "NA", "RSSI RX0": "NA", "Tcr0 Rf Power": "NA", "TXOP": "NA"}


    def __init__(self):
        self.dict_name_variable = [self.start, self.start_testResult, self.start_testResult_testCases,
                              self.start_testResult_testCases_testParams,
                              self.start_testResult_testCases_testParams_AP, self.start_testResult_testCases_testSteps,
                              self.measurement]

    def format(self):
        try:
            print(f"\nLine 1: format: \n{format} \n")
            dict_format = dict()
            dict_format.update(self.start)
            lis = dict_format.get("test_results")
            lis.append(self.start_testResult)
            print(f"\nLine 2: pre-bug format: \n{format} \n")
            [lis] = dict_format.get("test_results")
            print(f"\nLine 2: past-bug format: \n{format} \n")
            lis = lis.get("test_cases")
            lis.append(self.start_testResult_testCases)
            [lis] = lis
            lis_1 = lis.get("test_params")
            lis_1.update(self.start_testResult_testCases_testParams)
            lis_1.get("AP").update(self.start_testResult_testCases_testParams_AP)
            lis_2 = lis.get("test_steps")
            lis_2.append(self.start_testResult_testCases_testSteps)
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
