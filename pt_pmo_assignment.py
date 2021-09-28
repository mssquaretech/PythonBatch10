from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest
import time


class PMO(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.pmindia.gov.in/en/")
        driver.maximize_window()

    def test_PMOSite(self):
        govtsitesXpath = "//ul[contains(@class, 'our-gov clearfix')]//a"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, govtsitesXpath)))
        govtsitesElement = driver.find_elements_by_xpath(govtsitesXpath)

        for govsite in govtsitesElement:
            if '.' in govsite.get_attribute("href") and govsite.get_attribute("href") != 'https://www.pmindia.gov.in/en':
                # print("Site Link: ", govsite.get_attribute("href"))
                govsite.click()

        WindowHandleList = driver.window_handles

        for windowhandle in WindowHandleList:
            driver.switch_to.window(windowhandle)
            # print(driver.title)
            if driver.title == 'Parliament of India, Lok Sabha':
                profileXpath = "//a[@title='Profile']"
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, profileXpath)))
                profileElement = driver.find_element_by_xpath(profileXpath)
                profileElement.click()
                time.sleep(2)

                WindowHandleList = driver.window_handles

                for windowhandle in WindowHandleList:
                    driver.switch_to.window(windowhandle)
                    # print(driver.title)
                    if driver.title == 'The Office of Speaker Lok Sabha':
                        # formerspeakerXpath = "//img[contains(@alt, 'Former Speaker')]"
                        formerspeakerXpath = "//a[contains(@href, 'frmspeaker.asp')]"
                        # formerspeakerXpath = "//a[text()='Former Speaker']"
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, formerspeakerXpath)))
                        formerspeakerElement = driver.find_element_by_xpath(formerspeakerXpath)
                        formerspeakerElement.click()
                        time.sleep(2)

                        speakernameXpath = "//table[@width='96%']//td[@valign='top']//a"
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, speakernameXpath)))
                        speakernameElement = driver.find_elements_by_xpath(speakernameXpath)

                        for speakername in speakernameElement:
                            print("Speaker Name: ", speakername.text)

                        break
            else:
                driver.close()


unittest.main()

