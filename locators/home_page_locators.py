from selenium.webdriver.common.by import By


class HomePageLocators:
    header_order_button = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]')
    header_logo_yandex = (By.XPATH, '//img[@alt="Yandex"]')
    header_logo_scooter = (By.XPATH, '//img[@alt="Scooter"]')
    roadmap_order_button = (By.XPATH, '//div[@class="Home_RoadMap__2tal_"]//button[text()="Заказать"]')
    questions_accordion_button = (By.XPATH, '(//div[@class="accordion__button"])[{}]')
    questions_accordion_panel_text = (By.XPATH, '(//div[@class="accordion__panel"]/p)[{}]')