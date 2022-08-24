from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(testing, go_to_my_pets):
   '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''
   driver = testing

   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]//td[1]')))
   names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]//td[1]')
   cnt = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]').text

   lines = cnt.split()
   print('\n Всего питомцев:', lines[2])
   print(' Статистика пользователя:', len(names))
   assert int(lines[2]) == len(names)
   # Ожидаемый результат - количество питомцев, PASSED


# python -m pytest -v --driver Chrome --driver-path /Users/zaytsev/PycharmProjects/Unit_25.5.1/chromedriver tests/test_all_pets_are_present.py