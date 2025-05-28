import pytest
from selenium import webdriver
from faker import Faker
from pages.home_page import HomePage
from pages.sale_page import SalePage
from pages.wishlist_page import WishlistPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.customer_account_page import CustomerAccountPage
from pages.promotions_women_sale_page import PromotionsWomenSalePage
from pages.customer_account_create_page import CustomerAccountCreatePage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def women_sale_page(driver):
    return PromotionsWomenSalePage(driver)


@pytest.fixture()
def account_create_page(driver):
    return CustomerAccountCreatePage(driver)


@pytest.fixture()
def wishlist_page(driver):
    return WishlistPage(driver)


@pytest.fixture()
def account_page(driver):
    return CustomerAccountPage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def authorize_new_user(account_create_page, account_page, person):
    account_name = person["firstname"]
    account_lastname = person["lastname"]
    account_email = person["email"]
    account_create_page.open()
    account_create_page.fill_form(account_name, account_lastname, account_email)
    account_create_page.click_create_button()
    account_page.is_opened()


@pytest.fixture()
def person():
    faker = Faker()
    return {
        'firstname': faker.first_name(),
        'lastname': faker.last_name(),
        'email': faker.email(),
        'password': faker.password()
    }
