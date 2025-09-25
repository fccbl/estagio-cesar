from selenium.webdriver.common.by import By
from pages.tool_tips_page import ToolTipsPage
import json
from utils.data_loader import load_json_data

test_data = load_json_data("data/test_data.json")


def test_button_tooltip(driver):

    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    tool_tips_page.hover_over_button()

    tooltip_text = tool_tips_page.get_tooltip_text()
    assert tooltip_text == test_data["tool_tip_button_text"]

def test_field_tooltip(driver):

    tool_tips_page = ToolTipsPage(driver)

    tool_tips_page.navigate(test_data["tool_tips_url"])

    tool_tips_page.hover_over_field()
    
    tooltip_text = tool_tips_page.get_tooltip_text()

    assert tooltip_text == (test_data["tool_tip_field_text"])