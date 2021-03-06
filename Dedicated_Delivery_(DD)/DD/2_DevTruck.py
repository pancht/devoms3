from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
#from Automatization.A_Devoms3 import *
from DD import HtmlTestRunner


class Dev3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev3.spherewms.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_dev3(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username").send_keys("yeyej27@gmail.com")
        driver.find_element_by_name("password").send_keys("Jhennifer01")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

        ###################################################################################
        #Truck_Schedule

        """longitud = 4
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        p = ""
        p = p.join([choice(valores) for i in range(longitud)])"""

        Select(driver.find_element_by_id("_force_env_id_")).select_by_visible_text("Target Ruby WMS")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(10)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='137'])[2]").click()
        time.sleep(3)

        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys("1vrS")
        driver.find_element_by_xpath("//table[@id='datatable-example']/tbody/tr/td[15]/a/i").click()
        time.sleep(3)
        driver.find_element_by_id("arn_headers_hawb_").send_keys("1vrS"+"H")
        time.sleep(1)
        driver.find_element_by_name("arn_headers[scheduled_arrive_beg_datetime]").click()
        driver.find_element_by_link_text("Add Lines via PO").click()
        time.sleep(3)
        driver.find_element_by_id("search_text").send_keys("1vrS")
        driver.find_element_by_id("select_all").click()
        driver.find_element_by_xpath("//*[@id='form_element_config_save']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='form-render']/section/footer/div/input").click()
        time.sleep(10)
        driver.get_screenshot_as_file("2_Truck.png")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_truck'))