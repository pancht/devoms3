from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        time.sleep(5)
        driver.find_element_by_link_text("Outbound Loads").click()
        driver.find_element_by_id("48").click()
        driver.find_element_by_xpath("(//span[@id='46'])[2]").click()
        time.sleep(5)
        driver.find_element_by_id("add_update").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='select2-shippings_client_id-container']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='select2-shippings_location_id-container']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='SHIPPINGS_SHIP_TO']/span/span[1]/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='shippings_hawb_']").send_keys("SSkm"+"H2" + Keys.TAB)
        driver.find_element_by_xpath("//*[@id='shippings_ref_1_']").send_keys("SSkm"+"H2")
        driver.find_element_by_xpath("//*[@id='form-render']/section/footer/div/input").click()
        time.sleep(5)
        driver.get_screenshot_as_file("9_CreateOutboundload.png")

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_createOutboload'))