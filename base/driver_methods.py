import os
import utilities.read_properties as cp


class Driver:
    bs_user_name = str(os.environ.get('BS_USER_NAME'))
    bs_access_key = str(os.environ.get('BS_ACCESS_KEY'))
    bs_grid_url = "@hub-cloud.browserstack.com/wd/hub"

    def get_driver_method(self, driver):
        """
        method to return driver
        """
        # desired_caps = {}
        # desired_caps['URL'] = cp.read_properties('BASE_URL')
        # driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        driver.get(cp.read_properties('BASE_URL'))
        return driver
