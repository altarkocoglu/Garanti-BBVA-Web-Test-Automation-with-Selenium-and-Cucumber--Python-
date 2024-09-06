from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))


    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def get_title(self):
        return self.driver.title

    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")



    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        self.driver.get(url)

