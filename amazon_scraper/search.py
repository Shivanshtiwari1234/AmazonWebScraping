"""
Amazon search automation using Selenium.

This module is responsible for:
- Opening Amazon
- Performing a product search
- Returning raw HTML for further processing
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from amazon_scraper.driver import get_chrome_driver
from amazon_scraper.config import AMAZON_BASE_URL, DEFAULT_QUERY


def search_amazon(query: str = DEFAULT_QUERY) -> str:
    """
    Perform a search on Amazon India and return the page HTML.

    Args:
        query (str): Product search query

    Returns:
        str: HTML source of the search results page
    """
    driver = get_chrome_driver()

    try:
        # Step 1: Open Amazon
        driver.get(AMAZON_BASE_URL)

        # Step 2: Locate search box
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")

        # Step 3: Enter query and submit
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Step 4: Return page HTML
        return driver.page_source

    finally:
        driver.quit()
