from selenium.webdriver.common.by import By


class CreateOrderPageLocators:
    name_input = (By.XPATH, '//input[@placeholder="* Имя"]')
    surname_input = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_input = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro_dropdown_menu = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    phone_input = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()="Далее"]')
    datepicker_input = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    rental_period_input = (By.XPATH, '//div[text()="* Срок аренды"]/following-sibling::div//span[@class="Dropdown-arrow"]')
    comment_input = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    order_button_in_form = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    confirm_order_button = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]')
    success_order_modal = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    check_status_button = (By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()="Посмотреть статус"]')

    @staticmethod
    def metro_locator(metro):
        return (By.XPATH, f'//*[text() = "{metro}"]')

    @staticmethod
    def rental_date_locator(rental_date):
        return (By.XPATH, f'//div[contains(@class, "react-datepicker__day")][text() = "{rental_date}"]')

    @staticmethod
    def rental_period_locator(rental_period):
        return (By.XPATH, f'//div[@class="Dropdown-option"][text()="{rental_period}"]')

    @staticmethod
    def scooter_color_locator(scooter_color):
        return (By.XPATH, f'//label/input[@id="{scooter_color}"]')