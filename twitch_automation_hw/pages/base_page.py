from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, by, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def input_text(self, by, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located((by, locator))
        )
        element.clear()
        element.send_keys(text)

    def is_visible(self, by, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except Exception:
            return False
        
    def scroll_down(self, times):
        for i in range(times):
            self.driver.execute_script(
                "window.scrollBy(0, window.innerHeight * 0.8);" #往下滑80%
            )
            time.sleep(1) #看到在滑動的

    def save_screenshot(self, file_path):
        self.driver.save_screenshot(file_path) 

    def try_click(self, by, locator):
        try:
            element = self.driver.find_element(by, locator)
            element.click()

            return True
        except Exception:
            return False  