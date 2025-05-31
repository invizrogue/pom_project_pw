import allure

from pages.base_page import BasePage

firstname_field = (By.ID, "firstname")
firstname_error = (By.ID, "firstname-error")
lastname_field = (By.ID, "lastname")
lastname_error = (By.ID, "lastname-error")
email_address_field = (By.ID, "email_address")
email_address_error = (By.ID, "email_address-error")
password_field = (By.ID, "password")
password_error = (By.ID, "password-error")
password_confirm_field = (By.ID, "password-confirmation")
password_confirm_error = (By.ID, "password-confirmation-error")
create_button = (By.CSS_SELECTOR, "button[title='Create an Account']")
wellcome_message = (By.CLASS_NAME, "logged-in")
empty_error_text = "This is a required field."
not_match_error_text = "Please enter the same value again."


class CustomerAccountCreatePage(BasePage):
    page_url = "/customer/account/create/"

    @allure.step("Заполнение поля Name")
    def fill_firstname(self, data):
        self.find(firstname_field).is_displayed()
        self.find(firstname_field).send_keys(data)

    @allure.step("Заполнение поля Lastname")
    def fill_lastname(self, data):
        self.find(lastname_field).is_displayed()
        self.find(lastname_field).send_keys(data)

    @allure.step("Заполнение поля Email")
    def fill_email(self, data):
        self.find(email_address_field).is_displayed()
        self.find(email_address_field).send_keys(data)

    @allure.step("Заполнение поля Password")
    def fill_password(self, data):
        self.find(password_field).is_displayed()
        self.find(password_field).send_keys(data)

    @allure.step("Заполнение поля Password Confirm")
    def fill_password_confirm(self, data):
        self.find(password_confirm_field).is_displayed()
        self.find(password_confirm_field).send_keys(data)

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Name")
    def check_empty_firstname_error_exist(self):
        self.find(firstname_error).is_displayed()
        assert self.find(firstname_error).text == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Lastame")
    def check_empty_lastname_error_exist(self):
        self.find(lastname_error).is_displayed()
        assert self.find(lastname_error).text == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Email")
    def check_empty_email_error_exist(self):
        self.find(email_address_error).is_displayed()
        assert self.find(email_address_error).text == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Password")
    def check_empty_password_error_exist(self):
        self.find(password_error).is_displayed()
        assert self.find(password_error).text == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Password Confirm")
    def check_empty_password_confirm_error_exist(self):
        self.find(password_confirm_error).is_displayed()
        assert self.find(password_confirm_error).text == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке несовпадения паролей")
    def check_not_match_password_confirm_error_exist(self):
        self.find(password_confirm_error).is_displayed()
        assert self.find(password_confirm_error).text == not_match_error_text

    @allure.step("Нажатие кнопки Create an Account")
    def click_create_button(self):
        self.find(create_button).is_displayed()
        self.find(create_button).click()

    @allure.step("Заполнение формы создания аккаунта")
    def fill_form(self, firstname, lastname, email, password="Test@123456!"):
        self.fill_firstname(firstname)
        self.fill_lastname(lastname)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_password_confirm(password)
