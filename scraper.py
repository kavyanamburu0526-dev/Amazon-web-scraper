import requests
from bs4 import BeautifulSoup
def scrape_amazon(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/142.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        return {
            "error": f"Amazon returned status code {response.status_code}"
        }
    soup = BeautifulSoup(response.text, "html.parser")
    # Product name
    title = soup.select_one("#productTitle")
    # Price
    price = (
        soup.select_one(".a-price .a-offscreen")
        or soup.select_one(".a-price-whole")
    )
    # Rating
    rating = soup.select_one(
        "#acrPopover .a-size-base"
    )
    # Reviews
    reviews = soup.select_one(
        "#acrCustomerReviewText"
    )
    # Availability
    availability = soup.select_one(
        "#availability span"
    )
    product = {
        "title": title.get_text(strip=True) if title else "Not found",
        "price": price.get_text(strip=True) if price else "Not found",
        "rating": rating.get_text(strip=True) if rating else "Not found",
        "reviews": reviews.get_text(strip=True) if reviews else "Not found",
        "availability": (
            availability.get_text(strip=True)
            if availability else "Not found"
        ),
        "url": url
    }
    return product