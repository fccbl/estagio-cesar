from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Alert:
    def __init__ (self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"
        self.alerts_home = (By.XPATH, "//*[text()='Alerts, Frame & Windows']")
        self.alerts = (By.XPATH, "//span[text()='Alerts']")
        self.alerts_button = (By.ID, "alertButton")
        self.wait = WebDriverWait(driver, 10)
        self.time_alert_button = (By.ID, "timerAlertButton")

   
    def navigate(self):
        self.driver.get(self.url)
                 
    def Find_Alert_home(self):
        self.driver.find_element(*self.alerts_home).click()

    def Alert_Page(self):
        menu_left = self.wait.until(EC.visibility_of_element_located(self.alerts))
        menu_left.click()

    def Button(self): 
       self.driver.find_element(*self.alerts_button).click()
    
    def Wait_button(self):
       simple_alert = self.wait.until(EC.alert_is_present())
       return simple_alert.text
        
    def accept_alert(self):
        simple_alert = self.wait.until(EC.alert_is_present())
        return simple_alert.accept


     #def click_time_alert_button(self):
    #   self.driver.find_element(*self.time_alert_button).click()