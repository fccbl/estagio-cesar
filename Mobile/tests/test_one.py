import pytest  
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.my_car_page import MyCarPage
from pages.login_usr_page import LoginPage
from pages.form_page import FormPage
# Import other page objects as needed


def test_product_selection(driver, appium_test_capabilities):
    # Initialize page objects with the driver provided by the fixture
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    my_car_page = MyCarPage(driver)
    login_usr_page = LoginPage(driver)
    form_page = FormPage(driver)
    form_data = appium_test_capabilities["form_user"]["backpack"]
    product_data = appium_test_capabilities["products"]["backpack"]


    # Perform actions using page object methods
    home_page.get_home_page_title(product_data)
    home_page.select_orange_backpack()

    #Continue with product page interactions
    product_page.get_product_page_title(product_data) 
    product_page.decrease_quantify()
    assert product_page.button_cart() == False
    product_page.add_quantify()
    product_page.card_button_enabled()
    product_page.add_to_cart()
    product_page.validate_cart_quantity()
    product_page.click_to_cart_icon()


    # # # ... continue with other page interactions

    my_car_page.is_cart_screen_displayed()
    my_car_page.validade_product(product_data)
    my_car_page.unit_price_text(product_data)
    assert my_car_page.validate_items() == 2 
    assert my_car_page.validate_quantify() == 2
    my_car_page.validate_total()
    my_car_page.click_button()
    my_car_page.click_checkout()

    assert login_usr_page.click_button_login() == "Username is required"
    assert login_usr_page.username_login() == "Enter Password"
    login_usr_page.username_field()
    login_usr_page.password_field()
    login_usr_page.button_login()

    form_page.validate()

    form_page.form(form_data)

    form_page.payment_button()

    form_page.payment_form(form_data)

    form_page.payment_button()

    form_page.checkout_validate()

    form_page.full_name_validate(form_data)

    form_page.adress_validate(form_data)

    form_page.city_validate(form_data)

    form_page.state_validate(form_data)

    form_page.coutry_validate(form_data)

    form_page.zip_code_validate(form_data)

    form_page.validate_fullname_card(form_data)

    form_page.validate_card(form_data)

    form_page.validate_product(product_data)

    form_page.expectative_validate_price(product_data)

    form_page.expectative_validate_code(form_data)

    form_page.total_price(product_data)
    