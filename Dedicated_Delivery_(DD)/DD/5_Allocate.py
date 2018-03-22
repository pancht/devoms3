from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

from DD import HtmlTestRunner


class Allocate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev3.spherewms.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_allocate(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username").send_keys("yeyej27@gmail.com")
        driver.find_element_by_name("password").send_keys("Jhennifer01")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

        Select(driver.find_element_by_id("_force_env_id_")).select_by_visible_text("Target Ruby WMS")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(5)

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        time.sleep(1)
        driver.find_element_by_id("47").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//span[@id='111'])[2]").click()
        time.sleep(3)
        Select(driver.find_element_by_id("Location")).select_by_value("3")
        time.sleep(3)
        driver.find_element_by_id("alloc_masters.targetwms_isd").send_keys("04/02/2018" + Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='button3']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='datatable-example_filter']/label/input").send_keys("SSkm")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='datatable-example']/tbody/tr/td[9]/a/i").click()
        time.sleep(10)
        driver.get_screenshot_as_file("5_Allocate.png")

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_allocate'))