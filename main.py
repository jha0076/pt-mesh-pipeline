import os
import logging
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_driver():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    service = Service(os.environ.get('CHROMEDRIVER_PATH'))
    driver = webdriver.Chrome(service=service)
    return driver

def search_tenders(driver, search_query):
    tenders = []
    try:
        driver.get('https://etenders.gov.in/eprocure/app')
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "SearchDescription"))
        )
        search_input.send_keys(search_query)
        search_button = driver.find_element_by_name("Go")
        search_button.send_keys(Keys.ENTER)

        for i in range(1, 20):
            sleep(10)
            table = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//table[@id='table']"))
            )
            rows = table.find_elements_by_xpath(".//tr")
            for row in rows:
                cells = row.find_elements_by_xpath(".//td")
                tender = []
                for cell in cells:
                    tender.append(cell.text)
                tenders.append(tender)

            df = pd.DataFrame(tenders)
            df.to_csv('tenders.csv', index=False, header=False)
            driver.find_element_by_id("linkFwd").click()
    except Exception as e:
        logger.error(e)
    finally:
        return tenders

def close_driver(driver):
    driver.close()

if __name__ == "__main__":
    driver = setup_driver()
    tenders = search_tenders(driver, 'all')
    close_driver(driver)
