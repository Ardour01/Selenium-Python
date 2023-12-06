import pytest
from tests.test_base import TestBase
from utilities.read_properties import read_yaml


class TestInputFormsPage(TestBase):

    def test_all_forms(self):
        """
        This test case reads the test data from yaml file
        :return:
        """
        self.input_forms_obj.click_input_forms_btn()
        assert (read_yaml('Input Forms') == self.input_forms_obj.input_forms_all_elements())

    @pytest.mark.parametrize("test_string, test_total",
                             [("Test Message", "8"),
                              pytest.param("test Message", "8", marks=pytest.mark.xfail),
                              pytest.param("Test Message", "9", marks=pytest.mark.xfail),
                              pytest.param("Test message", "18", marks=pytest.mark.xfail)
                              ])
    def test_simple_form_demo(self, test_string, test_total):
        """
        This test case reads test data from parameterization and is failing expectedly
        :param test_string:
        :param test_total:
        :return:
        """
        assert (test_string == self.simple_form_obj.single_input_field())
        assert (test_total == self.simple_form_obj.two_input_fields())

    def test_checkbox_demo(self):
        assert (read_yaml('CHECKBOX_SUCCESS_MESSAGE') == self.checkbox_demo_obj.checkbox_demo())
        assert ("true" == self.checkbox_demo_obj.multiple_checkbox_demo())

    @pytest.mark.parametrize("radio_button_option",
                             ["Male", "Female"
                              ])
    def test_radio_button_demo(self, radio_button_option):
        self.radio_button_obj.radio_button_demo()
        assert (read_yaml('RADIO_BUTTON_SUCCESS_MESSAGE').replace("'Male'", "'" + radio_button_option + "'") ==
                self.radio_button_obj.select_radio_button_value(radio_button_option))

    @pytest.mark.parametrize("radio_button_option1, radio_button_option2",
                             [("Male", "0 - 5"),
                              ("Female", "0 - 5"),
                              ("Male", "5 - 15"),
                              ("Female", "5 - 15"),
                              ("Male", "15 - 50"),
                              ("Female", "15 - 50"),
                              ])
    def test_group_radio_button_demo(self, radio_button_option1, radio_button_option2):
        self.radio_button_obj.radio_button_demo()
        assert ("Sex : " + radio_button_option1 + "\n" + "Age group: " + radio_button_option2 ==
                self.radio_button_obj.group_radio_button_demo(radio_button_option1, radio_button_option2))
