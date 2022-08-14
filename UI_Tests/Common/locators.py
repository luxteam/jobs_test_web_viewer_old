from selenium.webdriver.common.by import By

class ProjectsPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    ALL_MATERIALS_BUTTON = '//span[text()=" Materials "]'
    ALL_COLLECTIONS_BUTTON = '//span[text()=" Collections "]'
    MATERIALS = '(//div[@class="absolute z-1 top-0 col d-flex flex-column fill-height justify-center align-center"])'
    FIRST_MATERIAL_ICON = '(//div[contains(@class, "vue-recycle-scroller__item-view")]/div/div)[1]'
    PROJECT_LOCATOR = '(//div[@class="project-card w-full"])'
    