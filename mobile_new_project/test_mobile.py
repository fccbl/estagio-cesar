import pytest
from pages.home_mob_page import HomePage

def test_product_selection(driver):
    home_page = HomePage(driver)

    home_page.click_show_popup()
    assert  home_page.get_popup_title() == "Confirm"

    home_page.click_accept()

