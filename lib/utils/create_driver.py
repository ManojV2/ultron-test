import pytest
from selenium.webdriver import Chrome, firefox, Ie

def get_driver_instance():
    browser = pytest.config.option.browser.lower()
    url = pytest.config.option.server.lower()

    if browser == 'firefox':
        driver = firefox("./browser-servers/geckodriver.exe")
    elif browser == 'chrome':
        driver = Chrome("./browser-servers/chromedriver.exe")
    elif browser == 'ie':
        driver = Ie("./browser-servers/IEDriverServer.exe")
    else:
        print('---------------------Error----------------------')
        print('!!!!-----------Invalid Broser Option---------!!!!')
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url == 'prod':
        driver.get('https://demo.actitime.com/')
    else:
        driver.get('http://localhost')
    return driver