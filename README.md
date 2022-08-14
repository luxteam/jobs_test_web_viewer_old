# Autotests for WML project

### Prerequisites
1. Install Allure command line tool (https://docs.qameta.io/allure/#_installing_a_commandline)
2. Install Python
3. Install Chrome browser and webdriver for your downloaded version (https://sites.google.com/a/chromium.org/chromedriver/downloads)

### How to use
1. Customize a configuration file in "Utils/ConfigurationFiles" to your liking or create a new one. These parameters are used in autotests. Configuration file name should end with "Config.yaml"
2. To run autotests use "run.bat" script from "scripts" folder. It takes 3 arguments:  
2.1. Tests type. Values: API/UI/LOAD/ALL  
2.2. Tests selector. Relative to a selected tests type folder. Use ALL to select every test of selected type. If ALL tests type was selected, skip tests selector.  
2.3. Config selection. Only specify the required prefix. For instance, if you want to run testingConfig.yaml, send 'testing'  
Usage examples:  
.\run.bat API Tags testing  
.\run.bat UI Materials production  
.\run.bat ALL testing  
.\run.bat UI ALL dev  
.\run.bat API Tags/test_api_tags.py::TestAPITags::test_get_all_tags dev  

To run all tests of the selected test type just use '.' symbol:
.\run.bat API . testing  
.\run.bat UI . testing  

3. View results with a 'view_results.bat' script. Then view them through your browser, following instructions from the script.
