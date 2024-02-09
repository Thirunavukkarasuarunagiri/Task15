from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")


username_field = driver.find_element_by_id("user-name")
password_field = driver.find_element_by_id("password")
login_button = driver.find_element_by_css_selector("input[type='submit']")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

login_button.click()

# Task 1: Get the title of the webpage
title = driver.title
print("Title of the webpage:", title)

# Task 2: Get the current URL of the webpage
current_url = driver.current_url
print("Current URL of the webpage:", current_url)

# Task 3: Extract the entire contents of the webpage
page_source = driver.page_source

with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)


driver.quit()