from tests.test_base import TestBase
import utilities.custom_logger as cl


class TestLandingPage(TestBase):

    def test_page_title(self):
        assert self.landing_obj.page_title() == "Selenium Easy - Best Demo website to practice Selenium Webdriver Online"

    def test_landing_page(self):
        assert self.landing_obj.is_displayed_top_navigation_bar() == True

    def test_start_practising(self):
        assert "down" in self.landing_obj.click_start_practising_btn()
