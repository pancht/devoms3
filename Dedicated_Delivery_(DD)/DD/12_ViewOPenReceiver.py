from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

from DD import HtmlTestRunner


class B(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev3.spherewms.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_b(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username").send_keys("yeyej27@gmail.com")
        driver.find_element_by_name("password").send_keys("Jhennifer01")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

        Select(driver.find_element_by_id("_force_env_id_")).select_by_visible_text("Target Ruby WMS")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(5)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='3'])[2]").click()
        time.sleep(5)
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys("3CKH")
        time.sleep(20)
        driver.get_screenshot_as_file("lInboundLicensePlates.png")
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='3'])[2]").click()
        time.sleep(5)
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys("3CKH")
        time.sleep(20)
        driver.get_screenshot_as_file("12_Print_Doc.png")

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_OpenReceiver'))