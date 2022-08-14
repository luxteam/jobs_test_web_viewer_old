import pytest
import allure

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from jobs_test_wml.UI_Tests.Common.locators import *
from jobs_test_wml.UI_Tests.Common.pages import LoginPage, ProjectsPage
from jobs_test_wml.UI_Tests.Common.common import BaseSteps

#################################################
#            Steps for a Login page             #
#################################################

class SmokeSteps(BaseSteps):

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def fill_login(self, login, password):
        loginPage = LoginPage(self.driver)
        loginPage.fill_form(login, password)
        return self

    def open_project(self, project):
        projectsPage = ProjectsPage(self.driver)
        projectsPage.openProject(project)

    def render_project(self. project):
        pass
