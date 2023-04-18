from base_page import *
from urllib.parse import urlparse
from locators import *


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c' \
              '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid& '

        driver.get(url)

        self.input = driver.find_element(*Locators.AUTH_INPUT)
        self.password = driver.find_element(*Locators.AUTH_PASS)
        self.auth_btn = driver.find_element(*Locators.BTN_AUTH)
        self.forgot = driver.find_element(*Locators.FORGOTE_PASS)
        self.register = driver.find_element(*Locators.REGISTER)
        self.agree = driver.find_element(*Locators.DOC_AGREEMENT)
        self.private = driver.find_element(*Locators.DOC_PRIVATE_POLICE)
        self.vk_btn = driver.find_element(*Locators.AUTH_VK)
        self.ok_btn = driver.find_element(*Locators.AUTH_OK)
        self.mail_btn = driver.find_element(*Locators.AUTH_MAIL)
        self.google_btn = driver.find_element(*Locators.AUTH_GOOGlE)
        self.ya_btn = driver.find_element(*Locators.AUTH_YA)
        self.email = driver.find_element(*Locators.AUTH_EMAIL)
        self.login = driver.find_element(*Locators.AUTH_LOGIN)
        self.person_acc = driver.find_element(*Locators.AUTH_PERSON_ACCOUNT)
        self.phone = driver.find_element(*Locators.AUTH_PHONE)
        self.password_recovery = driver.find_element(*Locators.FORGOTE_PASS)

    def btn_click(self):
        self.auth_btn.click()

    def reg_click(self):
        self.register.click()

    def find_element(self, by, location):
        return self.driver.find_element(by, location)

    def get_current_url(self):
        return self.driver.current_url

    def scroll_down(self, offset=0):

        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


class CodePage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://my.rt.ru/'

        driver.get(url)

        self.get_code = driver.find_element(*Locators.BTN_GET_CODE)
        self.standart_auth = driver.find_element(*Locators.BTN_STANDART_AUTH)
        self.address = driver.find_element(*Locators.REG_ADDRESS)

    def get_click(self):
        self.get_code.click()

    def find_element(self, by, location):
        return self.driver.find_element(by, location)

    def get_current_url(self):
        url = urlparse(self.driver.current_url)
        return url.path


class RegPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

        self.name = driver.find_element(*Locators.REG_NAME)
        self.lastname = driver.find_element(*Locators.REG_LASTNAME)
        self.region = driver.find_element(*Locators.REG_REGION)
        self.address = driver.find_element(*Locators.REG_ADDRESS)
        self.new_pass = driver.find_element(*Locators.REG_PASS)
        self.confirm = driver.find_element(*Locators.REG_PASS_CONFIRM)
        self.reg = driver.find_element(*Locators.BTN_REG)

    def get_click(self):
        self.reg.click()

    def find_element(self, by, location):
        return self.driver.find_element(by, location)

    def get_current_url(self):
        return self.driver.current_url


class RecPass(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

        self.telephone = driver.find_element(*Locators.REC_TELEPHONE)
        self.mail = driver.find_element(*Locators.REC_MAIL)
        self.login = driver.find_element(*Locators.REC_LOGIN)
        self.ls = driver.find_element(*Locators.REC_LS)
        self.input = driver.find_element(*Locators.REC_INPUT)
        self.resume = driver.find_element(*Locators.BTN_RESUM)


    def get_click(self):
        self.resume.click()

    def find_element(self, by, location):
        return self.driver.find_element(by, location)

    def get_current_url(self):
        return self.driver.current_url