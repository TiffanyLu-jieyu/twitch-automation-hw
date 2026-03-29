from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class HomePage(BasePage):
    URL = "https://www.twitch.tv/"

    BROWSE_LINK = (By.XPATH, '//a[normalize-space()="瀏覽"]')

    def open(self):
        self.open_url(self.URL)

    def click_browse(self):
        self.click(*self.BROWSE_LINK)