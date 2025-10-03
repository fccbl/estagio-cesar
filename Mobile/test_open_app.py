import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.saucelabs.mydemoapp.android",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
    "appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.MainActivity",
	"appWaitDuration": 30000  # opcional, tempo de espera em ms (30s)
})
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(4)
	
first_bag_pack = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(0)')
first_bag_pack.click()

change_color_green = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Green color']").click()

increment_quantify = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Increase item quantity").click()

add_to_cart= driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart").click()

click_little_car = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV").click()

time.sleep(1)

decrease_increment = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV").click()

checkout = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Confirms products for checkout").click()

time.sleep(1)

login_user = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")

login_user.send_keys("UserTest")

login_password = driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/passwordET")

login_password.send_keys("PasswordTest")

login = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials").click()

time.sleep(2)

fullname = driver.find_element(AppiumBy.ID,value = 'com.saucelabs.mydemoapp.android:id/fullNameET')


time.sleep(3)

fullname.send_keys("fabiana lima ")

adress = driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/address1ET")

time.sleep(1)

adress.send_keys("rua blabla")

adress2 = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address2ET")

time.sleep(1)

adress2.send_keys("rua 2")

city = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")

time.sleep(1)

city.send_keys("recife")

state = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/stateET")

time.sleep(1)

state.send_keys("pernambuco")

code = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")

time.sleep(1)

code.send_keys("38473874")

country = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")

time.sleep(1)

country.send_keys("brazil")

payment= driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Saves user info for checkout").click()

name_full_cart = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@resource-id='com.saucelabs.mydemoapp.android:id/nameET']")

time.sleep(3)

name_full_cart.send_keys("fabiana c c b lima")

cart_number = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")

time.sleep(1)

cart_number.send_keys("7282732")

time.sleep(1)

expired_date = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/expirationDateET")')

time.sleep(1)

expired_date.send_keys("02/37")

security_code = driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/securityCodeET")

security_code.send_keys("123")

time.sleep(1)

review_order = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Saves payment info and launches screen to review checkout data').click()

place_order = driver.find_element(AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/paymentBtn").click()

time.sleep(1)

thankyou_message = driver.find_element(AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/thankYouTV").text

assert thankyou_message == "Thank you for your order"

driver.quit()