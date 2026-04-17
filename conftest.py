import pytest
import allure
from selenium import webdriver
from config import Config

@pytest.fixture(scope="class")
def driver_setup(request):
    driver = webdriver.Firefox()
    driver.get(Config.BASE_URL)
    request.cls.driver = driver
    yield driver
    driver.quit()