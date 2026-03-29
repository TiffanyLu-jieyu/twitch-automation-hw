from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class StreamerPage(BasePage):

    CLOSE_POPUP = (By.XPATH, '//button[@aria-label="Close"]')


    def dismiss_popup(self):
        self.try_click(*self.CLOSE_POPUP)

        
    def wait_until_loaded(self):
        self.dismiss_popup()
        try:
            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )
            return
        except:
            pass



