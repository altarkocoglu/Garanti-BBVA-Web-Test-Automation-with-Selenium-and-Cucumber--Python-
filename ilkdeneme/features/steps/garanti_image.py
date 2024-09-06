import requests
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.garanti_home_page import GarantiHomePage
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
import time


@given('Garanti BBVA ana sayfası açılır')
def garanti_acilir(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.ruud.com/mobile/")
    context.driver.maximize_window()
    context.home_page = GarantiHomePage(context.driver)
    context.main_page = MainPage(context)
    time.sleep(1)


@when('Görsel tespiti')
def görüntü_tespiti(context):
    context.images = WebDriverWait(context.driver, 5).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )


@then('Kırık görsel bulunamadı')
def görüntü_kontrolü(context):
    broken_images = []
    checked_images = set()  # Kontrol edilen görsellerin URL'lerini tutmak için bir set

    for img in context.images:
        img_url = img.get_attribute("src")
        print(img_url)

        if img_url is None:
            print("Image source is None, skipping this image.")
            continue

        # Eğer URL zaten kontrol edildiyse, devam et
        if img_url in checked_images:
            print(f"Duplicate image found: {img_url}, skipping.")
            continue

        # URL'yi kontrol edilenler listesine ekle
        checked_images.add(img_url)

        # HTTP isteği yap ve sonucu kontrol et
        response = requests.get(img_url)
        if response.status_code != 200:
            broken_images.append(img_url)

    assert len(broken_images) == 0, f"Broken images found: {broken_images}"