import time, json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

csv_columns = ['Influencer','link', 'Follower count','Following count', 'Like count', 'video 1', 'video 2', 'video 3',
               'Average Views','Multiplier']
csvfile = open('Account_Data.csv', 'w', newline='', encoding="utf-8")
writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
writer.writeheader()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

options.add_argument('--disable-notifications')

def style_num_to_float(style_num):
    if 'K' in style_num:
        return float(style_num.replace('K', '')) * 1000
    elif 'M' in style_num:
        return float(style_num.replace('M', '')) * 1000000
    else:
        return style_num

def fetch_e2e(data_id):
    identifier = '[data-e2e="' + data_id + '"]'
    resp_list = driver.find_elements(by=By.CSS_SELECTOR, value=identifier)
    output_list = []
    for i in range(len(resp_list)):
        output_list.append(int(style_num_to_float(resp_list[i].get_attribute('innerHTML'))))
    return output_list

def get_data():
    input_file = open('AccountLinks.txt', 'r')
    file_data = input_file.read().split('\n')
    for link in file_data:
        item = dict()
        driver.get(link)
        
        item['Influencer'] = link.replace('https://www.tiktok.com/@', '')
        item['link'] = driver.current_url

        item['video 1'] = fetch_e2e('video-views')[0]
        item['video 2'] = fetch_e2e('video-views')[1]
        item['video 3'] = fetch_e2e('video-views')[2]

        item['Average Views'] = int((item['video 1'] + item['video 2'] + item['video 3']) / 3)

        item['Following count'] = fetch_e2e('following-count')[0]
        item['Follower count'] = fetch_e2e('followers-count')[0]
        item['Like count'] = fetch_e2e('likes-count')[0]
        item['Multiplier']=''

        writer.writerow(item)

if __name__ == '__main__':
    driver = webdriver.Chrome(options=options)
    get_data()
    driver.quit()
