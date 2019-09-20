from configparser import ConfigParser
from selenium import webdriver

def login(driver):
    driver.get(URL)
    driver.close()
    driver.quit()

cfg = ConfigParser()
cfg.read('Config.ini')

DRIVER_PATH = cfg.get('SELENIUM', 'DRIVER_PATH')
URL = cfg.get('SELENIUM', 'URL')

driver = webdriver.Chrome(DRIVER_PATH)
login(driver)
