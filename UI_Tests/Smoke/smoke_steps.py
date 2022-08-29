import pytest
import allure

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from PIL import Image, ImageChops
import os
from jobs_test_web_viewer.UI_Tests.Common.locators import *
from jobs_test_web_viewer.UI_Tests.Common.pages import ProjectsPage, MainPage, FinalRenderPage
from jobs_test_web_viewer.UI_Tests.Common.common import BaseSteps

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

    @allure.step
    def open_project(self, project):
        projectsPage = ProjectsPage(self.driver)
        projectsPage.open_project(project)
        return self

    @allure.step
    def compare_screenshots(self, screenshot_name):
        outputdir = os.path.join('..', 'Work')
        actual_result_path = os.path.join(outputdir, screenshot_name + '.png')
        expected_result_path = os.path.join('..', 'Baselines', screenshot_name + '.png')
        os.makedirs(outputdir , exist_ok=True)
        os.makedirs(os.path.join('..', 'Baselines') , exist_ok=True)
        self.driver.save_screenshot(f"../Work/{screenshot_name}.png")
        actual_screenshot = Image.open(actual_result_path)
        expected_screenshot = Image.open(expected_result_path)
        image_diff = ImageChops.difference(actual_screenshot, expected_screenshot).convert('RGB')
        if image_diff.getbbox():
            diff_results = os.path.join(outputdir, screenshot_name + "-diff.png")
            print("Images are different, difference saved in " + diff_results)
            os.makedirs(outputdir , exist_ok=True)
            image_diff.save(diff_results)
            assert False
        else:
            print("Images are equal")
            assert True
        return self

    @allure.step
    def open_final_render(self):
        mainPage = MainPage(self.driver)
        mainPage.open_final_render()
        return self

    @allure.step
    def final_render(self, format="JPEG (Image)", width="1920", height="1080"):
        finalRenderPage = FinalRenderPage(self.driver)
        finalRenderPage.final_render(format=format, width=width, height=height)
        return self