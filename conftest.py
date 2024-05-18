import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import login, password
from locators import (input_email, input_password, button_login, button_logout, button_checkout_main_page,
                      header_profile)



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


@pytest.fixture(scope='function')
def authorization(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_login)))
    driver.find_element(By.XPATH, input_email).send_keys(login)
    driver.find_element(By.XPATH, input_password).send_keys(password)
    driver.find_element(By.XPATH, button_login).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_checkout_main_page)))
    return driver


@pytest.fixture(scope='function')
def go_to_profile(driver, authorization):
    driver.find_element(By.XPATH, header_profile).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_logout)))
