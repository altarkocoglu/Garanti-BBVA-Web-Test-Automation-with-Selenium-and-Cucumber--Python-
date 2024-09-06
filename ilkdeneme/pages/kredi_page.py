from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class KrediPage(BasePage):
    İhtiyaç_Kredisi = (By.XPATH, "//div/ul/li[@data-apply-url='/content/public-website/tr/kendim-icin/krediler/bireysel-ihtiyac-kredisi/kredi-basvurusu']")
    Konut_Kredisi = (By.XPATH, "//div/ul/li[@data-apply-url='/content/public-website/tr/kendim-icin/krediler/konut-kredisi/konut-kredisi-basvurusu']")
    Taşıt_Kredisi = (By.XPATH, "//div/ul/li[@data-apply-url='/content/public-website/tr/kendim-icin/krediler/tasit-kredisi/tasit-arac-kredisi-basvurusu']")

    İhtiyaç_Kredisi_Input = (By.XPATH, "//div[@data-credit-type='PERSONAL_GENERAL']/descendant::input[@id='js-credit__input-PERSONAL_GENERAL']")
    Konut_Kredisi_Input = (By.XPATH, "//div[@data-credit-type='PERSONAL_MORTGAGE']/descendant::input[@id='js-credit__input-PERSONAL_MORTGAGE']")
    Taşıt_Kredisi_Input = (By.XPATH, "//div[@data-credit-type='PERSONAL_AUTO']/descendant::input[@id='js-credit__input-PERSONAL_AUTO']")

    Faiz_Oranı = (By.XPATH, "//p/strong[@class='js-calc__rate']")


    def click_İhtiyaç_Kredisi(self):
        self.click(*self.İhtiyaç_Kredisi)

    def click_Konut_Kredisi(self):
        self.click(*self.Konut_Kredisi)

    def click_Taşıt_Kredisi(self):
        self.click(*self.Taşıt_Kredisi)

    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def clear_and_enter_text(self, input_locator, text):
        element = self.driver.find_element(*input_locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_and_clear_İhtiyaç_Kredisi_Input(self, text):
        self.clear_and_enter_text(self.İhtiyaç_Kredisi_Input, text)

    def click_and_clear_Konut_Kredisi_Input(self, text):
        self.clear_and_enter_text(self.Konut_Kredisi_Input, text)

    def click_and_clear_Taşıt_Kredisi_Input(self, text):
        self.clear_and_enter_text(self.Taşıt_Kredisi_Input, text)

    def write_faiz_oranı(self):
        faiz_write_element = self.find_element(*self.Faiz_Oranı)
        faiz_write_text = faiz_write_element.text
        print(f"Bulunan sonuç sayısı: {faiz_write_text}")

    def click_vade_option(self, vade):
        vade_options = {
            "3 Ay": "//div//button[@data-value='3']",
            "6 Ay": "//div//button[@data-value='6']",
            "9 Ay": "//div//button[@data-value='9']",
            "12 Ay": "//div//button[@data-value='12']",
            "18 Ay": "//div/ul[@class='js-Dropdown-list is-open']/li[@data-index='0']",
            "24 Ay": "//div/ul[@class='js-Dropdown-list is-open']/li[@data-index='1']",
            "30 Ay": "//div/ul[@class='js-Dropdown-list is-open']/li[@data-index='2']",
            "36 Ay": "//div/ul[@class='js-Dropdown-list is-open']/li[@data-index='3']"
        }

        if vade in vade_options:
            self.click(By.XPATH, vade_options[vade])
        else:
            print(f"Geçersiz vade seçeneği: {vade}")
