from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.click_botton = "com.saucelabs.mydemoapp.android:id/loginBtn"
        self.error_user_name_text = "com.saucelabs.mydemoapp.android:id/nameErrorTV"
        self.user_name_input = "com.saucelabs.mydemoapp.android:id/nameET"
        self.username_test = "fabiana"
        self.error_password_text = "com.saucelabs.mydemoapp.android:id/passwordErrorTV"
        self.first_username_text = 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/username1TV")'
        self.get_password = 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/password1TV")'
        self.password_input = "com.saucelabs.mydemoapp.android:id/passwordET"


    def click_button_login(self):
        element_text = self.click_element(AppiumBy.ID, self.click_botton)
        return self.get_element_text(AppiumBy.ID, self.error_user_name_text)
    
    def username_login(self):
        self.click_element(AppiumBy.ID, self.user_name_input)
        self.send_keys_to_element(AppiumBy.ID, self.user_name_input, self.username_test)
        self.click_element(AppiumBy.ID, self.click_botton)
        return self.get_element_text(AppiumBy.ID, self.error_password_text)
            
    def username_field(self):
        self.clear_box(AppiumBy.ID, self.user_name_input)
        first_name = self.get_element_text(AppiumBy.ANDROID_UIAUTOMATOR, self.first_username_text)  
        self.send_keys_to_element(AppiumBy.ID, self.user_name_input, first_name)
        return first_name  

    def password_field(self):
        first_password = self.get_element_text(AppiumBy.ANDROID_UIAUTOMATOR, self.get_password)
        self.send_keys_to_element(AppiumBy.ID, self.password_input, first_password)
        return first_password

    def button_login(self):
        self.click_element(AppiumBy.ID, self.click_botton)