import pytest
import allure

from jobs_test_web_viewer.UI_Tests.Common.common import UITestClass, init_urls
from jobs_test_web_viewer.UI_Tests.Smoke.smoke_steps import SmokeSteps
from jobs_test_web_viewer.conftest import conf
from jobs_test_web_viewer.UI_Tests.Common.locators import ProjectsPageLocators

@allure.sub_suite("Smoke")
@allure.suite("Smoke")
@allure.parent_suite("UI tests")
@pytest.mark.usefixtures("init_urls")
class TestSmoke(UITestClass):
    
    @allure.title("WUV_PROJECTS_001")
    @allure.description("""Test opening project""")
    def test_opening_project_kitchen(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['projects']). \
            open_project(ProjectsPageLocators.KITCHEN_SCENE). \
            compare_screenshots("kitchen")
    
    @allure.title("WUV_PROJECTS_002")
    @allure.description("""Test opening project""")
    def test_opening_project_lambo(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['projects']). \
            open_project(ProjectsPageLocators.LAMBO_SCENE). \
            compare_screenshots("lambo")
    
    @allure.title("WUV_PROJECTS_003")
    @allure.description("""Test opening project""")
    def test_opening_project_bath(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['projects']). \
            open_project(ProjectsPageLocators.BATH_SCENE). \
            compare_screenshots("bath")