import requests
from bs4 import BeautifulSoup
from flask import Response

def crawler(url: str):
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,'referer':'https://www.google.com/'}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        return soup
    else:
        return response.status_code

def smartstore_product_info_parser(parsed_html, url: str):
    try:
        title = parsed_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div._1eddO7u4UC > h3").get_text()
        price = parsed_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > strong > span._1LY7DqCnwR").get_text()
        price_currency = parsed_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > strong > span.won").get_text()
        soldout_element = parsed_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._2BQ-WF2QUb")
        image = parsed_html.select_one("#content > div > div._2-I30XS1lA > div._3rXou9cfw2 > div.bd_23RhM > div.bd_1uFKu.bd_2PG3r > img").get("src")

        return {
            "url": url,
            "title": title,
            "price": price,
            "priceCurrency": price_currency,
            "soldout": bool(soldout_element),
            "imageUrl": image,
        }
    except:
        return Response("Cannot get product.", status=400)
