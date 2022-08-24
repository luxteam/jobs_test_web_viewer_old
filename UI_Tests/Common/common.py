from attr import s
import pytest
import allure
import yaml
import allure
import time
import os
import random
import string

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from jobs_test_web_viewer.conftest import conf

@pytest.fixture(scope='class')
def init_urls(request):
    request.cls.urls = conf['UI']

class UtilityFunctions:
    
    def find_web_element(driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(
                lambda driver: driver.find_element_by_xpath(locator))

    def find_web_elements(driver, locator, timeout=10):
        WebDriverWait(driver, timeout).until(
                lambda driver: driver.find_element_by_xpath(locator))
        return driver.find_elements_by_xpath(locator)

    def list_multiple_elements(driver, locator, timeout=10):
        elements = list()
        for i in range(1, len(UtilityFunctions.find_web_elements(driver, locator)) + 1):
            WebDriverWait(driver, timeout).until(
                lambda driver: driver.find_element_by_xpath(locator + '[' + str(i) + ']'))
            elements.append(BasePageElement(driver, locator + '[' + str(i) + ']'))
        return elements

class UITestClass:
    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @pytest.fixture(autouse=True)
    def init_driver(self):
        if (conf["browser"] == "Chrome"):
            options = webdriver.ChromeOptions()
            for flag in conf['chromeArguments']:
                options.add_argument(flag)
            prefs = conf['chromeSettings']
            options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome('..\drivers\chromedriver.exe', options=options)
        elif (conf["browser"] == "Firefox"):
            driver = webdriver.Firefox()
        yield
        allure.attach(self.driver.get_screenshot_as_png(), name=self.id_generator(), attachment_type=AttachmentType.PNG)
        self.driver.close()
class BaseSteps:

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def open_url(self, url):
        self.driver.get(url)
        return self

    @allure.step
    def check_url(self, url):
        assert self.driver.current_url == url
        return self

    @allure.step
    def wait_for_download(self, pathToDownloads, timeout):
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < timeout:
            time.sleep(1)
            dl_wait = False
            for fname in os.listdir(pathToDownloads):
                if fname.endswith('.crdownload'):
                    dl_wait = True
            seconds += 1
    
    def refresh_page(self):
        self.driver.refresh()
        return self
        

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def check_element_exists(self, locator):
        try: 
            WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(locator))
        except TimeoutException:
            return False
        return True

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver, locator, timeout=10):
        self.driver = driver
        self.locator = locator
        self.element = WebDriverWait(driver, timeout).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
