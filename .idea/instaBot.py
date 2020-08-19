#This program created by sam mordoch for study and research use on your own risk of getting banned from IG
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#i use chrome so you will need to install selenium python and chrome driver
PATH="C:\Program Files (x86)\chromedriver.exe"#enter chrome driver path here
driver=webdriver.Chrome(PATH)
#Enter your username and password here
username="username"
password="password"
#this fun will log you in using the info above
def login(username,password):
    user_input=driver.find_element_by_name("username")
    user_input.send_keys(username)
    user_password=driver.find_element_by_name("password")
    user_password.send_keys(password)
    user_password.send_keys(Keys.ENTER)
    time.sleep(5)
#this func will like photos and videos in the explore page call it with the amount of likes you want to give
def likeExplore(amount):
    driver.get("https://www.instagram.com/explore/")
    time.sleep(5)
    driver.find_element_by_class_name("_9AhH0").click()
    time.sleep(1.5)
    for i in range(amount):
        #for loop will loop as many times you calld the func with plus 1
        driver.find_element_by_class_name("fr66n").click()
        time.sleep(2)
        driver.find_element_by_partial_link_text("Next").click()
        time.sleep(2)
#this func will like photos and videos in a tag page call it with the tag name and the amount of likes you want to give
def likeTag(tag,amount):
    driver.get("https://www.instagram.com/explore/tags/"+tag+"/")
    time.sleep(5)
    driver.find_element_by_class_name("_9AhH0").click()
    time.sleep(1.5)
    for i in range(amount):
        driver.find_element_by_class_name("fr66n").click()
        time.sleep(2)
        driver.find_element_by_partial_link_text("Next").click()
        time.sleep(2)


driver.get("https://instagram.com")
time.sleep(2)
login(username,password)
likeExplore(10)
likeTag("likeforlike",10)