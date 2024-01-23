#30.5.1.2 В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы:

import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# 1. Присутствуют все питомцы

def test_all_pets_are_present(test_show_my_pets):
    """Проверка, что на странице "Мои питомцы" присутствуют все питомцы """

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    # Сохранение элементов статистики в переменную "statistic"
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохранение элементов карточек питомцев в переменную "pets"
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Получение количества питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Получение количества карточек питомцев
    number_of_pets = len(pets)

    # Проверка того, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_of_pets

# 2. Хотя бы у половины питомцев есть фото.

def test_half_pets_have_poto(test_show_my_pets):
    """Проверка того, что на странице "Мои питомцы" хотя бы у половины питомцев есть фото"""

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    # Сохранение элементов статистики в переменную "statistic"
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Сохранение элементов с атрибутом "img" в переменную "images"
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Получение количества питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Нахождение половины от количества питомцев
    half = number // 2

    # Нахождение количества питомцев с фотографией
    number_of_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_of_photos += 1

    # Проверка того, что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_of_photos >= half
    print(f'Количество фото: {number_of_photos}')
    print(f'Половина от числа питомцев: {half}')

# 3. У всех питомцев есть имя, возраст и порода.

def test_there_are_a_name_age_and_gender(test_show_my_pets):
    """Проверка, что на странице "Мои питомцы" у всех питомцев есть имя, возраст и порода"""

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохранение элементов с данными о питомцах в переменную "pet_data"
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираются данные из переменной "pet_data"
    # Сохраняются имя, возраст и порода, остальное меняется на пустую строку и разделяется пробелом
    # Находится количество элементов в получившемся списке и сравнивается с ожидаемым результатом
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3

# 4. У всех питомцев разные имена.

def test_all_pets_have_different_names(test_show_my_pets):
    """Проверка, что на странице "Мои питомцы" у всех питомцев разные имена"""

    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохранение элементов с данными о питомцах в переменную "pet_data"
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираются данные из переменной "pet_data"
    # Сохраняются имя, возраст и порода, остальное меняется на пустую строку и разделяется пробелами
    # Выбираются имена и добавляются в список "pets_name"
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Перебираются имена и, если имя повторяется, к счетчику "r" прибавляется единица
    # Если r == 0, то повторяющихся имен нет
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(r)
    print(pets_name)