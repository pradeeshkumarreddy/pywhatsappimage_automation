"""
*******-------install these libraries---------*******
install pandas,numpy and selenium libraries
pip install pandas
pip install numpy
pip install selenium

""" 
from csv import reader
from selenium import webdriver
import argparse
from selenium.common.exceptions import NoSuchElementException
#import webbrowser as web
import time
driver = webdriver.Chrome("enter your file path/chromedriver.exe")#add chromedriver.exe path
driver.get('https://web.whatsapp.com/')
filepath = input("enter image path and press enter: ") #enter the image path after scanning the qrcode

#parser = argparse.ArgumentParser(description='PyWhatsapp Guide')
#parser.add_argument('--chrome_driver_path', action='store', type=str, default=chrome_default_path,help='chromedriver executable path (MAC and Windows path would be different)')

with open('number.csv') as numbers: #to open .csv file
    csv_reader = reader(numbers) # to remove header row
    header = next(csv_reader)#read next to header
    if header != None:
        for contact  in csv_reader :
            num =' '.join(contact) #convert list to string
            #print(num)
            time.sleep(2)
            driver.get("https://web.whatsapp.com/send?phone="+num)
            time.sleep(5)
            try:
                time.sleep(2)
                attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                attachment_box.click()
                time.sleep(1)
                image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(filepath)
                time.sleep(2)
                send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
                send_button.click()
                time.sleep(5)
            except NoSuchElementException as e:
                print("send message exception: ", e)
        print("image sent")
driver.quit()
