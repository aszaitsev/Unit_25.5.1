from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_show_pet_friends(testing):
   '''Проверка карточек питомцев'''
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

   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

   images = driver.find_elements(By.XPATH, '//th/img')
   names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]//td[1]')
   descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('currentSrc') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

# python -m pytest -v --driver Chrome --driver-path /Users/zaytsev/PycharmProjects/Unit_25.5.1/chromedriver tests/test_show_pet_friends.py