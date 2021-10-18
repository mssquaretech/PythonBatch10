from selenium import webdriver
import unittest


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class PmoIndia(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        driver = webdriver.Chrome()
        driver.get("https://www.pmindia.gov.in/en/")
        driver.maximize_window()

    def test_PMO(self):
        PmoWebsiteListXpath = "//ul[@class = 'our-gov clearfix']/li/a"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, PmoWebsiteListXpath)))
        PmoWebsiteListElement = driver.find_elements_by_xpath(PmoWebsiteListXpath)


        for PmoSubWebSite in PmoWebsiteListElement:
            PMOLink = PmoSubWebSite.get_attribute("href")
            if PMOLink!="https://www.pmindia.gov.in/en":
               PmoSubWebSite.click()


        windowHandleList = driver.window_handles
        for windowHandle in windowHandleList:
            driver.switch_to.window(windowHandle)
            url = driver.current_url
            print(url)

            if url == "https://loksabha.nic.in/":
                ProfileXpath = driver.find_element_by_xpath("//a[@title =  'Profile']")

                ProfileXpath.click()
                break

        windowHandleListSpeaker = driver.window_handles

        for speakerWindow in windowHandleListSpeaker:
            driver.switch_to.window(speakerWindow)
            if driver.title == "The Office of Speaker Lok Sabha":
                break


        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//img[@alt= 'Former Speaker']")))
        driver.find_element_by_xpath("//img[@alt= 'Former Speaker']").click()



        speakerlistXpath = "//img[@src='images/former_speakers_txt.gif']//..//../following-sibling::tr/descendant::td[@valign='top']/a"
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,speakerlistXpath)))
        speakerlistelement = driver.find_elements_by_xpath(speakerlistXpath)



        for speakerName in speakerlistelement:
            print(speakerName.text)

unittest.main()