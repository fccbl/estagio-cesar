from pages.text_box_page import TextBoxPage


def test_fill_form_with_pom(driver):
    text_box_page = TextBoxPage(driver)
    text_box_page.navigate()

    # Test data
    full_name = "John Doe"
    email = "john.doe@example.com"
    current_address = "123 Main St"
    permanent_address = "456 Oak Ave"

    # Fill and submit form using page object methods
    text_box_page.fill_form(full_name, email, current_address, permanent_address)
    text_box_page.submit()

    # Get output and assert
    output = text_box_page.get_output_text()

    assert full_name in output
    assert email in output
    assert current_address in output
    assert permanent_address in output