from bs4 import BeautifulSoup


def parse_products(html: str) -> list[dict]:
    """
    Parse Amazon HTML for products.
    Filters out Sponsored ads and duplicates (by ASIN).
    """
    soup = BeautifulSoup(html, "html.parser")
    products = []
    seen_asins = set()

    for item in soup.select("div[data-asin]"):
        asin = item.get("data-asin", "").strip()
        if not asin or asin in seen_asins:
            continue  # skip empty or duplicate ASIN

        # find all links inside the card
        links = item.find_all("a", href=True)

        product_link = None
        for a in links:
            href = a["href"]

            # ❌ skip ads
            if "Sponsored" in (a.get("aria-label") or ""):
                continue
            if href.startswith("http") and "/dp/" not in href and "/gp/" not in href:
                continue
            if "/dp/" in href or "/gp/" in href:
                product_link = a
                break

        if not product_link:
            continue  # no valid link

        title_span = product_link.find("span")
        title = title_span.get_text(strip=True) if title_span else None
        link = "https://www.amazon.in" + product_link["href"]

        price_tag = item.select_one("span.a-price span.a-offscreen")
        price = price_tag.get_text(strip=True) if price_tag else None

        products.append({
            "asin": asin,
            "title": title,
            "price": price,
            "link": link,
        })

        seen_asins.add(asin)  # mark ASIN as seen

    return products
