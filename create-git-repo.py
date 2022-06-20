from selenium import webdriver
import keyring
import sys

print("---- PYTHON SCRIPT STARTED")

PATH = "/Users/roland/Desktop/Coding/tools/chromedriver"
browser = webdriver.Chrome(PATH)

# Get login page and elements
browser.get("https://github.com/login")
loginField = browser.find_element_by_xpath("//*[@id='login_field']")
passwordField = browser.find_element_by_xpath("//*[@id='password']")
signInButton = browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")

# Log in
loginField.send_keys("RoliVegas")
passwordField.send_keys(keyring.get_password("git", "sajat"))
signInButton.click()

# Get new repo page and elements
browser.get("https://github.com/new")
repoNameField = browser.find_element_by_xpath("//*[@id='repository_name']")
createButton = browser.find_element_by_xpath("//*[@id='new_repository']/div[5]/button")

# Create new repo
repoNameField.send_keys(sys.argv[1])
createButton.submit()

browser.close()

print("---- PYTHON SCRIPT FINISHED ----")