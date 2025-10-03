from selenium.webdriver.common.by import By

class TextBoxForm:
    def __init__ (self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        #forms
        self.fullname_input = self.find_element(By ID, "username")
        self.email_input = self.find_element(By ID,  "userEmail")
        self.current_adress_input = self.find_element(By ID,  "currentAddress")
        self.permanent_address_input = self.find_element(By ID,  "permanentAddress")
        self.submit_botton = self.find_element(By ID, "submit")
        self.output = self.find_element(By ID, "output")

    def navigator (self):
        self.driver.get(self.url)

    def fillforms (self):
        self.driver.find_element(*self.fullname_input).send_keys("fabiana lima")

    

    









# métodos como:
# open() — abre a página do formulário de Text Box
# set_full_name(name)
# set_email(email)
# set_current_address(address)
# set_permanent_address(address)
# submit()
# get_output() — retorna o texto mostrado após submissão