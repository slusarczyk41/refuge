from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome = webdriver.Chrome(options = chrome_options)

chrome.get('https://refugedugouter.ffcam.fr/GB_resapublic.html')
sleep(5)
iframe = chrome.find_element_by_xpath('//*[@id="if_booking"]')
chrome.switch_to.frame(iframe)

while chrome.find_element_by_xpath('//*[@id="availability"]/div/div/div/span[1]').text != 'August':
    chrome.find_element_by_xpath('//*[@id="availability"]/div/div/a[2]').click()

from twilio.rest import Client

account_sid = 'xxx'
auth_token = 'xxx'
client = Client(account_sid, auth_token)

for day in chrome\
    .find_element_by_xpath('//*[@id="availability"]/div/table/tbody/tr[1]')\
    .find_elements_by_tag_name('td'):
    
    if "DISPO" in day.get_attribute('class'):
        message = client.messages \
            .create(
                 body="O KURWA JEST MIEJSCE "+day.text,
                 from_='+48799448749',
                 to='+48666932065'
             )
    print('----')
    print('day'+ day.text)
    print(day.get_attribute('class'))
