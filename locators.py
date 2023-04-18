from selenium.webdriver.common.by import By


class Locators:
    # локаторы формы авторизации
    AUTH_PHONE = (By.ID, 't-btn-tab-phone')
    AUTH_EMAIL = (By.ID, "t-btn-tab-mail")
    AUTH_LOGIN = (By.ID, 't-btn-tab-login')
    AUTH_PERSON_ACCOUNT = (By.ID, 't-btn-tab-ls')
    AUTH_INPUT = (By.ID, 'username')
    AUTH_PASS = (By.ID, "password")

    # локаторы соц сетей
    ALL_SOCIAL = (By.CSS_SELECTOR, '.social-providers__provider')
    AUTH_VK = (By.ID, 'oidc_vk')
    AUTH_OK = (By.ID, 'oidc_ok')
    AUTH_MAIL = (By.ID, 'oidc_mail')
    AUTH_GOOGlE = (By.ID, 'oidc_google')
    AUTH_YA = (By.ID, 'oidc_ya')

    # локаторы ссылок
    DOC_AGREEMENT = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    DOC_PRIVATE_POLICE = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    REGISTER = (By.ID, 'kc-register')
    FORGOTE_PASS = (By.ID, 'forgot_password')

    # локаторы кнопок
    BTN_AUTH = (By.ID, 'kc-login')
    BTN_REG = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    BTN_GET_CODE = (By.ID, 'otp_get_code')
    BTN_STANDART_AUTH = (By.ID, 'standard_auth_btn')
    BTN_INTER = (By.XPATH, '/html/body/section/div/div[2]/a[1]')
    BTN_RESUM = (By.ID, 'reset')

    # локаторы формы регистрации
    REG_NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    REG_LASTNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    REG_REGION = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]')
    REG_ADDRESS = (By.ID, 'address')
    REG_PASS = (By.XPATH, '//*[@id="password"]')
    REG_PASS_CONFIRM = (By.ID, 'password-confirm')

    # локаторы формы восстановление пароля
    REC_TELEPHONE = (By.XPATH, '// *[ @ id = "t-btn-tab-phone"]')
    REC_MAIL = (By.XPATH, '//*[@id="t-btn-tab-mail"]')
    REC_LOGIN = (By.XPATH, '//*[@id="t-btn-tab-login"]')
    REC_LS = (By.XPATH, '//*[@id="t-btn-tab-ls"]')
    REC_INPUT = (By.XPATH, '//*[@id="username"]')
