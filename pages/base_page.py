import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открытие страницы")
    def open(self):
        if self.page_url:
            self.driver.get(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this page class")

    @allure.step("Проверка открытия страницы")
    def is_opened(self):
        WebDriverWait(self.driver, 5).until(EC.url_matches(f"{self.base_url}{self.page_url}"))

    def find(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))
