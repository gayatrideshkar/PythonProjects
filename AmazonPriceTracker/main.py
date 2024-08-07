import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

SENDER = "deshkargayatri10@gmail.com"
RECEIVER = "gayatrideshkar8@gmail.com"
PASSWORD = "lpfl fdpi hach ytoz"
BUY_PRICE = 570
product_link = ("https://www.amazon.in/DOT-KEY-Strawberry-Protection-Hyaluronic"
                "/dp/B0CDX9LJM2/ref=sr_1_1_sspa")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(product_link, headers=header)

soup = BeautifulSoup(response.content, "lxml")
title = soup.find(id="productTitle").get_text().strip()
print(title)
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
print(price_without_currency)

if price_as_float < BUY_PRICE:

    message = f"{title} is now at price {price}."
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(SENDER, PASSWORD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECEIVER,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_link}".encode("utf-8")
        )
