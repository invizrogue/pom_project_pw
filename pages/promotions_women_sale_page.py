import allure

from pages.base_page import BasePage

page_name = (By.TAG_NAME, "h1")


class PromotionsWomenSalePage(BasePage):
    page_url = "/promotions/women-sale.html"

    @allure.step("Проверка названия страницы")
    def check_page_name(self):
        self.find(page_name)
        assert self.find(page_name).text == "Women Sale"
