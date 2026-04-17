import allure
import pytest

from selenium import webdriver

from pages.create_order_page import CreateOrderPage
from locators.home_page_locators import HomePageLocators
from data.order_data import OrderData

@pytest.mark.usefixtures("driver_setup")
class TestCreateOrderPage:
    def setup_method(self):
        self.create_order_page = CreateOrderPage(self.driver)
        self.create_order_page.open_page()
        self.create_order_page.click_cookie_button()

    @allure.title(f'Проверка оформления заказа')
    @pytest.mark.parametrize('order_button, personal_data, rental_data', [
        (
                HomePageLocators.header_order_button,
                [
                    OrderData.NAME_1, OrderData.SURNAME_1, OrderData.ADDRESS_1, OrderData.METRO_1, OrderData.PHONE_1
                ],
                [
                    OrderData.DATE_1, OrderData.RENTAL_PERIOD_1, OrderData.SCOOTER_COLOR_1, OrderData.COMMENT_1
                ]
        ),
        (
                HomePageLocators.roadmap_order_button,
                [
                    OrderData.NAME_2, OrderData.SURNAME_2, OrderData.ADDRESS_2, OrderData.METRO_2, OrderData.PHONE_2
                ],
                [
                    OrderData.DATE_2, OrderData.RENTAL_PERIOD_2, OrderData.SCOOTER_COLOR_2, OrderData.COMMENT_2
                ]
        )
    ])
    def test_create_order(self, order_button, personal_data, rental_data):
        with allure.step(f'Кликаем по кнопке "Заказать"'):
            self.create_order_page.click_order_button(order_button)
        with allure.step(f'Заполняем форму "Для кого самокат"'):
            self.create_order_page.fill_personal_data_form(*personal_data)
        with allure.step(f'Кликаем по кнопке "Далее"'):
            self.create_order_page.click_next_button()
        with allure.step(f'Заполняем форму "Про аренду"'):
            self.create_order_page.fill_rental_data_form(*rental_data)
        with allure.step(f'Кликаем по кнопке "Заказать" внизу формы'):
            self.create_order_page.click_order_button_after_filling_form()
        with allure.step(f'Кликаем по кнопке "Да" в окне подтверждения заказа'):
            self.create_order_page.click_confirm_order_button()
        with allure.step(f'Проверяем отображение окна "Заказ оформлен"'):
            self.create_order_page.check_success_order_modal()
        with allure.step(f'Кликаем по кнопке "Посмотреть статус"'):
            self.create_order_page.click_check_status_button()
        with allure.step(f'Кликаем на логотип "Самоката" в правом верхнем углу страницы'):
            self.create_order_page.click_logo_scooter()
        with allure.step(f'Проверяем переход на главную страницу'):
            self.create_order_page.check_current_url_main_scooter()
        with allure.step(
                f'Кликаем на логотип "Самоката" в правом верхнем углу страницы и проверяем открытие главной страницы Дзена в новой вкладке'):
            self.create_order_page.check_current_url_dzen_in_new_window()