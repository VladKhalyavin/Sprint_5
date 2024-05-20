import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import login, password
from locators import (button_login, button_login_main_page, button_checkout_main_page, input_email, input_password,
                      header_profile, link_login)


dataset_for_authorization = [['https://stellarburgers.nomoreparties.site/', button_login_main_page],
                             ['https://stellarburgers.nomoreparties.site/', header_profile],
                             ['https://stellarburgers.nomoreparties.site/register', link_login],
                             ['https://stellarburgers.nomoreparties.site/forgot-password', link_login]]


class TestAuthorization:
    @pytest.mark.parametrize('link,button', dataset_for_authorization)
    def test_authorization_main_page_successful_authorization(self, driver, link, button):
        driver.get(link)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button)))
        driver.find_element(By.XPATH, button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_login)))
        driver.find_element(By.XPATH, input_email).send_keys(login)
        driver.find_element(By.XPATH, input_password).send_keys(password)
        driver.find_element(By.XPATH, button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_checkout_main_page)))
        assert (driver.current_url == 'https://stellarburgers.nomoreparties.site/'
                and driver.find_element(By.XPATH, button_checkout_main_page))
