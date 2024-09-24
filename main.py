import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


url = "https://www.divan.ru/krasnodar/category/divany-i-kresla"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)


# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
divans = driver.find_elements(By.CLASS_NAME, '')



# Выводим вакансии на экран
print(divans)
# Создаём список, в который потом всё будет сохраняться
my_list = []



# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for divan in divans:
   try:
   # Находим элементы внутри вакансий по значению
   # Находим название
     name = divan.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
     # Находим цену
     price = divan.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
     # Находим ссылку с помощью атрибута 'href'
     url = divan.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except:
     print("произошла ошибка при парсинге")
     continue



# Вносим найденную информацию в список
my_list.append([name, price, url])



# Закрываем подключение браузер
driver.quit()



# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
# Используем модуль csv и настраиваем запись данных в виде таблицы
# Создаём объект
writer = csv.writer(file)
# Создаём первый ряд
writer.writerow(['Название', 'Цена', 'Ссылка'])

# Прописываем использование списка как источника для рядов таблицы
writer.writerows(my_list)