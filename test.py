from selenium import webdriver 
import time

uid = 'redltd891'
pas = 'karvy123'
 
browser = webdriver.Chrome() 
browser.get('https://mfs.kfintech.com/mfs/distributor/distributor_login.aspx') 

userid = browser.find_element_by_id('txtUserId')
userid.clear()
userid.send_keys(uid)

password  = browser.find_element_by_id('txtPassword')
password.clear()
password.send_keys(pas)

js = "cptcha()"
browser.execute_script(js)

captcha = browser.find_element_by_id('mainCaptcha')
#print(captcha.text)
browser.find_element_by_id('txtcapthca_txtcptcha').send_keys(captcha.text)

browser.implicitly_wait(45)

browser.find_element_by_name("btnSubmit").click()

browser.implicitly_wait(45)

browser.find_element_by_xpath('//*[@title="Mail Back Reports"]').click()

browser.implicitly_wait(45)

browser.find_element_by_xpath('//*[@id="imgReq201"]').click()

browser.implicitly_wait(45)

dateFrom = browser.find_element_by_id('ctl00_MiddleContent_fromdatetodate1_txtDate')#browser.find_element_by_xpath('html/body/form/div/div/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr/td[2]/input[@id="ctl00_MiddleContent_fromdatetodate1_txtDate"][1]')
dateFrom.clear()
dateFrom.send_keys('01/08/2020') 

dateTo = browser.find_element_by_id('ctl00_MiddleContent_fromdatetodate1_txtToDt')#browser.find_element_by_xpath('html/body/form/div/div/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr/td[4]/input[@id="ctl00_MiddleContent_fromdatetodate1_txtToDt"][1]')
dateTo.clear()
dateTo.send_keys('11/08/2020') 

browser.find_element_by_id('ctl00_MiddleContent_FundsSchemes1_selFunds_0').click()

browser.find_element_by_id('chkmailid0').click()

password  = browser.find_element_by_id('ctl00_MiddleContent_ZipPassword1_txtZipPwd')
password.clear()
password.send_keys(pas)

password  = browser.find_element_by_id('ctl00_MiddleContent_ZipPassword1_txtconfirmzippwd')
password.clear()
password.send_keys(pas)

browser.find_element_by_name("ctl00$MiddleContent$BtnReq").click()

time.sleep(5)

obj = browser.switch_to.alert

time.sleep(2)

obj.accept()

browser.close()
browser.quit()
print("test completed")
