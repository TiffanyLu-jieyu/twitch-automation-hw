from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"][placeholder="搜尋"]')

    def enter_search_keyword(self, keyword):
        self.input_text(*self.SEARCH_INPUT, keyword)

    def submit_search(self):
        element = self.wait.until(
            lambda d: d.find_element(*self.SEARCH_INPUT)
        )
        element.send_keys(Keys.ENTER)

    def select_streamer(self):
        streamer_locator = (
            By.XPATH,
            '(//a[.//*[contains(text(),"StarCraft II")]])[1]'
        )

        self.click(*streamer_locator)
        
        return
    
    def wait_until_starcraft_loaded(self):
        self.wait.until(EC.url_contains("/directory/category/starcraft-ii"))
    
