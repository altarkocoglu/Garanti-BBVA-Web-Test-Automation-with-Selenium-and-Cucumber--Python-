from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.garanti_home_page import GarantiHomePage
from pages.search_page import SearchPage
import time


@given("Garanti BBVA resmi web sayfası arama için açılır")
def garanti_acilir(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.garantibbva.com.tr/")
    context.driver.maximize_window()
    context.home_page = GarantiHomePage(context.driver)
    context.search_page = SearchPage(context.driver)
    time.sleep(1)


@when("Arama kutusuna basılır")
def arama_kutusu(context):
    context.search_page.click_search()
    time.sleep(1)


@then("Arama kutusuna 'mevduat' yazılır ve Enter'a basılır")
def arama_yap(context):
    context.search_page.send_keys_to_search("altın")
    time.sleep(2)


@then("Arama sonrası kaç sonuç bulundu")
def arama_sonu(context):
    context.search_page.write_search()
    time.sleep(2)
