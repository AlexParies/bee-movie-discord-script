from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

uname = input("username:  ")
passw = input("password:  ")
chat = input("link to chat:  ")

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.title  # => "fttc"

driver.implicitly_wait(5.5)

driver.get(chat)

username = driver.find_element(By.NAME, 'email')
password = driver.find_element(By.NAME, 'password')

username.send_keys(uname)
driver.implicitly_wait(2.5)
password.send_keys(passw)
password.send_keys(u'\ue007')

useless = ('may need to verify, press enter when done')
print(useless)
ok = input('')

time.sleep(3)

passwordsL = []
f = open("bees.txt", "r")
for line in f:
    passwordsL.append(line)
    print(line)

ok = input('press enter when finished loading... ')

msg_input = driver.find_element_by_xpath(
    '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[3]/div/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')

for i in passwordsL:

    print(i)
    time.sleep(1)
    msg_input.send_keys(i)
    msg_input.send_keys(u'\ue007')
