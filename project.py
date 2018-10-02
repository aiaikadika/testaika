from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

#command Format : python test.py File1 File2
username = sys.argv[1]
password = sys.argv[2]

def LoginGithub(username,password):
    buttonSignup = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/a[2]")
    buttonSignup[0].click()
    fieldLogin = driver.find_element_by_id("login_field")
    fieldLogin.send_keys(username)
    fieldPassword = driver.find_element_by_id("password")
    fieldPassword.send_keys(password)
    fieldPassword.send_keys(Keys.ENTER)
    print "Login github : PASSED"
    print "Go to gist page : PASSED"

def AddNewGist():
    buttonAddNewGist = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/ul/li[1]/a')
    buttonAddNewGist.click()
    fieldGistName = driver.find_element_by_name("gist[contents][][name]")
    fieldGistName.send_keys('aikacoba.sql')
    fieldContentGist = driver.find_element_by_class_name('CodeMirror-code')
    fieldContentGist.send_keys('select * from ws_user')
    buttonPublicGist = driver.find_element_by_name("gist[public]")
    buttonPublicGist.click()
    print "Add new gist : PASSED"

def EditGist():
    buttonEditGist = driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[1]/a')
    buttonEditGist.click()
    fieldContentGist = driver.find_element_by_class_name('CodeMirror-code')
    fieldContentGist.send_keys('Edited')
    elefieldContentGistm9.send_keys(Keys.ENTER)
    buttonPublicGist = driver.find_element_by_xpath("//button[contains(.,'Update public gist')]")
    buttonPublicGist.click()
    print "Edit gist : PASSED"

def DeleteGist():
    buttonDelete = driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[2]/form/button')
    buttonDelete.click()
    popUp = driver.switch_to.alert
    popUp.accept()
    print "Delete gist : PASSED"

def SeeAllGist():
    buttonSeeAllGist = driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[2]/nav/a')
    if buttonSeeAllGist:
        print "See all gist : PASSED"

driver = webdriver.Firefox()
driver.get("https://gist.github.com")
LoginGithub(username,password)
AddNewGist()
#EditGist()
#DeleteGist()
#SeeAllGist()
#driver.close()