from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.base_page_locators import BasePageLocators
from config import Config


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url=None):
        full_url = Config.BASE_URL + url if url else Config.BASE_URL
        self.driver.get(full_url)

    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def check_current_url(self, url):
        assert self.driver.current_url == url

    def check_url_page_in_new_window(self, locator, url):
        original_window = self.driver.current_window_handle
        self.driver.find_element(*locator).click()
        self.wait.until(ec.number_of_windows_to_be(2))
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
        assert self.wait.until(
            ec.url_to_be(url)), f'Текущий url: {self.driver.current_url} не совпадает с ожидаемым'
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def click_cookie_button(self):
        wait = WebDriverWait(self.driver, 10)
        elements = self.driver.find_elements(*BasePageLocators.cookie_button)
        if elements:
            try:
                wait.until(ec.element_to_be_clickable(BasePageLocators.cookie_button)).click()
            except:
                pass