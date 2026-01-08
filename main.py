from amazon_scraper.search import search_amazon
from amazon_scraper.parser import parse_products
from amazon_scraper.exporter import save_to_csv, save_to_excel


def main():
    # 1️⃣ Search Amazon for a query
    query = "laptop"
    print(f"Searching Amazon for: {query}")
    html = search_amazon(query)

    # 2️⃣ Parse HTML to extract products
    products = parse_products(html)
    print(f"Products found: {len(products)}")

    if not products:
        print("No products found. Exiting.")
        return

    # 3️⃣ Export results
    save_to_csv(products, filename="products.csv")
    save_to_excel(products, filename="products.xlsx")
    print("Export complete.")


if __name__ == "__main__":
    main()
