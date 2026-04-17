from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.create_order_page_locators import CreateOrderPageLocators
from config import Config
from data.order_data import OrderData


class CreateOrderPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)

    def fill_personal_data_form(self, name, surname, address, metro, phone):
        self.input_text(CreateOrderPageLocators.name_input, name)
        self.input_text(CreateOrderPageLocators.surname_input, surname)
        self.input_text(CreateOrderPageLocators.address_input, address)
        self.click_element(CreateOrderPageLocators.metro_dropdown_menu)
        metro_locator = CreateOrderPageLocators.metro_locator(metro)
        self.click_element(metro_locator)
        self.input_text(CreateOrderPageLocators.phone_input, phone)

    def fill_rental_data_form(self, rental_date, rental_period, scooter_color, comment):
        self.click_element(CreateOrderPageLocators.datepicker_input)
        rental_date_locator = CreateOrderPageLocators.rental_date_locator(rental_date)
        self.click_element(rental_date_locator)
        self.click_element(CreateOrderPageLocators.rental_period_input)
        rental_period_locator = CreateOrderPageLocators.rental_period_locator(rental_period)
        self.click_element(rental_period_locator)
        scooter_color_locator = CreateOrderPageLocators.scooter_color_locator(scooter_color)
        self.click_element(scooter_color_locator)
        self.input_text(CreateOrderPageLocators.comment_input, comment)

    def click_order_button(self, locator):
        self.click_button(locator)

    def click_next_button(self):
        self.click_button(CreateOrderPageLocators.next_button)

    def click_order_button_after_filling_form(self):
        self.click_button(CreateOrderPageLocators.order_button_in_form)

    def click_confirm_order_button(self):
        self.click_button(CreateOrderPageLocators.confirm_order_button)

    def click_check_status_button(self):
        self.click_button(CreateOrderPageLocators.check_status_button)

    def click_logo_yandex(self):
        self.click_element(HomePageLocators.header_logo_yandex)

    def click_logo_scooter(self):
        self.click_element(HomePageLocators.header_logo_scooter)

    def check_success_order_modal(self):
        assert OrderData.TEXT_SUCCESS_ORDER_MODAL in self.get_element_text(CreateOrderPageLocators.success_order_modal)

    def check_current_url_main_scooter(self):
        self.check_current_url(Config.BASE_URL)

    def check_current_url_dzen_in_new_window(self):
        self.check_url_page_in_new_window(HomePageLocators.header_logo_yandex, Config.DZEN_URL)