from jobs_test_wml.UI_Tests.Common.common import BasePageElement
from jobs_test_wml.UI_Tests.Common.locators import MainPageLocators, MaterialViewWindowLocators
from jobs_test_wml.UI_Tests.Common.common import BasePageElement, UtilityFunctions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By

class ElementTextField(BasePageElement):
    def set(self, value):
        self.value = value
        self.element.send_keys(value)

class ElementClickable(BasePageElement):
    def click(self, timeout=10):
        self.element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, self.locator))
            )
        self.element.click()