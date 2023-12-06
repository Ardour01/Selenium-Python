from selenium import webdriver
import pytest
import time
from webdriver_manager.chrome import ChromeDriverManager
from utilities.read_properties import read_properties as rp


@pytest.fixture(scope='function', autouse=True)
def before_method(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    base_url = rp("BASE_URL")
    driver.get(base_url)
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(2)
    driver.quit()  # request contains all information of the requesting test function


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser name")

#
#
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Selenium Easy Demo'
#     config._metadata['Module Name'] = 'UI'
#     config._metadata['Test Type'] = 'Automation'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
