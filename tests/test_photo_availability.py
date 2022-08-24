import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_photo_availability(testing, go_to_my_pets):
   '''Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''
   driver = testing

   WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))

   # Сохраняем в переменную ststistic элементы статистики
   statistic = driver.find_elements(By.XPATH, '//div[@class=".col-sm-4 left"]')

   # Сохраняем в переменную images элементы с атрибутом img
   images = driver.find_elements(By.XPATH, '//th/img')

   print(statistic)
   print(images)

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   print(number)
   number = number[1].split(' ')
   number = int(number[1])

   # Находим половину от количества питомцев
   half = number // 2

   # Находим количество питомцев с фотографией
   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   assert number_а_photos >= half
   print(f'количество фото: {number_а_photos}')
   print(f'Половина от числа питомцев: {half}')

# python -m pytest -v --driver Chrome --driver-path /Users/zaytsev/PycharmProjects/Unit_25.5.1/chromedriver tests/test_photo_availability.py