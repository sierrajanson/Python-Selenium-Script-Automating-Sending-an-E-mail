"""
Created by Sierra Janson
December 2022

Purpose:
User Requirements: Fork this repl.it and input your e-mail & password, and the e-mail & message for who you want to send a message to.

Notice: 
In the middle of the script, you will be prompted by the console to enter the bot-text to satisfy reCAPTCHA v3, as I have not been able to get around it yet.

Made with Selenium library
"""
# WARNING: PLEASE READ ABOVE, you need to input information where directed in the code below in order for the script to work... as free repl.it accounts are public to all repl.it users, it is strongly recommended you use the log-in information for a g-mail that does not contain information personal to you ... I am not responsible for any harm that comes to users that resulted from not heeding the above warnings.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
time.sleep(3.12334534)
driver.get("https://google.com/")
time.sleep(4.39485834)
# logging in 
gmailButton = driver.find_element(By.CSS_SELECTOR, "a[href='https://mail.google.com/mail/&ogbl']")
gmailButton.click()
time.sleep(4.12938192478)
signIN = driver.find_element(By.CSS_SELECTOR, "a[data-action='sign in']")
signIN.click()
time.sleep(3)
username = driver.find_element(By.NAME, "identifier")
username.send_keys("") # PUT YOUR G-MAIL IN QUOTATIONS HERE
username.send_keys(Keys.ENTER)
# HANDLING reCAPTCHA v3
try:
  pwd = driver.find_element(By.NAME, "Passwd")
  pwd.send_keys("")
  pwd.send_keys(Keys.ENTER)
except:
  saveTheDay = input() #PROMPTED TO ENTER reCAPTCHA v3 TEXT HERE
  botTest = driver.find_element(By.NAME, "ca")
  botTest.send_keys(saveTheDay)
  botTest.send_keys(Keys.ENTER)
  time.sleep(3)
  pwd = driver.find_element(By.NAME, "Passwd")
  pwd.send_keys("") # PUT YOUR G-MAIL PASSWORD HERE
  pwd.send_keys(Keys.ENTER)
  time.sleep(10)
  compose = driver.find_element(By.CSS_SELECTOR, "div[jscontroller='eIu7Db']")
  compose.click()
  time.sleep(10)
  friend = driver.find_element(By.CSS_SELECTOR, "input[aria-haspopup='listbox']")
  friend.send_keys("") # PUT A FRIEND'S EMAIL HERE
  subject = driver.find_element(By.ID, ":qo")
  subject.send_keys("you're the best") # change the subject of your email here
  box = driver.find_element(By.ID, ":ru")
  box.send_keys("pleading face emoji") # change the message you want to send to your friend here
  sendButton = driver.find_element(By.ID, ":qe")
  sendButton.click()

"""
Future vision for this project:
- creating a simple GUI for a user to input their gmail/password & person2gmail/message instead of having to manually change it in the code
- getting around reCAPTCHA v3

More information about the project:
- website was loading too slowly for script, added time.sleep()s where necessary throughout the script to give the website time to load..if project throws an error try re-running the project again and it should be fine
  - values in time.sleep() are varied as I was experimenting to see if very specific     
  different time.sleep() values would mislead Google into thinking this session was an 
  authentic person logging in 
"""