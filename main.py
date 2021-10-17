import csv
from selenium import webdriver
import urllib.request

# скачать драйвер для хрома https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    # считываем ссылки из вайла с массив
    urls = []  # массив ссылок для ссылок
    with open('urls.csv', newline='') as file:  # открываем файл
        reader = csv.reader(file, delimiter=' ', quotechar='|')  # читаем файл
        for row in reader:  # идем построчно
            urls.append(row[0])  # добавляем ссылку в массив

    # подключаемся к браузеру
    driver = webdriver.Chrome(executable_path="/Users/vladimir/PycharmProjects/download_images/chromedriver")

    # ищем ссылки для скачивания файлов
    downloads_urls = []  # массив для ссылок на скачивание фото
    for url in urls:  # идем по массиву ссылок
        driver.get(url)  # переходим по ссылке
        arrow = driver.find_element(By.ID, "popover-download-button")  # ищем галочку выбора размера фото
        arrow.click()  # нажимаем
        tabs = driver.find_elements(By.TAG_NAME, "li")  # ищем все размеры фото
        li = None
        for tab in tabs:
            if "small" in tab.text.lower():  # выбираем те на которых написано маленькая
                li = tab
        if li is not None:
            downloads_url = li.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")  # достаем ссылку на скачивание
            downloads_urls.append(downloads_url)  # добавляем ссылку на скачивание в массив

    driver.close()  # закрываем браузер

    # скачиваем файл
    i = 1
    for downloads_url in downloads_urls:  # идем по ссылкам для скачивания
        i += 1
        urllib.request.urlretrieve(downloads_url, f"images/{i}.jpg")

    print(f"загружено {i} файлов")
