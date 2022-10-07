from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from time import sleep, time
from tqdm import tqdm
import re
import datetime
import pandas as pd


def sanpham(names,total,borns) -> list:
    """ return (ten tac gia, link, ngaythangnamsinh, quotes )"""
    result = list()
    for i in range(len(names)):
        result.append({'ten san pham': names[i],
            'total_count': total[i],
             'Date': borns[i]
             })

    return result


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

with open("list.txt", "r") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

total_count_product = []
name_of_product = []
date_list = []
x = datetime.datetime.now()
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
            name_info =  soup.findAll('div', class_='_2rQP1z')
            name_info = [i.find('span') for i in name_info] 
            count = 0
            total_count = []
            
            if len(products_info) > 2:
                total_sup = re.findall(r'\d+', products_info[-2].text)
            else:
                total_sup = re.findall(r'\d+', products_info[0].text)
                print()
            num = int("".join(map(str, total_sup)))
            text = str("".join(map(str, name_info[0].text)))
            print(num, name_info[0].text) 

            total_count_product.append(num)
            name_of_product.append(text)
            date_list.append(x.strftime("%A"))
            break
        except TimeoutException: 
            print('Error')
          
    browser.quit()


# import csv
# # field names 
items = sanpham(name_of_product,total_count_product ,date_list)
path = "sanpham.csv"
# print(items)
df=pd.DataFrame(items)
df.to_csv(path,index=None)
# with open('GFG', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerow(fields)
#     write.writerows(total_count_product) 


