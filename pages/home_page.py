import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

hot_sellers_title = (By.XPATH, "//h2[text()='Hot Sellers']")


class HomePage(BasePage):
    page_url = ""

    @allure.step("Проверка наличия блока Hot Sellers на странице")
    def check_hot_sellers_block_exist(self):
        self.find(hot_sellers_title).is_displayed()
