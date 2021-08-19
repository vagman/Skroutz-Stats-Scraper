from source_file import SourceFile
from config import URLConfiguration
import requests
from bs4 import BeautifulSoup as bs

#TODO: Find purchased products that I haven't reviews yet.

class ReviewMoreProducts():
    

    url_config = URLConfiguration()
    
    response = requests.get(url_config.review_more_products, headers = SourceFile.headers, cookies = SourceFile.cookies)
    soup = bs(response.content, "html.parser")


