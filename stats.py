from source_file import SourceFile
from config import URLConfiguration
import requests
from sys import exit
from bs4 import BeautifulSoup as bs

class PersonalStats():

    url_config = URLConfiguration()

    try:
        response = requests.get(url_config.personal_statistics, cookies = SourceFile.cookies)
        soup = bs(response.content, "lxml")

        # Select <div> element that consists of the <ul> of the stats
        personal_stats_ul = soup.find_all("div", {"class": "info-box cf"})

        # Select all four <li><span>...</span></li>
        for li in personal_stats_ul:
            span_info = li.find_all("span")

        # Get my personal statistics from ../account/settings/profile
        product_reviews = int(bs.get_text(span_info[0]))
        upvotes = int(bs.get_text(span_info[1]))
        shop_reviews = int(bs.get_text(span_info[2]))
        comments = int(bs.get_text(span_info[3]))

        print("Product reviews: {}\nUpvotes: {}\nShop reviews: {}\nComments: {}\n".format(product_reviews, upvotes, shop_reviews, comments))
    except NameError:
        print("You haven't specified _helmet_couch cookie element in SourceFile class. Read more at https://github.com/vagman/Skroutz-Stats-Scraper/blob/main/README.md")
        exit()
    # Product reviews: 130
    # Upvotes: 509
    # Shop reviews: 23
    # Comments: 884