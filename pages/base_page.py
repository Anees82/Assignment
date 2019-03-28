from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    title = ''
    WAIT_SECONDS = 5

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_page(self):
        """
        Is browser on home page
        """
        self.wait_for_ajax()
        return self.title in self.driver.title

    def wait_for_ajax(self):
        """
        Wait for jQuery to be loaded and for all ajax requests to finish
        """
        return self.driver.execute_script(
            "return typeof(jQuery)!='undefined' && jQuery.active==0")

    def wait_for_css(self, wait_selector):
        """
        Wait for css selector (wait_selector) to be present in DOM
        """
        return WebDriverWait(self.driver, self.WAIT_SECONDS).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, wait_selector))
        )
