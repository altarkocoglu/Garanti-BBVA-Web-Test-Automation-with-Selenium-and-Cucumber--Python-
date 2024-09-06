from behave import given, when, then
from selenium import webdriver
from pages.garanti_home_page import GarantiHomePage
from pages.mevduat_page import MevduatPage
import time

@given("Garanti BBVA resmi web sayfası açılır")
def garanti_acilir(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.garantibbva.com.tr/")
    context.driver.maximize_window()
    context.home_page = GarantiHomePage(context.driver)
    context.mevduat_page = MevduatPage(context.driver)
    time.sleep(1)


@when("Mevduat'a tıklanır")
def mevduat_acilir(context):
    context.home_page.click_mevduat()
    time.sleep(1)


@when("Mevduat ürünlerinin bulunduğu sayfa açılır")
def mevduat_hesabi(context):
    assert "Mevduat | Garanti BBVA" == context.mevduat_page.get_title()
    time.sleep(1)


@when("Sayfa aşağıya kaydırılır")
def sayfa_kaydirma(context):
    context.mevduat_page.scroll_down(2000)
    time.sleep(1)


@when("Daha Fazla Gör'e tıklanır")
def daha_fazla(context):
    context.mevduat_page.click_daha_fazla()
    time.sleep(1)


@when('sayfadaki başlıklar kontrol edilir')
def step_impl(context):
    context.expected_titles = [
        "e-Vadeli Hesap",
        "Vadeli TL Hesabı",
        "Vadeli Döviz Hesabı",
        "Biriktirdiğini Ödeyen Mevduat",
        "Döviz/Altın Dönüşümlü Kur Korumalı TL Vadeli Mevduat",
        "Vadesiz TL Hesabı",
        "Vadesiz Döviz Hesabı",
        "Elma Mevduat Hesabı",
        "Yuvam Hesabı"
    ]
    context.actual_titles = context.mevduat_page.get_titles()
    print(context.actual_titles)
    time.sleep(1)


@then('başlıklar hatasız olmalıdır')
def step_impl(context):
    assert context.expected_titles == context.actual_titles, f"Beklenen: {context.expected_titles}, Gerçekleşen: {context.actual_titles}"
    context.driver.quit()
