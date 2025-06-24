import sys
import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.about_page import AboutPage

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

with open(os.path.join(os.path.dirname(__file__), '..', 'locators', 'locators.yaml'), 'r', encoding='utf-8') as f:
    locators = yaml.safe_load(f)

try:
    driver.get("https://test-stand.gb.ru/login")

    wait = WebDriverWait(driver, 20)

    username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators['login_page']['username_field'])))
    username_input.send_keys("Nastya379")

    password_input = driver.find_element(By.CSS_SELECTOR, locators['login_page']['password_field'])
    password_input.send_keys("2d94b3b2a2")

    login_button = driver.find_element(By.CSS_SELECTOR, locators['login_page']['login_button'])
    login_button.click()

    about_page = AboutPage(driver, locators)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(about_page.about_link_locator))

    about_page.click_about_link()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(about_page.header_locator))

    font_size = about_page.get_header_font_size()
    assert font_size == "32px", f"Размер шрифта {font_size}, ожидается 32px"
    print("Входим на сайт https://test-stand.gb.ru")
    print("Кликаем по ссылке About")
    print("Размер шрифта корректен:", font_size)

finally:
    driver.quit()
