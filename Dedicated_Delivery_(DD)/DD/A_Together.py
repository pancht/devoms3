from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
from selenium.webdriver.support.select import Select
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
        time.sleep(2)
        driver.find_element_by_xpath("//div/span/span/span").send_keys(Keys.DOWN)
        time.sleep(2)
        driver.find_element_by_id("DTE_Field_default_in_store_date").send_keys(time.strftime('%m/%d/%y'))
        time.sleep(2)
        driver.find_element_by_xpath("//div[6]/div/div/span/span/span").send_keys(Keys.DOWN)
        time.sleep(2)
        driver.find_element_by_xpath("//div[7]/div/div/span/span/span").send_keys(Keys.DOWN)
        time.sleep(2)
        driver.find_element_by_xpath("//div[8]/div/div/span/span/span").send_keys(Keys.DOWN)
        time.sleep(2)
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
        time.sleep(5)
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
        driver.get_screenshot_as_file("aSync.png")

        ##############################################################################
        # Saltar Pagina

        driver.get("http://dev3.spherewms.com/login")

        driver.find_element_by_id("username").send_keys("yeyej27@gmail.com")
        driver.find_element_by_name("password").send_keys("Jhennifer01")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

        ###################################################################################
        # Truck_Schedule

        Select(driver.find_element_by_id("_force_env_id_")).select_by_visible_text("Target Ruby WMS")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(10)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='137'])[2]").click()
        time.sleep(3)

        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        driver.find_element_by_xpath("//table[@id='datatable-example']/tbody/tr/td[15]/a/i").click()
        time.sleep(3)
        driver.find_element_by_id("arn_headers_hawb_").send_keys(p + "H")
        time.sleep(1)
        driver.find_element_by_name("arn_headers[scheduled_arrive_beg_datetime]").click()
        driver.find_element_by_link_text("Add Lines via PO").click()
        time.sleep(3)
        driver.find_element_by_id("search_text").send_keys(p)
        driver.find_element_by_id("select_all").click()
        driver.find_element_by_xpath("//*[@id='form_element_config_save']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='form-render']/section/footer/div/input").click()
        time.sleep(10)
        driver.get_screenshot_as_file("bTruck.png")

        ######################################################################################3
        # Receiver

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='26'])[2]").click()

        Select(driver.find_element_by_id("Location")).select_by_value("3")
        driver.find_element_by_id("bins.bin").send_keys("staging" + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("WMS Receiver # / HAWB").send_keys(p + "H" + Keys.ENTER)
        driver.find_element_by_id("Inventory Type").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[8]/input").send_keys("1" + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("items.length").send_keys("90" + Keys.ENTER)
        driver.find_element_by_id("items.width").send_keys("90" + Keys.ENTER)
        driver.find_element_by_id("items.height").send_keys("90" + Keys.ENTER)
        driver.find_element_by_id("items.weight").send_keys("90" + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("arn_details.qty_actual").send_keys("200" + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[19]/input").send_keys("G" + Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_id("button148").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='rf-alert']/section/footer/div/div/button").click()
        time.sleep(7)
        driver.get_screenshot_as_file("cReceiver.png")

        ######################################################################################
        # On Hand

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Inventory Views").click()
        driver.find_element_by_xpath("(//a[@href='http://dev3.spherewms.com/inquiry/inqdetail/inventory'])[2]").click()
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        time.sleep(20)
        driver.get_screenshot_as_file("dOnHand.png")

        ########################################################################################
        # Allocate

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        time.sleep(1)
        driver.find_element_by_id("47").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//span[@id='111'])[2]").click()
        time.sleep(3)
        Select(driver.find_element_by_id("Location")).select_by_value("3")
        time.sleep(3)
        driver.find_element_by_id("alloc_masters.targetwms_isd").send_keys("03/02/2018" + Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='button3']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='datatable-example_filter']/label/input").send_keys(p)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='datatable-example']/tbody/tr/td[9]/a/i").click()
        time.sleep(10)
        driver.get_screenshot_as_file("eAllocate.png")

        ######################################################################################
        # Primary_user_picked


        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        driver.find_element_by_link_text("Allocation / Picking").click()
        driver.find_element_by_link_text("Primary User Picked").click()
        time.sleep(10)
        Select(driver.find_element_by_id("Select Location")).select_by_value("3")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[2]/input").send_keys(Keys.CONTROL + 'v' + Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[4]/input").send_keys("staging4" + Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[5]/input").send_keys("1" + Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[6]/input").send_keys("G" + Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[4]/input").send_keys("staging1" + Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[5]/input").send_keys("4" + Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[6]/input").send_keys("G" + Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[3]/input").send_keys("195" + Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[4]/input").send_keys("staging" + Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='rf-alert']/section/footer/div/div/button").click()
        time.sleep(10)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Inventory Views").click()
        driver.find_element_by_xpath("(//a[@href='http://dev3.spherewms.com/inquiry/inqdetail/inventory'])[2]").click()
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        time.sleep(20)
        driver.get_screenshot_as_file("fPrimaryUserPicked.png")

        ############################################################################################
        # Create_MLP

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
        time.sleep(10)
        driver.get_screenshot_as_file("gMLP.png")

        ############################################################################################
        # Assigned license

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element_by_id("43").click()
        driver.find_element_by_xpath("(//span[@id='70'])[2]").click()
        driver.find_element_by_xpath("(//span[@id='33'])[2]").click()
        time.sleep(5)
        Select(driver.find_element_by_id("Select Location")).select_by_value("3")
        driver.find_element_by_id("bins.bin").send_keys("staging" + Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[3]/input").send_keys("MLP-00000105" + Keys.ENTER)
        ##############################################################################suma 2
        driver.find_element_by_xpath("//*[@id='rf']/div/div[4]/input").send_keys(Keys.CONTROL + 'v' + Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='rf-alert']/section/footer/div/div/button").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Inventory Views").click()
        driver.find_element_by_xpath("(//a[@href='http://dev3.spherewms.com/inquiry/inqdetail/inventory'])[2]").click()
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        time.sleep(20)
        driver.get_screenshot_as_file("hAssigened_License.png")

        #############################################################################################
        # View/Create Outbound Load

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
        driver.find_element_by_xpath("//*[@id='shippings_hawb_']").send_keys(p + "H2" + Keys.TAB)
        driver.find_element_by_xpath("//*[@id='shippings_ref_1_']").send_keys(p + "H2")
        driver.find_element_by_xpath("//*[@id='form-render']/section/footer/div/input").click()
        time.sleep(10)
        driver.get_screenshot_as_file("iCreateOutboundload.png")

        ###############################################################################################
        # Scan Load

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        driver.find_element_by_link_text("Outbound Loads").click()
        driver.find_element_by_id("48").click()
        driver.find_element_by_xpath("(//span[@id='49'])[2]").click()
        time.sleep(5)
        driver.find_element_by_id("HAWB").send_keys(p + "H2" + Keys.ENTER)
        driver.find_element_by_id("inventory_bins.bin").send_keys("staging1" + Keys.ENTER)
        driver.find_element_by_id("dummy").send_keys("MLP-00000105" + Keys.ENTER)
        time.sleep(10)
        driver.get_screenshot_as_file("jScanLoad.png")

        ################################################################################################
        # Ship Scanned Inventory

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        driver.find_element_by_link_text("Outbound Loads").click()
        driver.find_element_by_id("48").click()
        driver.find_element_by_xpath("(//span[@id='46'])[2]").click()
        driver.find_element_by_xpath("//*[@id='datatable-example_filter']/label/input").send_keys(p + Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='testbox']/section/footer/div/div/button[1]").click()
        time.sleep(25)
        driver.get_screenshot_as_file("kShipment.png")
        time.sleep(10)

        ###############################################################################################
        # View Open Receiver

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='3'])[2]").click()
        time.sleep(5)
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        time.sleep(20)
        driver.get_screenshot_as_file("lInboundLicensePlates.png")
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='3'])[2]").click()
        time.sleep(5)
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        time.sleep(20)
        driver.get_screenshot_as_file("lPrint_Doc.png")

        ##################################################################################################
        # Identify Items by Receiver

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Receiving").click()
        driver.find_element_by_xpath("(//span[@id='26'])[2]").click()

        Select(driver.find_element_by_id("Location")).select_by_value("4")
        driver.find_element_by_id("bins.bin").send_keys("staging1" + Keys.ENTER)
        driver.find_element_by_id("WMS Receiver # / HAWB").send_keys(p + "H2" + Keys.ENTER)
        Select(driver.find_element_by_id("Inventory Type")).select_by_value("1")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rf']/div/div[8]/input").send_keys("MLP-00000105" + Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='rf-alert']/section/footer/div/div/button").click()

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Inventory Views").click()
        driver.find_element_by_xpath("(//a[@href='http://dev3.spherewms.com/inquiry/inqdetail/inventory'])[2]").click()
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        time.sleep(20)
        driver.get_screenshot_as_file("mReceiverMLP.png")

        ########################################################################################################
        # Create Regional Row/Lot Labels

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element_by_link_text("Inventory Management").click()
        time.sleep(2)
        driver.find_element_by_link_text("Container/License Managment").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//span[@id='141'])[2]").click()
        time.sleep(5)
        Select(driver.find_element_by_id("Select Location")).select_by_value("4")
        time.sleep(3)
        driver.find_element_by_id("order_headers.arrive_by_date").send_keys("03/26/2018" + Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_id("button4").click()
        time.sleep(10)
        driver.find_element_by_link_text("View as PDF").click()
        time.sleep(10)
        driver.get_screenshot_as_file("nRow_Lot.png")
        time.sleep(10)

        ###############################################################################################
        # Mobile Allocate by License Plate

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        driver.find_element_by_id("47").click()
        driver.find_element_by_xpath("(//span[@id='52'])[2]").click()
        time.sleep(5)
        driver.find_element_by_id("containers.license_plate").send_keys(Keys.CONTROL + 'v' + Keys.ENTER)
        time.sleep(10)
        driver.get_screenshot_as_file("oAllocateMobile.png")

        ###############################################################################################
        # Regional Allocation Management

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        time.sleep(2)
        driver.find_element_by_link_text("Manager Menu").click()
        driver.execute_script("window.scrollBy(0," + str(100) + ")")
        time.sleep(2)
        driver.find_element_by_xpath("(//span[@id='148'])[2]").click()
        driver.find_element_by_id("2378").click()
        driver.implicitly_wait(20)
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(Keys.CONTROL + 'v')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='datatable-example']/tbody/tr[1]/td[12]/a[1]/i").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("newSortOrder").clear()
        driver.implicitly_wait(3)
        driver.find_element_by_id("newSortOrder").send_keys("1")
        driver.implicitly_wait(3)
        driver.find_element_by_id("form_change_sort_order").click()
        driver.implicitly_wait(15)
        driver.find_element_by_xpath("//*[@id='datatable-example_filter']/label/input").clear()
        time.sleep(30)
        driver.find_element_by_id("2378").click()
        time.sleep(60)
        driver.find_element_by_id("2378").click()
        time.sleep(10)
        driver.get_screenshot_as_file("pAllocationMaganment.png")

        ###############################################################################################
        # Pick Ready Allocations

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        time.sleep(3)
        driver.find_element_by_id("47").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//span[@id='162'])[2]").click()
        driver.implicitly_wait(35)
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(Keys.CONTROL + 'v')
        time.sleep(200)
        driver.get_screenshot_as_file("qPickReadyAllocations.png")

        ###############################################################################################
        # Regional Pick

        driver.find_element_by_css_selector("div.sidebar-toggle.hidden-xs > i.fa.fa-bars").click()
        driver.find_element_by_id("47").click()
        driver.find_element_by_xpath("(//span[@id='124'])[2]").click()
        time.sleep(5)
        Select(driver.find_element_by_id("Location")).select_by_value("4")
        time.sleep(3)
        driver.find_element_by_id("button8").click()
        time.sleep(15)
        # LP
        driver.find_element_by_xpath("//*[@id='rf']/div/div[6]/input").send_keys(Keys.CONTROL + 'v' + Keys.ENTER)
        time.sleep(20)
        #################################################################Se le suman 8 - RLLP
        driver.find_element_by_xpath("//*[@id='rf']/div/div[2]/input").send_keys("RLLP-00006934" + Keys.ENTER)
        time.sleep(10)
        #################################################################Se le suma 46 - SCC
        driver.find_element_by_xpath("//*[@id='rf']/div/div[5]/input").send_keys("212400000000318588" + Keys.ENTER)
        time.sleep(20)

        driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a").click()
        driver.find_element_by_link_text("Inventory Views").click()
        driver.find_element_by_xpath("(//a[@href='http://dev3.spherewms.com/inquiry/inqdetail/inventory'])[2]").click()
        driver.find_element_by_css_selector("input[type=\"search\"]").send_keys(p)
        time.sleep(20)
        driver.get_screenshot_as_file("rRegionalPick.png")

    ###############################################################################################
    # Create Outbound Load - to store

    ###############################################################################################
    # Scan Inventory to Load - to store

    ###############################################################################################
    # Ship Scanned Inventory - to store

    ###############################################################################################
    # Regional Allocate By LP

    ##############################################################################################

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_Together'))