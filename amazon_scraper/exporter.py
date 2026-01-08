import csv
from openpyxl import Workbook
from typing import List, Dict


def save_to_csv(products: List[Dict], filename: str = "products.csv"):
    """Save products to a CSV file."""
    if not products:
        print("No products to save.")
        return

    keys = products[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)

    print(f"Saved {len(products)} products to {filename}")


def save_to_excel(products: List[Dict], filename: str = "products.xlsx"):
    """Save products to an Excel file."""
    if not products:
        print("No products to save.")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    # Write header
    headers = list(products[0].keys())
    ws.append(headers)

    # Write data
    for p in products:
        ws.append([p.get(h) for h in headers])

    wb.save(filename)
    print(f"Saved {len(products)} products to {filename}")
