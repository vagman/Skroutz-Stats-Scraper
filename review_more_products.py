from source_file import SourceFile
from config import URLConfiguration
import requests
from bs4 import BeautifulSoup as bs

#TODO: Find purchased products that I haven't reviews yet.

class ReviewMoreProducts():

    url_config = URLConfiguration()

    response = requests.get(url_config.review_more_products, headers = SourceFile.headers, cookies = SourceFile.cookies)
    soup = bs(response.content, "lxml")

    # Find all the <a> tags which are not reviewed prodcts
    not_reviewed_products = soup.find_all("a", {"class": "sku_title"})

    # Save as list
    to_be_reviewed_products = []
    for product in not_reviewed_products:
        to_be_reviewed_products.append(product.text)

    # Display
    def print_products(prod: list):
        for p in prod:
            print("\t" +  p)

            
    print("\nThe products that you bought but you haven't reviewed yet are:")
    print_products(to_be_reviewed_products)