import pytest
import allure

from jobs_test_web_viewer.UI_Tests.Common.common import UITestClass
from jobs_test_web_viewer.UI_Tests.Smoke.smoke_steps import SmokeSteps
from jobs_test_web_viewer.conftest import conf

@allure.sub_suite("Login")
@allure.suite("Smoke")
@allure.parent_suite("UI tests")
class TestSmoke(UITestClass):
    
    @allure.title("Test login")
    @allure.description("""Test login on correct data""")
    @pytest.mark.skip(reason="Needs update of its wait function")
    def test_login_successful_on_correct_creds(self):
        steps = SmokeSteps(self.driver)
        steps.open_url(self.urls['root'] + self.urls['login']). \
            fill_login(conf['adminCreds']['login'], conf['adminCreds']['password']). \
            wait_for_main_to_load(). \
            check_url(self.urls['root'] + self.urls['main'])