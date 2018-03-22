from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

from DD import HtmlTestRunner


class P(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev3.spherewms.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_p(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username").send_keys("yeyej27@gmail.com")
        driver.find_element_by_name("password").send_keys("Jhennifer01")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

        Select(driver.find_element_by_id("_force_env_id_")).select_by_visible_text("Target Ruby WMS")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(5)

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element_by_id("43").click()
        driver.find_element_by_xpath("(//span[@id='70'])[2]").click()
        driver.find_element_by_link_text("Create Master LP (MLP) Label").click()
        time.sleep(5)
        Select(driver.find_element_by_id("Select Location")).select_by_value("3")
        driver.find_element_by_xpath("//*[@id='rf']/div/div[2]/input").send_keys("staging" + Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[3]/input").send_keys(Keys.ENTER)
        driver.find_element_by_id("loads.arrive_by_date").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[5]/input").send_keys(Keys.ENTER)
        driver.find_element_by_id("button8").click()
        time.sleep(5)
        driver.find_element_by_link_text("View as PDF").click()
        time.sleep(5)
        driver.get_screenshot_as_file("7_MLP.png")

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_mlp'))