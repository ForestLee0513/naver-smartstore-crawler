from src import crawler

def get_product_info(url):
    crawled_html = crawler.crawler(url)
    
    try:
        title = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div._1eddO7u4UC > h3").get_text()
        price = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > strong > span._1LY7DqCnwR").get_text()
        price_currency = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > strong > span.won").get_text()
        soldout_element = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._2BQ-WF2QUb")
        image = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._3rXou9cfw2 > div.bd_23RhM > div.bd_1uFKu.bd_2PG3r > img").get("src")

        return {
            "url": url,
            "title": title,
            "price": price,
            "priceCurrency": price_currency,
            "soldout": bool(soldout_element),
            "imageUrl": image,
        }
    except:
        return "Cannot get product."