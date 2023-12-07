from src import crawler

def get_product_info(url):
    crawled_html = crawler.crawler(url)
    
    try:
        title = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div._1eddO7u4UC > h3")
        price = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > strong > span._1LY7DqCnwR")
        soldout_element = crawled_html.select_one("#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._2BQ-WF2QUb")
        print(title, price, bool(soldout_element))
        
        return "foo"
    except:
        return "Cannot get product."