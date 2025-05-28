import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

list_of_products = (By.CSS_SELECTOR, ".item.product.product-item")
limiter_per_page_selector = (By.CSS_SELECTOR, ".products-grid~.toolbar.toolbar-products #limiter")
sorter_selector = (By.CSS_SELECTOR, "div.toolbar.toolbar-products:has(~.products-grid) #sorter")
product_in_wishlist = (By.CSS_SELECTOR, "#wishlist-sidebar .product-item")
item_price = (By.CSS_SELECTOR, ".item.product.product-item .price")


class EcoFriendlyPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    @allure.step("Выбор сортировки по цене")
    def select_sorting_by_price(self):
        selector = Select(self.find(sorter_selector))
        selector.select_by_visible_text("Price")

    @allure.step("Проверка, что товары отсортированы по цене")
    def check_products_sorted_by_price(self):
        item_prices = self.find_all(item_price)
        prices = [price.text for price in item_prices]
        sorted_prices = sorted(prices, key=lambda x: float(x.replace("$", "")))
        assert prices == sorted_prices

    @allure.step("Выбор количества карточек на странице")
    def select_cards_per_page(self, amount):
        selector = Select(self.find(limiter_per_page_selector))
        selector.select_by_visible_text(amount)

    @allure.step("Проверка, что отображаются карточки товаров в соответствии с выбранным количеством")
    def check_amount_cards_less_or_equal_selected(self):
        selector = Select(self.find(limiter_per_page_selector))
        selected_amount = selector.first_selected_option.text
        products_on_page = self.find_all(list_of_products)
        assert len(products_on_page) <= int(selected_amount)

    @allure.step("Добавление товара в избранное")
    def add_product_to_wishlist(self, data):
        wait = WebDriverWait(self.driver, 10)
        product_card = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[alt='{data}']")))
        add_to_wishlist_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, f"a:has([alt='{data}'])~div [title='Add to Wish List']")
        ))
        ActionChains(self.driver).move_to_element(product_card).click(add_to_wishlist_button).perform()
