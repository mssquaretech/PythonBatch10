from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MoneyControl(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.moneycontrol.com/")
        driver.maximize_window()

    def test_PrintNetProfit (self):

        act1 = ActionChains(driver)
        scrollXpath = "//a[text()='Recommended Podcasts']"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, scrollXpath)))
        elem = driver.find_element_by_xpath(scrollXpath)
        act1.move_to_element(elem)

        category_element = driver.find_element_by_xpath("//select[@id='screen_crit']")
        sel1 = Select(category_element)
        sel1.select_by_value("net-profit")

        industry_element = driver.find_element_by_xpath("//select[@id='sel_code']")
        sel1 = Select(industry_element)
        sel1.select_by_value("airlines")

        search_btn_elemment = driver.find_element_by_xpath("//input[@class='btn_go' and @value='GO']")
        search_btn_elemment.click()

        CompanyNameXpath="//th[contains(text(), 'Company Name')]/parent::tr/following-sibling::tr/descendant::b"
        CompanyNameElement = driver.find_element_by_xpath(CompanyNameXpath)
        print(CompanyNameElement.text)


unittest.main()