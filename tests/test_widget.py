from pages.widget_page import Widget

def test_menu_widget(driver):
    test_widget = Widget(driver)
    
    test_widget.navigate()
    test_widget.widget_home()
    test_widget.widget_menu()