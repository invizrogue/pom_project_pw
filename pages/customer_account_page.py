import allure

from pages.base_page import BasePage

wellcome_message = (By.CLASS_NAME, "logged-in")
success_messages = (
    By.XPATH, "//div[contains(@data-ui-id, 'message-success')]//div[contains(@data-bind, 'message.text')]"
)
success_account_creation_message = "Thank you for registering with Main Website Store."


class CustomerAccountPage(BasePage):
    page_url = "/customer/account/"

    @allure.step("Проверка, что отображается сообщение об успешном создании аккаунта")
    def check_success_message_displayed(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(success_messages))
        assert self.find(success_messages).text == success_account_creation_message

    @allure.step("Проверка, что отображается приветственное сообщение с фамилией и именем")
    def check_wellcome_message_displayed(self, first_name, last_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(wellcome_message))
        assert self.find(wellcome_message).text == f"Welcome, {first_name} {last_name}!"
