import allure
from playwright.sync_api import expect

from pages.base_page import BasePage

welcome_message = ".panel.header .logged-in"
success_messages = "//div[contains(@data-ui-id, 'message-success')]//div"
success_account_creation_message = "Thank you for registering with Main Website Store."


class CustomerAccountPage(BasePage):
    page_url = "/customer/account/"

    @allure.step("Проверка, что отображается сообщение об успешном создании аккаунта")
    def check_success_message_displayed(self):
        # self.find(success_messages).is_visible()
        expect(self.find(success_messages)).to_have_text(success_account_creation_message)
        # assert self.find(success_messages).inner_text() == success_account_creation_message

    @allure.step("Проверка, что отображается приветственное сообщение с фамилией и именем")
    def check_wellcome_message_displayed(self, first_name, last_name):
        # self.find(welcome_message).is_visible()
        expect(self.find(welcome_message)).to_have_text(f"Welcome, {first_name} {last_name}!")
        # assert self.find(wellcome_message).inner_text() == f"Welcome, {first_name} {last_name}!"
