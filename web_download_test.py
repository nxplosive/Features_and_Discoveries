import time

from selenium import webdriver
from selene import query
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from script_os import TMP_DIR

chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    },
)

driver = webdriver.Chrome(
    service=ChromeService(executable_path=ChromeDriverManager().install()),
    options=chrome_options,
)
browser.config.driver = driver

browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
browser.element('[data-testid="download-raw-button"]').click()
time.sleep(5)
