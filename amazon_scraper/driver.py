"""
Chrome WebDriver setup for the Amazon Web Scraping project.

This module centralizes all Selenium driver configuration and relies on
Selenium Manager to automatically resolve the correct ChromeDriver version.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from amazon_scraper.config import (
    IMPLICIT_WAIT_TIME,
    PAGE_LOAD_TIMEOUT,
    USER_AGENT,
)


def get_chrome_driver(headless: bool = False) -> webdriver.Chrome:
    """
    Create and return a configured Chrome WebDriver instance.

    Args:
        headless (bool): Run Chrome in headless mode if True.

    Returns:
        webdriver.Chrome: Configured Chrome WebDriver
    """
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument(f"user-agent={USER_AGENT}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")

    # Selenium Manager automatically handles ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

    return driver
