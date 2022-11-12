import os
import requests
from bs4 import BeautifulSoup
import re
import cv2

categories = ["cars", "motorbikes", "plantmachinery"]

img_url_records = set()

for category in categories:
    cnt = 0
    i = 0
    while cnt < 1000:

        webpage_link = f"https://www.donedeal.ie/{category}?start={i*30}"
        i += 1
        response = requests.get(webpage_link)
        
        soup = BeautifulSoup(response.text, "html.parser")

        ul_items = soup.find_all('ul', class_=re.compile('Listings__List.*'))
        
        li_items = ul_items[0].find_all('li', class_=re.compile('Listings__.*'))
        
        for li_item in li_items:
            try: 
                img_url = li_item.find("img")['src']
                # Download the image from the url
                if img_url not in img_url_records:
                    img_url_records.add(img_url)
                    img_path = f"./train_types/{category}/{category}_{cnt}.jpg"
                    os.system(f"wget {img_url} -O {img_path}")
                    img = cv2.imread(img_path)
                    height, width, channels = img.shape
                    if height < 100:
                        continue
                    cnt += 1
                    print(f"Count: {category} -> {cnt}")
                    if cnt >= 1000:
                        break
            except: 
                pass

        a = 1
