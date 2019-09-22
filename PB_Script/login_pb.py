from configparser import ConfigParser


def login(driver):
    cfg = ConfigParser()
    cfg.read('Config\PB.ini')

    login_id_name = cfg.get('LOGIN', 'LOGIN_ID_NAME')
    login_pw_name = cfg.get('LOGIN', 'LOGIN_PW_NAME')
    login_btn_name = cfg.get('LOGIN', 'LOGIN_BTN_NAME')

    login_url = cfg.get('LOGIN', 'LOGIN_URL')
    login_id = cfg.get('LOGIN', 'LOGIN_ID')
    login_pw = cfg.get('LOGIN', 'LOGIN_PW')

    driver.get(login_url)

    driver.find_element_by_name(login_id_name).send_keys(login_id)
    driver.find_element_by_name(login_pw_name).send_keys(login_pw)
    driver.find_element_by_name(login_btn_name).click()
