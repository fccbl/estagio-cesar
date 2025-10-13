from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.id_product_orange_text = "//android.widget.TextView[@resource-id=\"com.saucelabs.mydemoapp.android:id/productTV\" and @text='Sauce Labs Backpack (orange)']"
        self.id_decrease_quantify = "com.saucelabs.mydemoapp.android:id/minusIV"
        self.id_number_quantify = "com.saucelabs.mydemoapp.android:id/noTV"
        self.cart = "com.saucelabs.mydemoapp.android:id/cartBt"
        self.increase_quantify = "com.saucelabs.mydemoapp.android:id/plusIV"
        self.items_cart = "com.saucelabs.mydemoapp.android:id/cartTV"
        


    def get_product_page_title(self,dado):
        element_text = self.get_element_text(AppiumBy.XPATH, self.id_product_orange_text)
        assert element_text == dado["name"], f"Expected '{dado}', but got '{element_text}'"
    
    def decrease_quantify(self):
        before = int(self.get_element_text(AppiumBy.ID, self.id_number_quantify))
        self.click_element(AppiumBy.ID, self.id_decrease_quantify)
        after = int(self.get_element_text(AppiumBy.ID, self.id_number_quantify))
        assert after == before - 1, f"Expected {before - 1}, but got {after}"
    
    def button_cart(self):
        return self.enable_cart(AppiumBy.ID, self.cart)

    def add_quantify(self):
        last_quantify = int(self.get_element_text(AppiumBy.ID, self.id_number_quantify))
        self.click_element(AppiumBy.ID, self.increase_quantify)
        new_quantify = int(self.get_element_text(AppiumBy.ID, self.id_number_quantify))
        assert new_quantify == last_quantify + 1, f"Expected {last_quantify + 1}, but got {new_quantify}"

    def card_button_enabled(self):
        return self.enable_cart(AppiumBy.ID, self.cart)
    
    def add_to_cart(self):
        self.click_element(AppiumBy.ID, self.increase_quantify)
        new_quantify = int(self.get_element_text(AppiumBy.ID, self.id_number_quantify))
        self.click_element(AppiumBy.ID, self.cart)
        assert new_quantify == 2
    
    def validate_cart_quantity(self):
        items_car = self.get_element_text(AppiumBy.ID, self.items_cart)
        quantify = self.get_element_text(AppiumBy.ID, self.id_number_quantify)
        assert items_car == quantify 
    
    def click_to_cart_icon(self):
        self.click_element(AppiumBy.ID, self.items_cart)