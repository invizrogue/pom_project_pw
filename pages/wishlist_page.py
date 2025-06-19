import allure
from playwright.sync_api import expect

from pages.base_page import BasePage

added_to_wishlist_text = "has been added to your Wish List"
product_in_wishlist = "#wishlist-sidebar .product-item"


class WishlistPage(BasePage):
    page_url = "/wishlist/index/index/wishlist_id/"

    @allure.step("Проверка открытия страницы")
    def is_opened(self):
        expect(self.page).to_have_url(containing=f"{self.base_url}{self.page_url}")
        # WebDriverWait(self.driver, 5).until(EC.url_contains(f"{self.base_url}{self.page_url}"))

    @allure.step("Проверка, что отображается сообщение об успешном добавлении товара в избранное")
    def check_product_name_in_success_message(self, data):
        # (WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
        #     (By.XPATH, f"//div[contains(text(), '{data} {added_to_wishlist_text}')]")
        # )))
        expect(self.find(f"//div[contains(text(), '{data} {added_to_wishlist_text}')]")).to_be_visible()
