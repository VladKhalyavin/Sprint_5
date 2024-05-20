from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random_data import RandomAccountData
from locators import button_registration, button_login, input_name, input_email, input_password


class TestRegistration:

    def test_registration_valid_data_successful_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_registration)))
        driver.find_element(By.XPATH, input_name).send_keys('Vlad')
        driver.find_element(By.XPATH, input_email).send_keys(RandomAccountData.login(10))
        driver.find_element(By.XPATH, input_password).send_keys(RandomAccountData.password(10))
        driver.find_element(By.XPATH, button_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_login)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_short_password_registration_failed(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_registration)))
        driver.find_element(By.XPATH, input_name).send_keys('Vlad')
        driver.find_element(By.XPATH, input_email).send_keys(RandomAccountData.login(10))
        driver.find_element(By.XPATH, input_password).send_keys(RandomAccountData.password(5))
        driver.find_element(By.XPATH, button_registration).click()
        assert driver.find_element(By.CSS_SELECTOR, '.input__error').text == 'Некорректный пароль'
