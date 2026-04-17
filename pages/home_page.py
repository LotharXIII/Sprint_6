from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)

    def click_accordion_button(self, header_number):
        locator = (
            HomePageLocators.questions_accordion_button[0], f"(//div[@class='accordion__button'])[{header_number}]")
        self.click_button(locator)

    def get_accordion_panel_text(self, header_number):
        locator = (
            HomePageLocators.questions_accordion_panel_text[0],
            f"(//div[@class='accordion__panel']/p)[{header_number}]")
        return self.get_element_text(locator)

    def check_accordion_panel_text(self, header_number, expected_answer):
        assert self.get_accordion_panel_text(header_number) == expected_answer