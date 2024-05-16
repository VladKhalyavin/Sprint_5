import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import button_login, button_logout, header_constructor, header_stellar_burger


class TestAccountPage:

    def test_go_to_profile_from_main_page_successful(self, driver, go_to_profile):
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()

    @pytest.mark.parametrize('button', [header_stellar_burger, header_constructor])
    def test_go_to_main_page_from_profile_successful(self, driver, go_to_profile, button):
        driver.find_element(By.XPATH, button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_logout_successful(self, driver, go_to_profile):
        driver.find_element(By.XPATH, button_logout).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button_login)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()