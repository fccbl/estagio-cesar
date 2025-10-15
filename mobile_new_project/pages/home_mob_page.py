from appium.webdriver.common.appiumby import AppiumBy
from .base_mob_page import BasePage
from utils.logger import log

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.show_id_poupup = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Show Popup")')
        self.accept = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accept")')
        self.cancel = 'new UiSelector().className("android.widget.Button").instance(0)'
        self.confirm = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Confirm")')
        self.notification = 
    
    def click_show_popup(self):
        log.info("clicando no show poupup")
        #declarar a variavel e quando chamar a variavel,colocar o *, porque é uma tupla
        self.click_element(*self.show_id_poupup)

    def get_popup_title(self):
        return self.get_element_text(*self.confirm)
    
    def click_accept(self):
        self.click_element(*self.accept)