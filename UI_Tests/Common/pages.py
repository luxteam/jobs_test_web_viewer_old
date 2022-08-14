from UI_Tests.Common.locators import ProjectsPageLocators
from jobs_test_wml.UI_Tests.Common.locators import *
from jobs_test_wml.UI_Tests.Common.common import BasePage, UtilityFunctions
from jobs_test_wml.UI_Tests.Common.elements import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class ProjectsPage(BasePage):

    def __init__(self, driver):
        super(ProjectsPage, self).__init__(driver)

    def open_project(self, project):
        ProjectsPageLocators.PROJECT_LOCATOR + '[{project}]'