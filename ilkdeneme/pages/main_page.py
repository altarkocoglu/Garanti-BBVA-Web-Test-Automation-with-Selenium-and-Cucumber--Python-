from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    IMAGE_LOCATOR = (By.TAG_NAME, "img")

    def get_all_images(self):
        return self.find_elements(*self.IMAGE_LOCATOR)
