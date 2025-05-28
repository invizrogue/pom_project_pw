import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

added_to_wishlist_text = "has been added to your Wish List"
product_in_wishlist = (By.CSS_SELECTOR, "#wishlist-sidebar .product-item")


class WishlistPage(BasePage):
    page_url = "/wishlist/index/index/wishlist_id/"

    @allure.step("Проверка открытия страницы")
    def is_opened(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains(f"{self.base_url}{self.page_url}"))

    @allure.step("Проверка, что отображается сообщение об успешном добавлении товара в избранное")
    def check_product_name_in_success_message(self, data):
        (WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, f"//div[contains(text(), '{data} {added_to_wishlist_text}')]")
        )))
