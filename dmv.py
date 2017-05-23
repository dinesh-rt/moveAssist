
from selenium import webdriver
import selenium 
url="https://www.dmv.ca.gov/portal/dmv/detail/online/coa/welcome"
br = webdriver.Firefox()
br.get(url)
startBtn = br.find_element_by_class_name('btn3')
startBtn.click()

#2nd page 
username = br.find_element_by_id('username')
username.send_keys("xxxxxx")
password = br.find_element_by_id('password')
password.send_keys("xxxxxx")
buttons = br.find_element_by_tag_name('button')
print(buttons.text)
buttons.click()

 #3rd page
 #cahnge both  id & vehicle or id or vehicle address 
 #also can check update status. 
option = br.find_element_by_name('transTypeCode')
option.send_keys(['BOTH']) # ['BOTH', 'DL', 'VR']
form = br.find_element_by_id('AuthenticateFormBean')
form.submit()

#4th page 


