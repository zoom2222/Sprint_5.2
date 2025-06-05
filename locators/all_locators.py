from selenium.webdriver.common.by import By


class HomePageLocators:
    login_account_button = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    account_link = (By.XPATH, "//a[@href = '/account']")
    constructor_link = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    # Секции конструктора
    buns_section = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]")
    sauces_section = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]")
    fillings_section = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]")

    # Элементы секций
    buns_items = (By.XPATH,
                  "//div[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//h2[text()='Булки']/following-sibling::ul")
    sauces_items = (By.XPATH,
                    "//div[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//h2[text()='Соусы']/following-sibling::ul")
    fillings_items = (By.XPATH,
                      "//div[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//h2[text()='Начинки']/following-sibling::ul")

class LoginPageLocators:
    login_label = (By.XPATH, "//h2[text() = 'Вход']")
    login_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    login_button = (By.XPATH, "//button[text()= 'Войти']")
    registration_link = (By.XPATH, "//a[@href='/register']")
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']")
    recovery_link = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    login_link = (By.XPATH, "//a[contains(text(), 'Войти')]")

class RegistrationPageLocators:
    name_input = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    email_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    register_button = (By.XPATH, "//button[text()= 'Зарегистрироваться']")
    password_error = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    login_button = (By.XPATH, "//button[text()= 'Войти']")
    login_link = (By.XPATH, "//a[contains(text(), 'Войти')]")

class AccountPageLocators:
    name_input = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    login_input = (By.XPATH, "//label[text() = 'Логин']/following-sibling::input")
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    logout_button = (By.XPATH, "//button[text()= 'Выход']")
