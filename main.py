"""
Main entry point for the Amazon Web Scraping project.

This script performs:
1. Amazon product search
2. HTML parsing
3. Exporting results to an Excel file

Run using:
    python main.py
"""

from amazon_scraper.search import search_amazon
from amazon_scraper.exporter import save_to_excel
from amazon_scraper.config import DEFAULT_QUERY


def main():
    # Step 1: Perform product search
    products = search_amazon(DEFAULT_QUERY)

    # Step 2: Export results
    if products:
        save_to_excel(products)
        print(f"Saved {len(products)} products to Excel.")
    else:
        print("No products found.")


if __name__ == "__main__":
    main()
