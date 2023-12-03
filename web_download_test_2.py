import time
from selene.support.shared import browser
from selenium.webdriver import Chrome, ChromeOptions
from script_os import TMP_DIR

prefs = {
    "download.default_directory": TMP_DIR,
    "download.directory_upgrade": True,
    "download.prompt_for_download": False,
}

chromeOptions = ChromeOptions()
chromeOptions.add_experimental_option("prefs", prefs)
driver = Chrome(options=chromeOptions)
browser.config.driver = driver

browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
browser.element('[data-testid="download-raw-button"]').click()
time.sleep(5)