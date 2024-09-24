import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

url = "https://www.divan.ru/krasnodar/category/divany-i-kresla"

driver.get(url)

time.sleep(3)

divans = driver.find_elements(By.CLASS_NAME, '_Ud0k')

my_list = []

for divan in divans:
    try:
        name = divan.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        my_list.append([name, price])  # Перенесено внутрь цикла
    except NoSuchElementException:
        print("Произошла ошибка при парсинге")
        continue

driver.quit()

with open("homework.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена'])
    writer.writerows(my_list)  # Перенесено внутрь блока с открытием файла