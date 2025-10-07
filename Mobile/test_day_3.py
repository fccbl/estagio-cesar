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
	"appWaitDuration": 30000,  # opcional, tempo de espera em ms (30s)
    "uiautomator2ServerLaunchTimeout": 30000,
    "uiautomator2ServerInstallTimeout": 30000
})
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(4)

#variables
expected_title = "Sauce Labs Backpack (orange)"
unit_price = 29.99
full_name = "fabiana c c b lima"
adress_line = "rua jose moscow"
adress_line2 = "rua jose cardoso"
city = "recife"
state = "pernambuco"
zip_code = "52015231"
country = "brasil"
card_number = "314546776589902"
expiradition_date = "02/32"
security_code = 234
username_fabiana = "fabiana"
expected_price = "$ 29.99"
price = unit_price *2
expected_error_password = "Enter Password"
expected_error_username = "Username is required"

#Select the product Sauce Labs Backpack (orange) from the list of products
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value= 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(2)').click()
time.sleep(1)

#Validate that the product page opened corresponds to the correct product
actual_title = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV").text
assert actual_title == expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'"

#Decrease the quantity of products by pressing '-' and validate that the quantity has decreased by 1 unit
before_number = int(driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/noTV").text)
decrase_quanty = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV").click()
after_number = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)
assert before_number - after_number == 1

#validate that when you reach zero quantity of products the Add to cart button will become inactive.
cart_button = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
assert not cart_button.is_enabled(), "Disabled"

#Increase the quantity of products by pressing '+' and check that the quantity has increased by 1 unit
before_number_add = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)
add_quantify = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV").click()
after_number_add = int(driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/noTV").text)
assert before_number_add + after_number_add == 1

#check that when you reach more than zero units the Add to cart button will become active
cart_button= driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt") 
assert cart_button.is_enabled(), "Enabled"

#Add another unit by pressing +, make sure you have 2 units and click on the Add to cart button.
add_quantify = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV").click()
new_quantify = after_number_add + 1
assert new_quantify
#click  cart bottom
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt").click()

#Validate that a circle has appeared in the cart icon informing you of the exact number of items you have added to the cart
validade_number_quantify = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)
validade_number_car = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartTV").text)
assert validade_number_quantify == validade_number_car

#Open the cart page by clicking on the cart icon
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartTV").click()
time.sleep(2)
#Validate that the My Cart screen has been opened
page_little_car = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/scrollView")
time.sleep(2)
assert page_little_car.is_displayed()

#Validate that your product is correct
validate_backpag_orange = driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/titleTV").text
#time.sleep(1)
assert validate_backpag_orange == expected_title, f"Expected title to be '{expected_title}', but found '{validate_backpag_orange}'"

#Validate that the unit price is as expected
unit_price_page = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV").text
assert unit_price_page == expected_price, f"Expected title to be '{expected_price}', but found '{unit_price_page}'"

#Validate that the quantity is correct in the field below the product photo
validate_quantify_itens = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)
assert validate_quantify_itens == 2

#Validate that the quantity is correct in the Total: x Items 
total_text = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemsTV").text
total_items = int(total_text.split()[0])
assert total_items == 2

#Validate that the total value of the purchase is as expected for 2 units of the product
validade_total_product = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalPriceTV").text
validade_product = float(validade_total_product.replace("$", "").strip())
calculator_item = unit_price * 2
assert validade_product == calculator_item, f"Expected title to be '{calculator_item}', but found '{validade_product}'"

#Click on the Proceed To Checkout button
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt").click()
time.sleep(1)
#Validate that the Login screen has been displayed
checkout_display = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value= 'new UiSelector().className("android.widget.ScrollView")')
time.sleep(1)
checkout_display.is_displayed()

#Log in without entering Username and Password
#time.sleep(1)
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn").click()

# Log in without entering Password and validate the error in the Password
error_username = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV").text
assert error_username == expected_error_username,f"Expected title to be '{expected_error_username}', but found '{error_username}'"

# Log in without entering Password and validate the error in the Password
user_name_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
user_name_input.send_keys(username_fabiana)

#Validate the error in the Password 
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn").click()
error_password = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV").text
assert error_password == expected_error_password, f"Expected title to be '{expected_error_password}', but found '{error_password}'"

#Capture the first Username from the Usernames list at the bottom 
first_username = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/username1TV").text
user_name_input.clear()
user_name_input.send_keys(first_username)

#Capture the Password from the Password list at the bottom
password_text = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/password1TV").text
password = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
password.send_keys(password_text)

#Click on the Login button
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn").click()

#Validate that the Checkout, Shipment Address
time.sleep(2)
validate_window_checkout = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(2)')
time.sleep(2)
assert validate_window_checkout.is_displayed()

#Enter information in all the form fields and proceed to payment
fullname_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
time.sleep(1)
fullname_input.send_keys(full_name)

adress_line_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
adress_line_input.send_keys(adress_line)

adress_line_input_2 = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address2ET")
adress_line_input_2.send_keys(adress_line2)

city_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")
city_input.send_keys(city)

state_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/stateET")
state_input.send_keys(state)

zip_code_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")
zip_code_input.send_keys(zip_code)

country_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")
country_input.send_keys(country)

button_to_payment = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn").click()
time.sleep(1)
#Validate that the Checkout, Payment screen has been displayed
checkout_screen = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/checkoutSV")
checkout_screen.is_displayed()

#Enter the values in the corresponding fields and keep the check-box selected
full_name_payment_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
full_name_payment_input.send_keys(full_name)

cart_number_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")
cart_number_input.send_keys(card_number)

expiration_date_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET")
expiration_date_input.send_keys(expiradition_date)

security_code_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET")
security_code_input.send_keys(security_code)

#Proceed to the review by clicking on the Review Order button
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn").click()

#Validate that the Checkout, Review your order screen has been displayed.

validate_window_review = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(3)')
time.sleep(2)
validate_window_review.is_displayed()

#Validate that the Deliver Address and Payment Method information 
validate_deliver_adress_fullname = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameTV").text
assert full_name == validate_deliver_adress_fullname, f"Expected title to be '{validate_deliver_adress_fullname}', but found '{full_name}'"

validate_adress = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/addressTV").text
assert validate_adress == adress_line, f"Expected title to be '{validate_adress}', but found '{adress_line}'"

validate_city = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityTV").text
validate_city_final =validate_city.split(",")[0]
assert validate_city_final == city

validate_state = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityTV").text
validate_state_final = validate_state.split(",")[1].strip()
assert validate_state_final == state

validate_country = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryTV").text
validate_coutry_final = validate_country.split(",")[0]
assert validate_coutry_final == country

validate_code = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryTV").text
validate_code_final= validate_code.split(",")[1].strip()
assert validate_code_final == zip_code

payment_validate_full_name = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardHolderTV").text
assert payment_validate_full_name == full_name

validate_card_number = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberTV")
assert card_number in validate_card_number.text

validate_product = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV").text
assert validate_product == expected_title

validate_price = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV").text
assert validate_price == expected_price

expiration_date_validate= "com.saucelabs.mydemoapp.android:id/expirationDateTV"
scrolling_expiration_validate = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{expiration_date_validate}"));')


total_price_text = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalAmountTV").text
price = float(total_price_text.replace("$"," ").strip())

freight_text = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/amountTV").text
freight = float(freight_text.replace("$", " ").strip())
assert price ==  freight + (unit_price *2)

#Click on the Place Order button
driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn").click()

time.sleep(1)
#Validate that the Checkout Complete screen has been displayed
validade_checkout_complete = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Manages scrolling of views in given screen")')
#time.sleep(1)
validade_checkout_complete.is_displayed()
#time.sleep(1)

#Click on the Continue Shopping button
driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/shoopingBt").click()
time.sleep(1)

#Validate that the Products screen has been displayed and that the cart is empty.
validate_product_page =driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(2)')
validate_product_page.is_displayed() 

driver.quit()