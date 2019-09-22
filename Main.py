from configparser import ConfigParser
from selenium import webdriver
from PB_Script import login_pb


cfg = ConfigParser()
cfg.read('Config\Config.ini')
DRIVER_PATH = cfg.get('SELENIUM', 'DRIVER_PATH')
URL = cfg.get('SELENIUM', 'URL')

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(DRIVER_PATH, options=options)

if __name__ == "__main__":
    login_pb.login(driver)
    driver.close()
    driver.quit()
