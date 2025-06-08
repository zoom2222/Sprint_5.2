from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from helpers.data_helpers import DataHelper
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocators
)


home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators
account_locators = AccountPageLocators()


#Переход из личного кабинета в конструктор (переход по клику на «Конструктор» и на логотип Stellar Burgers)
class TestNavigation:
    def test_from_account_to_constructor(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # 1. Логинимся
        driver.get("https://stellarburgers.nomoreparties.site/")
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        # 2. Переходим в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        # Ждем перехода в личный кабинет
        wait.until(EC.url_contains("/account/profile"))

        # 3. Проверяем переход по кнопке в "Конструктор"
        constructor_link = wait.until(EC.element_to_be_clickable(home_locators.constructor_link))
        constructor_link.click()

        # Ждем перехода на главную страницу
        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        # Проверяем что перешли на главную страницу
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        # 4. Снова переходим в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        # Ждем перехода в личный кабинет
        wait.until(EC.url_contains("/account/profile"))

        # 5. Проверяем переход по клику на логотип
        logo = wait.until(EC.element_to_be_clickable(home_locators.logo))
        logo.click()

        # Ждем перехода на главную страницу
        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        # Проверяем что перешли на главную страницу
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

# Тест проверки перехода к разделу "Соусы"
def test_sauces_section_navigation(self, create_driver):
    driver = create_driver
    wait = WebDriverWait(driver, timeout=10)

    # 1. Переходим на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait.until(EC.presence_of_element_located(home_locators.fillings_section))

    # 2. Проверяем переход к разделу "Соусы"
    sauces_section = wait.until(EC.element_to_be_clickable(home_locators.sauces_section))
    driver.execute_script("arguments[0].scrollIntoView();", sauces_section)
    sauces_section.click()

    # Ждем активации раздела и появления элементов
    wait.until(EC.text_to_be_present_in_element_attribute(
        home_locators.sauces_section, "class", "tab_tab_type_current__2BEPc"))
    sauces_items = wait.until(EC.visibility_of_element_located(home_locators.sauces_items))
    assert sauces_items.is_displayed()

# Тест проверки перехода к разделу "Начинки"
def test_fillings_section_navigation(self, create_driver):
    driver = create_driver
    wait = WebDriverWait(driver, timeout=10)

    # 1. Переходим на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait.until(EC.presence_of_element_located(home_locators.fillings_section))

    # 2. Проверяем переход к разделу "Начинки"
    fillings_section = wait.until(EC.element_to_be_clickable(home_locators.fillings_section))
    driver.execute_script("arguments[0].scrollIntoView();", fillings_section)
    fillings_section.click()

    # Ждем активации раздела и появления элементов
    wait.until(EC.text_to_be_present_in_element_attribute(
        home_locators.fillings_section, "class", "tab_tab_type_current__2BEPc"))
    fillings_items = wait.until(EC.visibility_of_element_located(home_locators.fillings_items))
    assert fillings_items.is_displayed()

# Тест проверки перехода к разделу "Булки"
def test_buns_section_navigation(self, create_driver):
    driver = create_driver
    wait = WebDriverWait(driver, timeout=10)

    # 1. Переходим на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait.until(EC.presence_of_element_located(home_locators.fillings_section))

    # 2. Проверяем переход к разделу "Булки"
    buns_section = wait.until(EC.element_to_be_clickable(home_locators.buns_section))
    driver.execute_script("arguments[0].scrollIntoView();", buns_section)
    buns_section.click()

    # Ждем активации раздела и появления элементов
    wait.until(EC.text_to_be_present_in_element_attribute(
        home_locators.buns_section, "class", "tab_tab_type_current__2BEPc"))
    buns_items = wait.until(EC.visibility_of_element_located(home_locators.buns_items))
    assert buns_items.is_displayed()