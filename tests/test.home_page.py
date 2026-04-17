import allure
import pytest

from selenium import webdriver

from pages.home_page import HomePage
from data.home_page_data import HomePageData

@pytest.mark.usefixtures("driver_setup")
class TestHomePage:
    questions_list = list(HomePageData.questions.items())

    def setup_method(self):
        self.home_page = HomePage(self.driver)
        self.home_page.open_page()
        self.home_page.click_cookie_button()

    @allure.title(f'Проверка текста ответа в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('question, expected_answer', questions_list)
    def test_text_by_clicking_on_the_arrow_in_important_questions_section(self, question, expected_answer):
        header_number = self.questions_list.index((question, expected_answer)) + 1
        with allure.step(f'Кликаем по стрелочку с вопросом "{question}"'):
            self.home_page.click_accordion_button(header_number)
        with allure.step(f'Проверяем текст ответа'):
            self.home_page.check_accordion_panel_text(header_number, expected_answer)