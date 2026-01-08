"""
Amazon search automation using Selenium.

This module:
- Opens Amazon India
- Performs a search
- Waits for results to load
- Returns the final page HTML
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from amazon_scraper.driver import get_chrome_driver
from amazon_scraper.config import AMAZON_BASE_URL, DEFAULT_QUERY


def search_amazon(query: str = DEFAULT_QUERY) -> str:
    driver = get_chrome_driver()

    try:
        # Open Amazon
        driver.get(AMAZON_BASE_URL)

        # Search
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # ✅ WAIT until search results are present
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.s-result-item[data-component-type='s-search-result']")
            )
        )

        return driver.page_source

    finally:
        driver.quit()
