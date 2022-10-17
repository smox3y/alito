from selenium import webdriver
import scrapy,time,json,csv

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

options.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=options)

csv_columns = ['link', 'Likes', 'shares', 'comments', 'Play_Count']
csvfile = open('Video_Data.csv', 'w', newline='', encoding="utf-8")
writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
writer.writeheader()
file = open('VideoLinks.txt','r')
filedata = [v.strip() for v in file.read().split('\n')]
for link in filedata:
    driver.get(link)
    res = scrapy.Selector(text=driver.page_source)
    data = json.loads(driver.find_element_by_css_selector('#sigi-persisted-data').get_attribute('innerHTML').split(']=')[1].split(';window')[0])
    item = dict()
    try:
        item['link'] = link
        item['Likes'] = data['ItemModule'][[v for v in data['ItemModule'].keys()][0]]['stats']['diggCount']
        item['shares'] = data['ItemModule'][[v for v in data['ItemModule'].keys()][0]]['stats']['shareCount']
        item['comments'] = data['ItemModule'][[v for v in data['ItemModule'].keys()][0]]['stats']['commentCount']
        item['Play_Count'] = data['ItemModule'][[v for v in data['ItemModule'].keys()][0]]['stats']['playCount']
        writer.writerow(item)
        csvfile.flush()
    except:
        print(f'video currently unavailable for  --> {link}')
driver.quit()
