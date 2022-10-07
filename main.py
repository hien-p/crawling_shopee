
from asyncio.log import logger
from email.mime import base, image
from lib2to3.pgen2 import driver
from math import prod
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep, time
from tqdm import tqdm
import re

# create object for chrome options
chrome_options = Options()
base_url = 'https://shopee.vn/Qu%E1%BA%A1t-t%E1%BA%A3n-nhi%E1%BB%87t-%C4%91i%E1%BB%87n-tho%E1%BA%A1i-s%C3%B2-l%E1%BA%A1nh-MEMO-DL05-FL05-G6-ch%C6%A1i-PUBG-FF-ROS-Si%C3%AAu-l%E1%BA%A1nh-hi%E1%BB%83n-th%E1%BB%8B-nhi%E1%BB%87t-%C4%91%E1%BB%99-LED-RGB-K%E1%BA%B9p-2-chi%E1%BB%81u-i.80267699.16518590268?xptdk=bbba2c0f-8b03-4f80-ba8e-4df4b16628b9'


chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument("--headless")
# To disable the message, "Chrome is being controlled by automated test software"
chrome_options.add_argument("disable-infobars")

chrome_options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
    })



lines = []
name_of_product = []
with open("list.txt", "r") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

total_count_product = []

for url in tqdm(range(len(lines))):
    browser = webdriver.Chrome(options = chrome_options)
    #try:
   
    browser.get(str(lines[url]))
    while True:
        try: 
            #WebDriverWait(browser, delay)
            sleep(5)
            html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            soup = BeautifulSoup(html, "html.parser")
            
            products_info = soup.findAll('div', class_='OktMMO')
            count = 0
            total_count = []
            if len(products_info) > 2:
                total_sup = re.findall(r'\d+', products_info[-2].text)
            else:
                total_sup = re.findall(r'\d+', products_info[0].text)
                print()
            res = int("".join(map(str, total_sup)))
            print(res)
            total_count_product.append(res)

            break
        except TimeoutException: 
            print('Error')
          
    browser.quit()


print(total_count_product)

# import csv
# # field names 
# fields = ['product', 'totalcount', 'Date']
# with open('GFG', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerow(fields)
#     write.writerows(total_count_product) 


