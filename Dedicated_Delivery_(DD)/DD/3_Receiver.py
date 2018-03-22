from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

from Pages.Logings import *
from Pages.Variable import *
from DD import HtmlTestRunner


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://devoms3.spherewms.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.page_login = Page_Index(self.driver)
        self.Add_Project = Page_Index(self.driver)

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.page_login.login("yeyej27@gmail.com","Jhennifer01")

    ####################################################################################################
    # AddProject

        longitud = 4
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        p = ""
        p = p.join([choice(valores) for i in range(longitud)])

        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_id("DTE_Field_identifier").send_keys(p)
        driver.find_element_by_css_selector("div.DTE_Form_Buttons > button.btn.btn-default").click()

    ####################################################################################################
    # AddVersion

        #fecha2 = date.today() + timedelta(days=10)
        #print(fecha2)

        driver.find_element_by_xpath("(//button[@type='button'])[8]").click()
        time.sleep(2)
        driver.find_element_by_id("DTE_Field_identifier").send_keys(p+"V" + Keys.TAB)
        driver.find_element_by_id("DTE_Field_name").send_keys(p+"V" + Keys.TAB)
        driver.find_element_by_id("DTE_Field_set_date").send_keys()
        time.sleep(5)
        driver.find_element_by_xpath("//div/span/span/span").send_keys(Keys.DOWN)
        time.sleep(2)
        driver.find_element_by_id("DTE_Field_default_in_store_date").send_keys(time.strftime('%m/%d/%y'))
        time.sleep(2)
        driver.find_element_by_xpath("//div[6]/div/div/span/span/span").send_keys(Keys.DOWN + Keys.CONTROL)
        time.sleep(2)
        driver.find_element_by_xpath("//div[7]/div/div/span/span/span").send_keys(Keys.DOWN + Keys.CONTROL)
        time.sleep(2)
        driver.find_element_by_xpath("//div[8]/div/div/span/span/span").send_keys(Keys.DOWN + Keys.CONTROL)
        time.sleep(3)
        driver.find_element_by_css_selector("div.DTE_Form_Buttons > button.btn.btn-default").click()
        time.sleep(10)
        driver.execute_script("window.scrollBy(0," + str(100) + ")")

    #####################################################################################################
    # AddPart

        driver.find_element_by_xpath("/html/body/section/div/section/div[3]/div/section/header/div/button").click()
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(p+"P")
        time.sleep(1)
        driver.find_element_by_id("description").send_keys(p+"P" + Keys.TAB)
        time.sleep(1)
        driver.find_element_by_css_selector("body > div.modal.fade.in > div.modal-dialog > div > div > div.DTE_Body.modal-body > div > form > div > div.DTE_Field.DTE_Field_Type_select2.DTE_Field_Name_supplier_id > div > div.DTE_Field_InputControl > span > span.selection > span").send_keys(Keys.DOWN)
        time.sleep(3)
        driver.find_element_by_id("DTE_Field_po_number").send_keys("5")
        driver.find_element_by_id("DTE_Field_order_date").send_keys(time.strftime('%m/%d/%y'))
        time.sleep(2)
        driver.find_element_by_id("DTE_Field_expected_delivery_date").send_keys(time.strftime('%m/%d/%y'))
        time.sleep(2)
        driver.find_element_by_id("DTE_Field_quantity").send_keys("200" + Keys.TAB)
        driver.find_element_by_css_selector("body > div.modal.fade.in > div.modal-dialog > div > div > div.DTE_Body.modal-body > div > form > div > div.DTE_Field.DTE_Field_Type_select2.DTE_Field_Name_excess_inventory_type_id > div > div.DTE_Field_InputControl > span > span.selection > span").send_keys(Keys.DOWN)
        time.sleep(3)
        driver.find_element_by_css_selector("div.DTE_Form_Buttons > button.btn.btn-default").click()
        driver.execute_script("window.scrollBy(0," + str(100) + ")")
        time.sleep(3)

    ####################################################################################################
    #  Manage Distribution

        driver.find_element_by_link_text("Manage Distribution").click()
        time.sleep(60)
        #driver.find_element_by_id("button-excel-upload").click()
        #with open('C:\Users\open\PycharmProjects\TestCase', 'r') as DD:
            #print(DD.read())
        print(p)
        driver.get_screenshot_as_file("3_Sync.png")

    ####################################################################################################

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

    unittest.main (testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_devoms'))
