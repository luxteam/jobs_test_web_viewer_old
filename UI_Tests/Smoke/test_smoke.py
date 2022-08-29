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
    
    @allure.title("WUV_PROJECTS_004")
    @allure.description("""Test rendering""")
    def test_final_render_jpeg(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['projects']). \
            open_project(ProjectsPageLocators.BATH_SCENE). \
            open_final_render(). \
            final_render(format="JPEG (Image)"). \
            compare_screenshots("final_jpeg")
    
    @allure.title("WUV_PROJECTS_005")
    @allure.description("""Test rendering""")
    # Doesn't work, the select element is not working
    def test_final_render_png(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['projects']). \
            open_project(ProjectsPageLocators.BATH_SCENE). \
            open_final_render(). \
            final_render(format="PNG (Image)"). \
            compare_screenshots("final_png")
    
    @allure.title("WUV_PROJECTS_006")
    @allure.description("""Test rendering""")
    # Doesn't work, the select element is not working
    def test_final_render_1280_720(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['projects']). \
            open_project(ProjectsPageLocators.BATH_SCENE). \
            open_final_render(). \
            final_render(width="1280", height="720"). \
            compare_screenshots("1280_720_resolution")
    
    @allure.title("WUV_PROJECTS_007")
    @allure.description("""Test rendering""")
    # Doesn't work, the select element is not working
    def test_final_render_800_600(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['projects']). \
            open_project(ProjectsPageLocators.BATH_SCENE). \
            open_final_render(). \
            final_render(width="800", height="600"). \
            compare_screenshots("800_600_resolution")
    