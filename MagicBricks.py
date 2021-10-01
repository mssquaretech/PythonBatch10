from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class MagicBricks(unittest.TestCase):
    def setUp(self):
        global driver
        opt = webdriver.ChromeOptions()
        opt.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=opt)
        # driver = webdriver.Chrome()
        driver.get("https://www.magicbricks.com/")
        driver.maximize_window()

    def test_SelectProperty(self):
        ClearSearchXpath = "//div[@class='mb-search__tag-close']"
        ClearSearchElement = driver.find_element_by_xpath(ClearSearchXpath)
        ClearSearchElement.click()
        time.sleep(1)

        SearchPropertyXpath = "//input[@id='keyword']"
        SearchPropertyElement = driver.find_element_by_xpath(SearchPropertyXpath)
        SearchPropertyElement.send_keys("Magarpatta City, Pune")
        time.sleep(1)

        PropertyElement= driver.find_element_by_xpath("//div[@id='serachSuggest']/div[contains(@onclick,'Magarpatta City')]")
        PropertyElement.click()

        PropertySearchXpath = "//div[@class='mb-search__btn']"
        PropertySearchElement = driver.find_element_by_xpath(PropertySearchXpath)
        PropertySearchElement.click()
        time.sleep(3)

        NewPropertyXpath = "//a[@id='projectTab']"
        NewPropertyElement = driver.find_element_by_xpath(NewPropertyXpath)
        NewPropertyElement.click()
        time.sleep(1)

        ResultPropertyElement = driver.find_elements_by_xpath("//div[contains(@id,'resultBlockWrapper')]")
        # ResultPropertyElement.click()

        for ResultProperty in ResultPropertyElement:
            ResultProperty.click()

        driver.switch_to.window(driver.window_handles[1])

        act = ActionChains(driver)
        ScrollPageElement = driver.find_element_by_xpath("//div[@class='heading' and text() ='About Cosmos']")
        act.move_to_element(ScrollPageElement).perform()

unittest.main()

