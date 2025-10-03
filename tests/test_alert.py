from pages.alert_page import Alert
import time

#def test_first(driver):
#    alert_test = Alert (driver)
#    alert_test.navigate()
    
#    alert_test.Find_Alert_home()

#    alert_test.Alert_Page()
#    time.sleep(2)

#    alert_test.Button()

#    texto = alert_test.Wait_button()
#    assert texto == "You clicked a button"
#    time.sleep(1)

#    alert_test.accept_alert()
#    time.sleep(1)

def test_second(driver):
    alert_test = Alert(driver)
    alert_test.navigate()