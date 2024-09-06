from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    Search_Button = (By.XPATH, "//div/button[@class='btn-link mainbar__search js-mainbar__search']")
    Search_Input = (By.XPATH, "//div/form/input[@type='text']")
    Search_Write = (By.XPATH, "//p/span[@class='found_count']")


    def click_search(self):
        self.click(*self.Search_Button)

    def send_keys_to_search(self, text):
        search_input = self.find_element(*self.Search_Input)
        search_input.send_keys(text + Keys.ENTER)


    def write_search(self):
        search_write_element = self.find_element(*self.Search_Write)
        search_write_text = search_write_element.text
        print(f"Bulunan sonuç sayısı: {search_write_text}")
