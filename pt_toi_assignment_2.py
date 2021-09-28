from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class TimesOfIndia(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://timesofindia.indiatimes.com/")
        driver.maximize_window()
        time.sleep(5)

    def test_iframe(self):
        act1 = ActionChains(driver)
        # scrollXpath = "//a[text()='INDIAN PREMIER LEAGUE 2021']"
        scrollXpath="//div[text()='CRICKET']"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, scrollXpath)))
        elem = driver.find_element_by_xpath(scrollXpath)
        act1.move_to_element(elem)
        elem.click()

        cricketXpath = "//div[@class='_2AG1g']//div[@class='slick-slide']//iframe"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cricketXpath)))
        cricketElementList = driver.find_elements_by_xpath(cricketXpath)

        for cricbio in cricketElementList:
            # iframeXpath = ""
            # iframeElement = cricbio.find_element_by_xpath(iframeXpath)
            time.sleep(2)
            driver.switch_to.frame(cricbio)
            bioPersonXapth = "//div[@class='_2qEfT--Bio--personName']"
            bioPersonElement = driver.find_element_by_xpath(bioPersonXapth)
            print("Bio Person Name is: ", bioPersonElement.text)
            driver.switch_to.default_content()
            print("------------------------------")






unittest.main()