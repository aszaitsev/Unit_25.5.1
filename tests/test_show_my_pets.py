from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_show_my_pets(testing):
   '''Проверяем что мы оказались на странице "Мои питомцы"'''
   driver = testing
   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys(valid_email)

   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys(valid_password)

   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   # Нажимаем на ссылку "Мои питомцы"
   driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

   # Проверяем что мы оказались на странице "Мои питомцы"
   assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

# python -m pytest -v --driver Chrome --driver-path /Users/zaytsev/PycharmProjects/Unit_25.5.1/chromedriver tests/test_show_my_pets.py