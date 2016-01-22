from selenium import webdriver

userEmail = "sketchy.email@yahoo.com"
userPassword = "realemail123"
print('Who would you like to send an email to?')
toField = input()
print('What is the subject of the email?')
subjectField = input()
print('What do you want the email to say?')
emailContent = input()

browser = webdriver.Firefox()
browser.get('https://www.yahoo.com/')

loginElem = browser.find_element_by_link_text('Mail')
loginElem.click()

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys(userPassword)

signinElem = browser.find_element_by_id('login-signin')
signinElem.click()

composeElem = browser.find_element_by_id('Compose')
composeElem.click()

toElem = browser.find_element_by_id('to-field')
toElem.send_keys(toField)

subjectElem = browser.find_element_by_id('subject-field')
subjectElem.send_keys(subjectField)

contentElem = browser.find_element_by_id('rtetext')
contentElem.send_keys(emailContent)

sendElem = browser.find_element_by_link_text('Send')
sendElem.click()