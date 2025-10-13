from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class FormPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.validate_screen = 'new UiSelector().className("android.widget.LinearLayout").instance(2)'
        self.input_full_name = "com.saucelabs.mydemoapp.android:id/fullNameET"
        self.input_adressline = "com.saucelabs.mydemoapp.android:id/address1ET"
        self.input_city = "com.saucelabs.mydemoapp.android:id/cityET"
        self.input_country = "com.saucelabs.mydemoapp.android:id/countryET"
        self.input_zip_code = "com.saucelabs.mydemoapp.android:id/zipET"
        self.input_cardnumber = "com.saucelabs.mydemoapp.android:id/cardNumberET"
        self.input_state = "com.saucelabs.mydemoapp.android:id/stateET"
        self.button_click = "com.saucelabs.mydemoapp.android:id/paymentBtn"
        self.full_name_payment = "com.saucelabs.mydemoapp.android:id/nameET"
        self.cardnumber_payment = "com.saucelabs.mydemoapp.android:id/cardNumberET"
        self.expiradition_date = "com.saucelabs.mydemoapp.android:id/expirationDateET"
        self.security_code = "com.saucelabs.mydemoapp.android:id/securityCodeET"
        self.validade_chekout = 'new UiSelector().className("android.view.ViewGroup").instance(3)'
        self.validate_fullname = "com.saucelabs.mydemoapp.android:id/fullNameTV"
        self.validate_adress = "com.saucelabs.mydemoapp.android:id/addressTV"
        self.validate_city = "com.saucelabs.mydemoapp.android:id/cityTV"
        self.validate_state = "com.saucelabs.mydemoapp.android:id/cityTV"
        self.validate_country = "com.saucelabs.mydemoapp.android:id/countryTV"
        self.validate_zipcde = "com.saucelabs.mydemoapp.android:id/countryTV"
        self.validate_payment_fullname = "com.saucelabs.mydemoapp.android:id/cardHolderTV"
        self.validate_card_number="com.saucelabs.mydemoapp.android:id/cardNumberTV"
        self.validate_title = "com.saucelabs.mydemoapp.android:id/titleTV"
        self.validate_price = "com.saucelabs.mydemoapp.android:id/priceTV"
        self.validate_code = "com.saucelabs.mydemoapp.android:id/expirationDateTV"
        self.final_value_id = "com.saucelabs.mydemoapp.android:id/totalAmountTV"
        self.delivery_value_id = "com.saucelabs.mydemoapp.android:id/amountTV"
        self.qnt_items_id = "com.saucelabs.mydemoapp.android:id/itemNumberTV"
        self.unit_price_id = "com.saucelabs.mydemoapp.android:id/priceTV"
        self.order_button = "com.saucelabs.mydemoapp.android:id/paymentBtn"




    def validate(self):
       return self.is_element_displayed(AppiumBy.ANDROID_UIAUTOMATOR , self.validate_screen)
    
    def form(self, dados):
        self.send_keys_to_element(AppiumBy.ID, self.input_full_name,dados["full_name_address"])
        self.send_keys_to_element(AppiumBy.ID, self.input_adressline,dados["address_line"])
        self.send_keys_to_element(AppiumBy.ID, self.input_city,dados["city"])
        self.send_keys_to_element(AppiumBy.ID, self.input_state,dados["state"])
        self.send_keys_to_element(AppiumBy.ID, self.input_zip_code,dados["zip_code"])
        self.send_keys_to_element(AppiumBy.ID, self.input_country,dados["country"])

    def payment_button(self):
        self.click_element(AppiumBy.ID, self.button_click)

    def payment_form(self, dados):
        self.send_keys_to_element(AppiumBy.ID, self.full_name_payment, dados["full_name_payment"])
        self.send_keys_to_element(AppiumBy.ID, self.cardnumber_payment, dados["card_number"])
        self.send_keys_to_element(AppiumBy.ID, self.expiradition_date, dados["exp_date"])  
        self.send_keys_to_element(AppiumBy.ID, self.security_code, dados["secure_code"])  

    def checkout_validate(self):
        return self.is_element_displayed(AppiumBy.ANDROID_UIAUTOMATOR, self.validade_chekout)
    
    def full_name_validate(self, dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_fullname)
        assert element_text == dado["full_name_address"], f"Expected '{dado}', but got '{element_text}'"

    def adress_validate(self, dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_adress)
        assert element_text == dado["address_line"], f"Expected '{dado}', but got '{element_text}'"

    def city_validate(self, dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_city)
        element = element_text.split(",")[0]
        assert element == dado ["city"],f"Expected '{dado}', but got '{element}'" 

    def state_validate(self, dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_state)
        element = element_text.split(",")[1].strip()
        assert element == dado["state"],f"Expected '{dado}', but got '{element}'" 

    def coutry_validate(self, dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_country)
        element = element_text.split(",")[0]
        assert element == dado["country"],f"Expected '{dado}', but got '{element}'" 

    def zip_code_validate(self,dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_zipcde)
        element = element_text.split(",")[1].strip()
        assert element == dado["zip_code"],f"Expected '{dado}', but got '{element}'" 

    def validate_fullname_card(self, dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_payment_fullname)
        assert element_text == dado["full_name_payment"], f"Expected '{dado}', but got '{element_text}'"

    def validate_card(self, dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_card_number)
        assert element_text == dado["card_number"], f"Expected '{dado}', but got '{element_text}'"

    def validate_product(self,dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_title)
        assert element_text == dado["name"], f"Expected '{dado}', but got '{element_text}'"

    def expectative_validate_price(self,dado):
        element_text = self.get_element_text(AppiumBy.ID, self.validate_price)
        assert element_text == dado["price_unit"], f"Expected '{dado}', but got '{element_text}'"

    def expectative_validate_code(self,dado):
        scroll_validate = self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{self.validate_code}"));')
        element_text = self.get_element_text(AppiumBy.ID, self.validate_code)
        assert element_text == dado["exp_final"], f"Expected '{dado}', but got '{element_text}'"
     
    def total_price(self,dado):
        #unit_price = data["products"]["unit_price_float"]
        unit_price= dado["price_unit_value"]
        qnt_items = int(self.get_element_text(AppiumBy.ID, self.qnt_items_id).split()[0])
        delivery = float(self.get_element_text(AppiumBy.ID, self.delivery_value_id).replace("$","").strip())
        final_value = float(self.get_element_text(AppiumBy.ID, self.final_value_id).replace("$","").strip())
        assert final_value == delivery + (qnt_items * unit_price)

    def cick_order_button(self):
        self.click_element(AppiumBy.ID, self.order_button)