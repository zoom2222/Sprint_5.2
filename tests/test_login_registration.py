from time import sleep

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

#Регистрация (успешная)
class TestLoginRegistration:
    def test_register_new_user(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        #переходим на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        #переходим по кнопке "Войти в аккаунт"
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        sleep(3)

        #переходим по кнопке "Зарегистрироваться"
        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()
        sleep(3)

        #вводим данные для регистрации
        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = DataHelper.generate_password()

        register_name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_input))
        register_email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        register_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))

        register_name_input.send_keys(name_data)
        register_email_input.send_keys(email_data)
        register_password_input.send_keys(password_data)

        register_button = wait.until(EC.element_to_be_clickable(registration_locators.register_button))
        register_button.click()
        sleep(3)

        #после регистрации мы попадаем на вход и проверяем введенные данные
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        #Переход в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        #Проверяем данные пользователя
        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute("value") == name_data
        assert account_login_input.get_attribute("value") == email_data
        sleep(3)


#Регистрация с некорректным паролем
    def test_register_with_invalid_password(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # переходим на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        # переходим по кнопке "Войти в аккаунт"
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        sleep(3)

        # переходим по кнопке "Зарегистрироваться"
        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()
        sleep(3)

        # вводим данные для регистрации с некорректным паролем (менее 6 символов)
        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        invalid_password = "12345"  # Пароль меньше 6 символов

        register_name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_input))
        register_email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        register_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))

        register_name_input.send_keys(name_data)
        register_email_input.send_keys(email_data)
        register_password_input.send_keys(invalid_password)

        register_button = wait.until(EC.element_to_be_clickable(registration_locators.register_button))
        register_button.click()
        sleep(3)

        # Проверяем, что появилось сообщение об ошибке
        error_message = wait.until(EC.visibility_of_element_located(registration_locators.password_error))
        assert error_message.text == "Некорректный пароль"

        # Проверяем, что мы остались на странице регистрации
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"
        sleep(3)


#Вход по кнопке «Войти в аккаунт» на главной странице:
    def test_login_home_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        #переходим на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        #переходим на страницу логина
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)
        sleep(3)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        #Переход в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # Проверяем данные пользователя
        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute("value") == user_data.name
        assert account_login_input.get_attribute("value") == user_data.email
        sleep(3)


#Вход через кнопку «Личный кабинет»
    def test_login_via_personal_account_button(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # переходим на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        # кликаем по кнопке "Личный кабинет"
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # проверяем, что перешли на страницу входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        # вводим данные для входа
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        # проверяем, что авторизовались и перешли на главную страницу
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


#Вход через кнопку в форме регистрации
    def test_login_via_registration_form_button(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # переходим на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        # переходим по кнопке "Личный кабинет"
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # переходим по кнопке "Зарегистрироваться"
        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()
        sleep(3)

        # кликаем по кнопке "Войти" в форме регистрации
        login_link = wait.until(EC.element_to_be_clickable(registration_locators.login_link))
        login_link.click()
        sleep(3)

        # проверяем, что перешли на страницу входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        # вводим данные для входа
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        # Переход в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # Проверяем данные пользователя
        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute("value") == user_data.name
        assert account_login_input.get_attribute("value") == user_data.email
        sleep(3)


#Вход через кнопку в форме восстановления пароля.
    def test_login_via_password_recovery_form_button(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # переходим на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        # переходим по кнопке "Личный кабинет"
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # переходим по кнопке "Восстановить пароль"
        recovery_link = wait.until(EC.element_to_be_clickable(login_locators.recovery_link))
        recovery_link.click()
        sleep(3)

        # кликаем по кнопке "Войти" в форме восстановления пароля
        login_link = wait.until(EC.element_to_be_clickable(login_locators.login_link))
        login_link.click()
        sleep(3)

        # проверяем, что перешли на страницу входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        # вводим данные для входа
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        # Переход в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # Проверяем данные пользователя
        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute("value") == user_data.name
        assert account_login_input.get_attribute("value") == user_data.email
        sleep(3)

#Выход из аккаунта
    def test_logout_from_account(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # 1. Авторизуемся
        driver.get("https://stellarburgers.nomoreparties.site/")
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        # Заполняем форму входа
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        # 2. Переходим в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # 3. Выходим из аккаунта
        logout_button = wait.until(EC.element_to_be_clickable(account_locators.logout_button))
        logout_button.click()
        sleep(3)

        # 4. Проверяем, что выход выполнен успешно
        # Проверяем URL страницы входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        # Проверяем, что отображается форма входа
        assert wait.until(EC.visibility_of_element_located(login_locators.login_input)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(login_locators.password_input)).is_displayed()

        # 5. Дополнительная проверка - попытка перейти в личный кабинет без авторизации
        driver.get("https://stellarburgers.nomoreparties.site/")
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # Проверяем, что остались на странице входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"



