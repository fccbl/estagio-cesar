from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class MyCarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_cart_screen = "com.saucelabs.mydemoapp.android:id/scrollView"
        self.validate_tittle_backpag = "com.saucelabs.mydemoapp.android:id/titleTV"
        self.id_validate_unit_price = "com.saucelabs.mydemoapp.android:id/priceTV"
        self.id_number_quantify = "com.saucelabs.mydemoapp.android:id/noTV"
        self.total_items = "com.saucelabs.mydemoapp.android:id/itemsTV"
        self.unit_price = 29.99
        self.total_quantify_price = "com.saucelabs.mydemoapp.android:id/totalPriceTV"
        self.card_click = "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/cartTV']"
        self.screen_cart = "new UiSelector().resourceId('com.saucelabs.mydemoapp.android:id/scrollView')"
        self.button_checkout = "com.saucelabs.mydemoapp.android:id/cartBt"

    
    def is_cart_screen_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.check_cart_screen)
   
    def validade_product(self,dado):
      element_text =self.get_element_text(AppiumBy.ID, self.validate_tittle_backpag)
      assert element_text == dado["name"],f"Expected '{dado}', but got '{element_text}'"
    
    def unit_price_text(self,dado):
        text_price = self.get_element_text(AppiumBy.ID, self.id_validate_unit_price)
        assert text_price == dado["price_unit"],f"Expected '{dado}', but got '{text_price}'"
    
    def validate_items(self):
        return int(self.get_element_text(AppiumBy.ID, self.id_number_quantify))
    
    def validate_quantify(self):
        items_text = self.get_element_text(AppiumBy.ID, self.total_items)
        result_quantify= int(items_text.split()[0])
        return result_quantify
    
    def validate_total(self):
        total_text = self.get_element_text(AppiumBy.ID, self.total_quantify_price)
        total_price = float(total_text.replace("$"," ").strip())
        calculator = self.unit_price * 2
        assert total_price ==  calculator 
    
    def click_button(self):
        self.click_element(AppiumBy.XPATH, self.card_click)

    def is_cart_screen_is_apple(self):
        return self.is_element_displayed(AppiumBy.ANDROID_UIAUTOMATOR, self.screen_cart)
    
    def click_checkout(self):
        self.click_element(AppiumBy.ID, self.button_checkout)
