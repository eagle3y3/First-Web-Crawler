'''
Created on Dec 4, 2018

@author: Lester H
'''
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url = 'https://www.adidas.com/us/men-shoes-new_arrivals'
  
res = requests.get(url, headers = headers)
page_soup = bs(res.text, "html.parser")


containers = page_soup.findAll("div", {"class": "gl-product-card-container show-variation-carousel"})


print(len(containers))
#for each container find shoe model
shoe_colors = []


for container in containers:
    if container.find("div", {'class': 'gl-product-card__reviews-number'}) is not None:
        shoe_model = container.div.div.img["title"]
        review = container.find('div', {'class':'gl-product-card__reviews-number'})
        review = int(review.text)
  
    
#Goes headless in selenium using url
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
shoe_prices = driver.find_elements_by_xpath("//span[@class='gl-price']")
myLength = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span.gl-price"))))
while True:
    driver.execute_script("window.scrollBy(0,400)", "");
    try:
        WebDriverWait(driver,20).until(lambda driver: len(driver.find_elements_by_css_selector("span.gl-price")) > myLength)
        titles = driver.find_elements_by_css_selector("span.gl-price")
        myLength = len(titles) 
    except TimeoutException:
        break

price_list = []
for price in titles:
    price_list.append(price.text)
print(price_list)
    

driver.quit()
