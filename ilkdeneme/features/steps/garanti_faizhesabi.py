import time
from selenium import webdriver
from behave import given, when, then
from pages.kredi_page import KrediPage

@given('Garanti BBVA web sayfası açılır')
def garanti_acilir(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.garantibbva.com.tr/")
    context.driver.maximize_window()
    context.kredi_page = KrediPage(context.driver)
    time.sleep(3)

@when("Sayfa kredi bölümüne kaydırılır")
def sayfa_kaydirma(context):
    context.kredi_page.scroll_down(900)
    time.sleep(1)

@when("Kredi türlerine sırayla tıklanır ve değerler girilir")
def kredi_turlerine_tikla(context):
    try:
        context.kredi_page.click_İhtiyaç_Kredisi()
        context.kredi_page.click_and_clear_İhtiyaç_Kredisi_Input("20000")
        context.kredi_page.click_vade_option("3 Ay")
        context.kredi_page.write_faiz_oranı()
    except Exception as e:
        print(f"İhtiyaç kredisine tıklanamadı: {e}")
    time.sleep(3)

    try:
        context.kredi_page.click_Konut_Kredisi()
        context.kredi_page.click_and_clear_Konut_Kredisi_Input("1000000")
        context.kredi_page.write_faiz_oranı()
    except Exception as e:
        print(f"Konut kredisine tıklanamadı: {e}")
    time.sleep(3)

    try:
        context.kredi_page.click_Taşıt_Kredisi()
        context.kredi_page.click_and_clear_Taşıt_Kredisi_Input("200000")
        context.kredi_page.write_faiz_oranı()
    except Exception as e:
        print(f"Taşıt kredisine tıklanamadı: {e}")
    time.sleep(3)

@then("Test tamamlandıktan sonra tarayıcı kapatılır")
def tarayici_kapat(context):
    context.driver.quit()
