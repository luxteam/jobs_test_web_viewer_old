class ProjectsPageLocators(object):
    PROJECTS = '(//div[@class="project-card w-full"])' # add [X] to find project by position
    LAMBO_SCENE = '//div[text()="Lambo"]'
    KITCHEN_SCENE = '//div[text()="Kitchen_set"]'
    BATH_SCENE = '//div[text()="BathHouse"]'
    UPLOAD_FILE = '(//div[@class="button-content-center vertical"])[1]'
    BROWSE_CLOUD = '(//div[@class="button-content-center vertical"])[2]'
    
class MainPageLocators(object):
    FINAL_RENDER = ' //*[local-name() = "path" and @d="M4,4H7L9,2H15L17,4H20A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4A2,2 0 0,1 2,18V6A2,2 0 0,1 4,4M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9Z"]'

class FinalRenderPageLocators(object):
    OUTPUT = '//*[text()="Output"]'
    FORMAT = '(//input[@class="containered-input select-text cursor-pointer"])[1]'
    BEGIN_RENDER = '//div[text()[contains(., "Begin Render")]]'
    WIDTH = '(//*[@maxlength])[1]'
    HEIGHT = '(//*[@maxlength])[1]'