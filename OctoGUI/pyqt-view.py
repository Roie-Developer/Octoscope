import re
import time
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
sys.path.insert(1,"/home/octoscope/Octoscope_New/newEditedOctoApi/")
from PyQt5.uic import loadUiType
from PlotGraphs.start_graph import Canvas
from gui_test_thread import TestThread
import octo

ui, _ = loadUiType('library.ui')
        
class MainGui(QMainWindow, ui):

    def __init__(self):
        self.user_test_data = {"Restart_PAL6": list(), "load_test": True, "plot_chart": False, "tests_seq": ["First line is overlooked",], "build_version": "NA","regulatory_domain" : "US" ,"Submitter": "","Platform":"NA"}
        self.thread = TestThread(octo,self.user_test_data)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_UI_changes()
        self.set_text_edit_interactive(True)
        self.add_listeners()
        self.add_test_names()

    def handel_UI_changes(self):
        self.hide_user_input_widget()
        self.main_tab_widget.tabBar().setVisible(False)

    def show_user_input_widget(self):
        self.user_input_data_widget.show()
        self.user_input_data_widget.setEnabled(True)

    def hide_user_input_widget(self):
        self.user_input_data_widget.hide()
        self.user_input_data_widget.setEnabled(False)

    def show_submitter_name_widget(self):
        self.submitter_name_widget.show()
        self.submitter_name_widget.setEnabled(True)

    def hide_submitter_name_widget(self):
        self.submitter_name_widget.hide()
        self.submitter_name_widget.setEnabled(False)

    def set_text_edit_interactive(self, value: bool):
        self.log_text_edit.setReadOnly(value)

    # function became too long - so i splited it to two functions
    def add_listeners(self):
        self.button_listeners()
        self.other_listeners()

    def other_listeners(self):
        self.platforn_combo_box.currentTextChanged.connect(self.on_change_platforn)
        self.submitter_name_combo_box.currentTextChanged.connect(self.on_change_submitter_name)
        self.load_test_check_box.stateChanged.connect(self.upload_test)
        self.plot_test_check_box.stateChanged.connect(self.plot_test)
        self.regulatory_domain_combo_box.currentTextChanged.connect(self.on_change_regulatory_domain)
        self.add_test_to_excution_button.clicked.connect(self.add_test_profile)
        self.new_submitter_line_edit.textChanged.connect(self.new_submitter_name)
        self.plot_test_check_box.stateChanged.connect(self.append_grapgh)

    def button_listeners(self):
        self.plot_chart_button.clicked.connect(self.select_plot_chart_tab)
        self.test_data_button.clicked.connect(self.select_test_data_tab)
        self.user_data_show_button.clicked.connect(self.select_user_data_tab)
        self.test_log_button.clicked.connect(self.select_log_tab)
        self.start_test_button.clicked.connect(self.start_test)
        self.stop_test_button.clicked.connect(self.stop_test)
        self.remove_selected_button.clicked.connect(self.delete_item_from_execution_list)
        self.remove_all_button.clicked.connect(self.clear_execution_list)
        self.refresh_test_list_button.clicked.connect(self.add_test_names)
        self.open_csv_config_folder_button.clicked.connect(self.open_csv_config_folder)
        self.load_from_file_button.clicked.connect(self.load_from_file)
        self.save_test_to_file_button.clicked.connect(self.save_test_to_file)


    #############################################
    ############## Open Frame Tab ###############
    #############################################

    def select_user_data_tab(self):
        self.main_tab_widget.setCurrentIndex(0)

    def select_plot_chart_tab(self):
        self.main_tab_widget.setCurrentIndex(1)

    def select_test_data_tab(self):
        self.main_tab_widget.setCurrentIndex(2)

    def select_log_tab(self):
        self.main_tab_widget.setCurrentIndex(3)

    #############################################
    ############# Handel Combo Box ##############
    #############################################

    def on_change_platforn(self):
        txt = str(self.platforn_combo_box.currentText())
        if txt == "Other Vendor":
            self.hide_user_input_widget()
        else:
            self.show_user_input_widget()

    def on_change_submitter_name(self):
        txt = self.submitter_name_combo_box.currentText()
        if txt == "New":
            self.new_submitter_line_edit.setReadOnly(False)
            self.show_submitter_name_widget()
        else:
            self.new_submitter_line_edit.setReadOnly(True)
            self.hide_submitter_name_widget()
            self.user_test_data["Submitter"] = txt

    def on_change_regulatory_domain(self):
        self.user_test_data["regulatory_domain"] = self.regulatory_domain_combo_box.currentText()

    #############################################
    ############## Test Execution ###############
    #############################################

    def start_test(self):
        ''' 
            Before befor starting, need to make sure certing criterias are met:
                1. Test is not running
                2. All data is collected from the GUI
                3. Do not clear values
                4. Disable GUI 
                5. Pass test cases 
        '''
        my_list = self.change_QList_to_List()
        cnt_profiles_without_restart = len(list(filter(lambda st: st != "Restart_PAL6", my_list)))        
        if self.platforn_combo_box.currentText() != "Other Vendor" :
            self.get_build_version()
        if  len(self.user_test_data["Submitter"]) <= 4 :
            print(f'This is not A valid name: {self.user_test_data["Submitter"]}')
            print("Must submit a name full name")
            return 
        if self.thread.isRunning() :
            print("Test is running")
        elif cnt_profiles_without_restart <= 0 :
            print(f"Must select A test first, profiles count: {cnt_profiles_without_restart}")
        else:
            self.seperate_restart_pal6_from_test(my_list)
            self.get_Submitter()
            self.get_platform()
            self.on_change_regulatory_domain()
            self.thread.start()

    def stop_test(self):
        if self.thread.isRunning():
            self.thread.stop()
            self.user_test_data = {"Restart_PAL6": [], "load_test": False, "plot_chart": False, "tests_seq": [], "build_version": "NA","regulatory_domain" : "US" }
            time.sleep(1)
            import octo
            print(f"Test was stopped, isRunning = {self.thread.isRunning()}")
            self.thread = TestThread(octo,self.user_test_data)
        else:
            print(f"No test is running,  isRunning = {self.thread.isRunning()}")

    def seperate_restart_pal6_from_test(self,profiles_list):
        for i in range(len(profiles_list)):
            if profiles_list[i] ==  "Restart_PAL6":
                self.user_test_data["Restart_PAL6"].append(i)
            else:
                self.user_test_data["tests_seq"].append(profiles_list[i])

    #############################################
    ############# Handel Check Box ##############
    #############################################

    def upload_test(self):
        self.user_test_data["load_test"] = self.load_test_check_box.isChecked()
        print(f'Test ulpoad to data base status is {self.load_test_check_box.isChecked()}')

    def plot_test(self):
        self.user_test_data["plot_chart"] = self.plot_test_check_box.isChecked()

    #############################################
    ############# Handel GUI Data ###############
    #############################################

    def change_QList_to_List(self)->list:
        my_list = list()
        for i in range(self.test_execution_list.count()):
            my_list.append(self.test_execution_list.item(i).text())
        return my_list

    def add_test_names(self)->None:
        test_names = octo.get_test_names()
        self.test_option_list.clear()
        self.test_option_list.addItem("Restart_PAL6")
        self.test_option_list.addItems(test_names)

    def open_csv_config_folder(self):
        import os
        csv_file_path = "nautilus /home/octoscope/Octoscope_New/newEditedOctoApi"
        os.system(csv_file_path)

    def get_build_version(self):
        txt = self.wlan_build_version_line_edit.text()
        if re.match(r"^(\d{1,2}\.){3}\d{1,2}$",txt):
            self.user_test_data["build_version"] = txt
        # TODO - create Error class - raise BadVersionFormatError("Version format is not as expected!")

    def get_Submitter(self):
        submitter = self.submitter_name_combo_box.currentText()
        if submitter == "New":
            self.user_test_data["Submitter"] = self.submitter_name_combo_box.currentText()
        
    def get_platform(self):
        self.user_test_data["Platform"] = self.platforn_combo_box.currentText()

    def set_log_text(self, my_text: str) -> None:
        self.log_text_edit.append(my_text + "\n")

    def add_test_profile(self):
        txt = self.test_option_list.selectedItems()[0].text()
        self.test_execution_list.addItem(txt)

    def delete_item_from_execution_list(self):
        selected_item_index = self.test_execution_list.currentRow()
        if None != selected_item_index != [] :
            self.test_execution_list.takeItem(selected_item_index)
        else:
            print("No item was selected")
    
    def clear_execution_list(self):
        self.test_execution_list.clear()

    def new_submitter_name(self):
        self.user_test_data["Submitter"] = self.new_submitter_line_edit.text()

    #############################################
    ########### Handel GUI Buttons ##############
    #############################################

    def load_from_file(self):
        print('File was open')

    def save_test_to_file(self):
        if len(self.user_test_data["tests_seq"]) > 0:
            print(f'File was saved - This is data: {self.test_execution_list}')


    #############################################
    ############### plot graph ##################
    #############################################

    def append_grapgh(self):
        chart = Canvas(self)

def main():
    app = QApplication(sys.argv)
    # TODO - Should be in separate thread
    window = MainGui()
    window.show()
    app.exec_()

if __name__ == "__main__":
    # os.system(f"pyrcc5 icons.qrc -o icons_rc.py")
    main()


