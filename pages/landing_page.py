from base.basepage import BasePage
import allure


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Landing Page Locators
    top_navigation_bar = "//div[@id='navbar-brand-centered']"
    start_practising_btn = "//*[@id='btn_basic_example']"
    tab_two = "//span[@class='round-tabs two']/i"

    @allure.step("Verify if top navigation bar is displayed")
    def is_displayed_top_navigation_bar(self):
        """
        Verify the top navigation bar is displayed or not
        """
        return self.is_element_displayed(self.top_navigation_bar)

    @allure.step("Fetch the title of the page")
    def page_title(self):
        """
        Verify the top navigation bar is displayed or not
        """
        return self.driver.title

    @allure.step("Click on start practicing button")
    def click_start_practising_btn(self):
        self.scroll_down()
        self.click_element(self.start_practising_btn)
        return self.get_hidden_element_attribute(locator_value=self.tab_two, attribute_name='class')


