from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class GarantiHomePage(BasePage):
    MEVDUAT_LINK = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/nav[2]/ul/li[1]/a")

    def click_mevduat(self):
        self.click(*self.MEVDUAT_LINK)