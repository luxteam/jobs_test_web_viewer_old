from .elements import ElementClickable, ElementSelect, ElementTextField
from jobs_test_web_viewer.UI_Tests.Common.locators import MainPageLocators, ProjectsPageLocators, FinalRenderPageLocators
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
                EC.presence_of_element_located((By.XPATH, '//*[@class="animate-spin"]'))
            )
            WebDriverWait(self.driver, 500).until_not(
                EC.presence_of_element_located((By.XPATH, '//*[@class="animate-spin"]'))
            )
            time.sleep(40)
        except Exception as e:
            assert False

class MainPage(BasePage):

    def __init__(self, driver):
        self.final_render_button = ElementClickable(driver, MainPageLocators.FINAL_RENDER)
        super(MainPage, self).__init__(driver)

    def open_final_render(self):
        self.final_render_button.click()

class FinalRenderPage(BasePage):

    def __init__(self, driver):
        self.output = ElementClickable(driver, FinalRenderPageLocators.OUTPUT)
        self.output.click()
        self.format = ElementSelect(driver, FinalRenderPageLocators.FORMAT)
        self.begin_render = ElementClickable(driver, FinalRenderPageLocators.BEGIN_RENDER)
        self.width = ElementTextField(driver, FinalRenderPageLocators.WIDTH)
        self.height = ElementTextField(driver, FinalRenderPageLocators.HEIGHT)
        super(FinalRenderPage, self).__init__(driver)

    def final_render(self, format="JPEG (Image)", width="1920", height="1080"):
        self.format.select(format)
        self.width.set(width)
        self.height.set(height)
        self.begin_render.click()
        time.sleep(20)