import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(testing, go_to_my_pets):
   '''Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена'''
   driver = testing

   WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]//td[1]')))
   # Сохраняем в переменную names элементы с данными о питомцах
   names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]//td[1]')

   # Перебираем данные из names и разделяем по пробелу.Выбераем имена и добавляем их в список pets_name.
   pets_name = []
   for i in range(len(names)):
      data_pet = names[i].text.replace('\n', '').replace('×', '')
      split_names = data_pet.split(' ')
      pets_name.append(split_names[0])

   # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
   # Проверяем, если r == 0 то повторяющихся имен нет.
   r = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         r += 1
   assert r == 0
   print('\n', 'Совпадений:', r)
   print(pets_name)

# python -m pytest -v --driver Chrome --driver-path /Users/zaytsev/PycharmProjects/Unit_25.5.1/chromedriver tests/test_all_pets_have_different_names.py