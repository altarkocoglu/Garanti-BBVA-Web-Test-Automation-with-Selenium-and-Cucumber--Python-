from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MevduatPage(BasePage):
    DAHA_FAZLA_BUTTON = (By.XPATH, "//div[@id='Mevduat-Ürünleri']/button/span[@class='card-grid-show-more-text js-card-grid-show-more-text']")
    TITLE_LOCATORS = (By.XPATH, "//*[@id='Mevduat-Ürünleri']/ul/li/descendant::p[@class='card-title']")

    def click_daha_fazla(self):
        self.click(*self.DAHA_FAZLA_BUTTON)

    def get_titles(self):
        elements = self.driver.find_elements(*self.TITLE_LOCATORS)
        return [elem.text for elem in elements]