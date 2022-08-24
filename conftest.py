import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
   driver = webdriver.Chrome('/Users/zaytsev/PycharmProjects/Unit_25.5.1/chromedriver')

   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   yield driver

   driver.quit()

@pytest.fixture()
def go_to_my_pets(testing):
   driver = testing

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