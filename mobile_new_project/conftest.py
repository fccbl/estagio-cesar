from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common.base import AppiumOptions
import pytest
import os
import base64

@pytest.fixture(scope="function")
def driver(request):
    # --- SETUP PHASE ---
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.automationmodule",
        "appium:appActivity": "com.automationmodule/.MainActivity"
    })

    # try:
    #     options = AppiumOptions()
    #     # ... capabilities ...
    #     _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    # except Exception as e:
    #     # If driver creation fails, skip the test with a message
    #     pytest.skip(f"Failed to create Appium driver: {e}")
    try:
        _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        _driver.start_recording_screen() # Start recording
    except Exception as e:
        pytest.skip(f"Failed to create Appium driver: {e}")

    yield _driver

    # Teardown
    if _driver:
        # Stop recording and get the video data
        video_data = _driver.stop_recording_screen()
        if video_data:
            # Create a unique filename for the video
            video_filename = f"videos/video_{request.node.name}.mp4"
            with open(video_filename, "wb") as f:
                f.write(base64.b64decode(video_data))
            print(f"Video saved as {video_filename}")
        _driver.quit()

    

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot_name = f"screenshots/screenshot_{item.name}.png"
            driver.get_screenshot_as_file(screenshot_name)
            print(f"Screenshot saved as {screenshot_name}")



 
