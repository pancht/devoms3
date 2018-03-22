from selenium.webdriver.common.keys import Keys

class Page_Index:
    def __init__(self,myDriver):
        self.driver = myDriver

    def login(self,username,password):
        self.driver.find_element_by_id('username').send_keys(username+Keys.TAB+password+Keys.TAB+Keys.ENTER)