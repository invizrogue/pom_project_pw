import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

women_deals_link = (By.XPATH, "//span[text()='Women’s Deals']")
cart_button = (By.CSS_SELECTOR, ".action.showcart")
empty_cart_message = (By.CSS_SELECTOR, ".subtitle.empty")
home_page_link = (By.CSS_SELECTOR, "a[title='Go to Home Page']")


class SalePage(BasePage):
    page_url = "/sale.html"

    @allure.step("Клик по ссылке 'Women’s Deals'")
    def click_women_deals(self):
        self.find(women_deals_link).click()

    @allure.step("Клик по кнопке 'Cart'")
    def click_cart_button(self):
        self.find(cart_button).click()

    @allure.step("Проверка отображения сообщения о пустой корзине")
    def check_empty_cart_message_exist(self):
        empty_message = self.find(empty_cart_message)
        assert empty_message.text == "You have no items in your shopping cart."

    @allure.step("Клик по ссылке 'Home'")
    def click_home_page_link(self):
        self.find(home_page_link).click()
