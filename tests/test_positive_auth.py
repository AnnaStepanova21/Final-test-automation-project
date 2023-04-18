import pytest
from auth_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# набор тестов для авторизации через соцсети
def test_auth_with_social_01(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.vk_btn.click()
    assert ros_tel.get_base_url() == 'oauth.vk.com'


def test_auth_with_social_02(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.ok_btn.click()
    assert ros_tel.get_base_url() == 'connect.ok.ru'


def test_auth_with_social_03(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.mail_btn.click()
    assert ros_tel.get_base_url() == 'connect.mail.ru'


def test_auth_with_social_04(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.google_btn.click()
    assert ros_tel.get_base_url() == 'accounts.google.com'


def test_auth_with_social_05(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.ya_btn.click()
    assert ros_tel.get_base_url() == 'oauth.yandex.ru'
    # 'passport.yandex.ru'


# проверка ссылки Пользовательское соглашение
def test_link_agreement(start_page):
    ros_tel = AuthPage(start_page)
    original_window = ros_tel.driver.current_window_handle
    ros_tel.agree.click()
    WebDriverWait(ros_tel.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in ros_tel.driver.window_handles:
        if window_handle != original_window:
            ros_tel.driver.switch_to.window(window_handle)
            break
    win_title = ros_tel.driver.execute_script("return window.document.title")

    assert win_title == 'User agreement'


# проверка авторизации по номеру телефона

def test_auth_with_valid_phone(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys('+79040213269')
    ros_tel.password.send_keys('Cntgfyjdf2.')
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.CLASS_NAME, 'card-title').text == 'Учетные данные'


# проверка авторизации по почте

def test_auth_with_valid_mail(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys('anna.stepanova69@yandex.ru')
    ros_tel.password.send_keys('Cntgfyjdf2.')
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.CLASS_NAME, 'card-title').text == 'Учетные данные'


# проверка авторизации по логину

def test_auth_with_login(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys('Анна')
    ros_tel.password.send_keys('Cntgfyjdf2.')
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'

    # тест входа по ЛС пропущен, так как ЛС нет


def test_auth_with_person_acc(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.person_acc.click()
    ros_tel.input.send_keys('879040213269')
    ros_tel.password.send_keys('Cntgfyjdf2.')
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'


# проверка входа по временному коду до момента ввода кода

def test_auth_with_sms(start_page):
    ros_tel = CodePage(start_page)
    ros_tel.address.send_keys('+79040213269')
    ros_tel.get_code.click()

    assert ros_tel.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация по коду'


# проверка входа по ссылке на почту до момента ввода

def test_auth_with_mail(start_page):
    ros_tel = CodePage(start_page)
    ros_tel.address.send_keys('anna.stepanova69@yandex.ru')
    ros_tel.get_code.click()

    assert ros_tel.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация по коду'


# проверка восстановление пароля по номеру

def test_password_recovery(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.password_recovery.click()
    rec_pass = RecPass(start_page, ros_tel.get_current_url())
    rec_pass.telephone.click()
    rec_pass.input.send_keys('+79040213269')

    assert ros_tel.find_element(By.ID, 'reset').text == 'Продолжить'

# проверка восстановление пароля по почте

def test_password_recovery_email(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.password_recovery.click()
    rec_pass = RecPass(start_page, ros_tel.get_current_url())
    rec_pass.mail.click()
    rec_pass.input.send_keys('anna.stepanova69@yandex.ru')

    assert ros_tel.find_element(By.ID, 'reset').text == 'Продолжить'

# проверка восстановление пароля по логину

def test_password_recovery_login(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.password_recovery.click()
    rec_pass = RecPass(start_page, ros_tel.get_current_url())
    rec_pass.login.click()
    rec_pass.input.send_keys('Анна')

    assert ros_tel.find_element(By.ID, 'reset').text == 'Продолжить'

# проверка восстановление пароля по Лицевому счёту

def test_password_recovery_ls(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.password_recovery.click()
    rec_pass = RecPass(start_page, ros_tel.get_current_url())
    rec_pass.ls.click()
    rec_pass.input.send_keys('3679040213269')

    assert ros_tel.find_element(By.ID, 'reset').text == 'Продолжить'

# проверка регистрации нового пользователя до момента подтверждения

def test_register_new_user(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.scroll_down()
    ros_tel.reg_click()
    reg_page = RegPage(start_page, ros_tel.get_current_url())
    reg_page.name.send_keys('Альбина')
    reg_page.lastname.send_keys('Фролова')
    reg_page.address.send_keys('anna.sv21.01@gmail.com')
    reg_page.new_pass.send_keys('Alibina123')
    reg_page.confirm.send_keys('Alibina123')
    reg_page.get_click()

    try:
        assert reg_page.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение email'
    except:
        assert reg_page.find_element(By.CLASS_NAME, 'card-modal__title').text == 'Учётная запись уже существует'

# проверка регистрации с валидными данными

def test_reg_with_valid_values(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.scroll_down()
    ros_tel.reg_click()
    reg_page = RegPage(start_page, ros_tel.get_current_url())
    reg_page.name.send_keys('Ольга')
    reg_page.lastname.send_keys('Фокина')
    reg_page.region.send_keys('Тверская обл')
    reg_page.address.send_keys('+79040213286')
    reg_page.new_pass.send_keys('OlgaFokina54')
    reg_page.confirm.send_keys('OlgaFokina54')
    reg_page.get_click()

    assert reg_page.find_element(By.XPATH,
                                 '//*[@id="page-right"]/div[1]/div[1]/h1[1]').text == 'Подтверждение телефона'
