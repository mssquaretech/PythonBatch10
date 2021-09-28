from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import unittest
import time


class ShareKhan(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://support.sharekhan.com/faq")
        driver.maximize_window()

    def test_Categories_login(self):
        categoryXpath = "//ul[@class='left-menu']//a"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, categoryXpath)))
        categoryElement = driver.find_elements_by_xpath(categoryXpath)

        for category in categoryElement:
            print("Category: ", category.text)

        act = ActionChains(driver)
        livechatXpath = "//span[contains(text(), 'Live Chat')]"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, livechatXpath)))
        act.move_to_element(livechatXpath)
        livechatElement = driver.find_element_by_xpath(livechatXpath)
        livechatElement.click()
        time.sleep(2)
        custserviceXpath = "//input[@id='radioEquityCust']"
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, custserviceXpath)))
        custservicElement = driver.find_element_by_xpath(custserviceXpath)
        custservicElement.click()

        chatnowXpath = "//input[@value='Chat Now']"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, chatnowXpath)))
        chatnowElement = driver.find_element_by_xpath(chatnowXpath)
        chatnowElement.click()

        time.sleep(2)
        closebtnXpath = "//span[@role='button']"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, chatnowXpath)))
        closebtnElement = driver.find_element_by_xpath(closebtnXpath)
        closebtnElement.click()
        time.sleep(2)
        closebtnElement = driver.find_element_by_xpath(closebtnXpath)
        closebtnElement.click()


unittest.main()

