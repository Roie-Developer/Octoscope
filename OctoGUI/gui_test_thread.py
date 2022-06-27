from PyQt5 import QtCore
from PyQt5.QtCore import *


class TestThread(QtCore.QThread, QObject):

    def __init__(self, octo, user_test_data):
        super(TestThread, self).__init__()
        self.user_test_data = user_test_data
        self.octo = octo

    def run(self):
        print("Automation is starting")
        self.octo.sys.argv = self.user_test_data["tests_seq"] 
        #  Need to verify the need for __name__ = "__main__"
        self.octo.__name__ = "__main__"
        self.octo.passing_data_from_gui = self.user_test_data
        # User started execution list with restarting PAL 6
        try:
            for i in range(len(self.user_test_data["Restart PAL6"])):
                if self.user_test_data["Restart PAL6"][0] == 0:
                    self.octo.json_controller.ParsingToJson.restart_pal6(self)
                    self.user_test_data["Restart PAL6"].pop(0)
                    for i in range(len(self.user_test_data["Restart PAL6"])):
                        self.user_test_data["Restart PAL6"][i] -= 1 
                else:
                    break
        except IndexError as e:
            print(f"\nError happend:\n{e}")
        if len(self.user_test_data["tests_seq"]) > 0:
            self.octo.main()
        else:
            print("Only restart for PAL6 is needed")

    def stop(self):
        self.terminate()