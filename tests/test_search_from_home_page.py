import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from constants import (SEARCH_BAR_ICON, SEARCH_INPUT, SEARCH_RESULTS_DIV, GOOD_SEARCH_WORD, SEARCH_PAGE_URL,
                       STORIES_BLOCKS, BAD_SEARCH_WORD, NO_RESULT_BLOCK)
from pages.home_page import MediumHomePage
from pages.search_page import MediumSearchPage


class TestMediumSearchUIHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = MediumHomePage(self.driver)
        self.search_page = MediumSearchPage(self.driver)
        self.driver.get(self.home_page.url)

    def test_user_is_on_home_page(self):
        """
        Validate Page Title - RA-001
        """
        self.assertTrue(self.home_page.is_browser_on_page())

    def test_search_icon_is_present(self):
        """
        Validate search icon - RA-001
        """
        self.assertIsNotNone(self.driver.find_element_by_css_selector(SEARCH_BAR_ICON))

    def test_search_input_is_displayed_on_clicking_search_icon(self):
        """
        Click the search icon on the top right of the page - RA-002
        """
        search_icon = self.driver.find_element_by_css_selector(SEARCH_BAR_ICON)
        search_icon.click()

        self.assertIsNotNone(self.home_page.wait_for_css(SEARCH_INPUT))

    def test_results_page_url_and_search_results_for_good_search_data(self):
        """
        Search from home page with good data - RA-002
        """
        search_icon = self.driver.find_element_by_css_selector(SEARCH_BAR_ICON)
        search_icon.click()

        search_input = self.driver.find_element_by_css_selector(SEARCH_INPUT)
        search_input.send_keys(GOOD_SEARCH_WORD)
        search_input.send_keys(Keys.RETURN)

        self.assertIsNotNone(self.home_page.wait_for_css(SEARCH_RESULTS_DIV))
        self.assertEqual(self.driver.current_url, f'{SEARCH_PAGE_URL}?q={GOOD_SEARCH_WORD}')
        self.assertTrue(len(self.search_page.wait_for_css(STORIES_BLOCKS)))

    def test_search_results_for_bad_search_data(self):
        """
        Search from home page with bad data - RA-003
        """
        search_icon = self.driver.find_element_by_css_selector(SEARCH_BAR_ICON)
        search_icon.click()

        search_input = self.driver.find_element_by_css_selector(SEARCH_INPUT)
        search_input.send_keys(BAD_SEARCH_WORD)
        search_input.send_keys(Keys.RETURN)

        self.assertIsNotNone(self.search_page.wait_for_css(NO_RESULT_BLOCK))

    def tearDown(self):
        """
        Tear down
        """
        self.driver.close()
