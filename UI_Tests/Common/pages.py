from .elements import ElementClickable
from jobs_test_web_viewer.UI_Tests.Common.locators import *
from jobs_test_web_viewer.UI_Tests.Common.common import BasePage, UtilityFunctions
from jobs_test_web_viewer.UI_Tests.Common.elements import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class ProjectsPage(BasePage):

    def __init__(self, driver):
        lambo_scene = ElementClickable(driver, ProjectsPageLocators.LAMBO_SCENE)
        bath_scene = ElementClickable(driver, ProjectsPageLocators.BATH_SCENE)
        kitchen_scene = ElementClickable(driver, ProjectsPageLocators.KITCHEN_SCENE)
        super(ProjectsPage, self).__init__(driver)

    def open_project(self, project):
        project = ElementClickable(self.driver, project)
        project.click()
        try:
            WebDriverWait(self.driver, 500).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="animate-spin loader"]'))
            )
            WebDriverWait(self.driver, 500).until_not(
                EC.presence_of_element_located((By.XPATH, '//*[@class="animate-spin loader"]'))
            )
            time.sleep(40)
        except Exception as e:
            assert False