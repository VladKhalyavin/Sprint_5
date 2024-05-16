import pytest
from selenium.webdriver.common.by import By
from locators import (constructor_navigation_fillings, constructor_navigation_sauces, constructor_navigation_buns,
                      constructor_header_fillings, constructor_header_sauces, constructor_header_buns,
                      constructor_div_buns, constructor_div_fillings, constructor_div_sauces, first_ingredient,
                      last_ingredient)


dataset_for_constructor = [[constructor_navigation_buns, constructor_header_buns, constructor_div_buns,
                            last_ingredient],
                           [constructor_navigation_sauces, constructor_header_sauces, constructor_div_sauces,
                            last_ingredient],
                           [constructor_navigation_fillings, constructor_header_fillings, constructor_div_fillings,
                            first_ingredient]]


class TestConstructor:
    @pytest.mark.parametrize('navigation,header,div, ingredient', dataset_for_constructor)
    def test_navigation_by_ingredients(self, driver, authorization, navigation, header, div, ingredient):
        element = driver.find_element(By.XPATH, ingredient)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(By.XPATH, navigation).click()
        assert (driver.find_element(By.XPATH, header).is_displayed() and
                'tab_tab_type_current' in driver.find_element(By.XPATH, div).get_attribute('class'))
        driver.quit()
