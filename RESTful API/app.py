from flask import Flask
import os


# from the Flask class we initialize the constructor, we us to call @app. for flask
app = Flask(__name__)


#  This path is for the home site
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/index')
def index():
    return 'This is index site, need HTML and CSS badly'





#  run in terminal:
#  export Flask_APP=app.py
if __name__ == "__main__":
    app.run(port=int(os.getenv('PORT', 2022)), debug=True)























# from selenium import webdriver
#
# try:
#     driver = webdriver.Chrome(executable_path='/home/octoscope/Octoscope_New/new edited octo api/RESTful API/chromedriver.exe')
#     driver.get('http://localhost:5000/testbed-components#x')
#     my_return = driver.find_element_by_id('systemResetTooltip_169.254.27.1').click()
# except Exception as e:
#     print(e)
# finally:
#     driver.close()

# driver = webdriver.Chrome('/home/user/drivers/chromedriver')
# driver = webdriver.Chrome(ChromeDriverManager().install())

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome(chrome_options=options)
#
#
# python_button = driver.find_element_by_class_name("fas fa-power-off fa-lg text-primary").click()


#
# b = webdriver.Chrome(executable_path=r'C:\Program Files\chromewebdriver\chromedriver.exe')
# b.maximize_window()
#
#
# class EventListeners(AbstractEventListener):
#     def before_navigate_to(self, url, driver):
#         print("before_navigate_to %s" % url)
#
#     def after_navigate_to(self, url, driver):
#         print("after_navigate_to %s" % url)
#
#     def before_click(self, element, driver):
#         print("before_click %s" % element)
#
#     def after_click(self, element, driver):
#         print("after_click %s" %element)
#
#     def after_navigate_forward(self, driver):
#         print("after_navigate_forward");
#
#     def before_navigate_forward(self, driver):
#         print("before_navigate_forward")
#
#     def after_navigate_back(self, driver):
#         print("after_navigate_back")
#
#     def before_navigate_back(self, driver):
#         print("before_navigate_back")
#
#     def before_change_value_of(self, element, driver):
#         print("before_change_value_of")
#
#
# d = EventFiringWebDriver(b,EventListeners())
