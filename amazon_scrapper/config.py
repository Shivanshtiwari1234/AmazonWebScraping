"""
Configuration values for the Amazon Web Scraping project.
All constants used across the project should be defined here.
"""

# Base URLs
AMAZON_BASE_URL = "https://www.amazon.in"
AMAZON_SEARCH_URL = "https://www.amazon.in/s"

# Default search query
DEFAULT_QUERY = "laptop"

# Selenium / scraping settings
IMPLICIT_WAIT_TIME = 10
PAGE_LOAD_TIMEOUT = 20

# HTTP headers (used when required)
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# Output settings
OUTPUT_FILE_NAME = "amazon_products.xlsx"
