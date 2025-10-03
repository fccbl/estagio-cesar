from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

#Inicializador
class Widget:
    def __init__ (self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"
        self.widget_page = (By.XPATH, "//h5[text()='Widgets']")
        self.widget_left = (By.XPATH, "//span[text()='Menu']")
        self.wait = WebDriverWait(driver,10)


#abrir o site demoqa
    def navigate(self):
        self.driver.get(self.url)
#clicar no botao Widget no home
    def widget_home(self):
        self.driver.find_element(*self.widget_page).click()
        self.driver.find_elements()
#dar um scroll e clicar no Widget do Menu
    def widget_menu(self):
        menu_widget = self.wait.until(EC.visibility_of_element_located(self.widget_left))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", menu_widget)
        menu_widget.click()
#

    