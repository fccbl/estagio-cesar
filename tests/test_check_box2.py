#from selenium.webdriver.common.by import By
from pages.check_box_pages import CheckBoxPage

def test_check_box(driver):
    check_box = CheckBoxPage(driver)
    check_box.navigate()
    
    
  # Expand the tree
   # expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
   # expand_all_button.click()
   
    check_box.click_expand_all()
    
  # Select the checkbox "Commands"
    #notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-commands']")
    #notes_checkbox.click()

    check_box.click_label_notes()
    # Validate if checkbox was ticked
    #notes_input = driver.find_element(By.ID, "tree-node-commands")
   # assert notes_input.is_selected()
   
    assert check_box.check_notes_is_selected()