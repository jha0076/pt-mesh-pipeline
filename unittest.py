import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
import pandas as pd

class TestScrapingCode(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.s = Service('C:/Users/HI/Downloads/chromedriver_win32 (2)/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get('https://etenders.gov.in/eprocure/app')
        
    def test_search_tenders(self):
        self.driver.find_element_by_name("SearchDescription").send_keys('all')
        self.driver.find_element_by_name("Go").send_keys(Keys.ENTER)
        tenders=[]
        for i in range(1,2):
            table = self.driver.find_element_by_xpath("//table[@id='table']")
            rows = table.find_elements_by_xpath(".//tr")
            for row in rows:
                cells = row.find_elements_by_xpath(".//td")
                tender=[]
                for cell in cells:
                    tender.append(cell.text)
                tenders.append(tender)
            df=pd.DataFrame(tenders)
            self.assertIsNotNone(df)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
