from bs4 import BeautifulSoup
from basescraper import BaseScraper
from utils.parsing import cleanup_sring

class AldiScraper(BaseScraper):
  def __init__(self):
    urls = [
        "https://www.aldi.pt/produtos/as-nossas-marcas/gut-bio/tofu-biologico-1816-1-0.article.html",
        "https://www.aldi.pt/produtos/as-nossas-marcas/gut-bio/tostas-bio-milho-arroz-3044-1-0.article.html",
        "https://www.aldi.pt/produtos/as-nossas-marcas/tesouros_do_mar/atum-posta-ao-natural-1994-1-0.article.html"
    ]
    super().__init__("Aldi", urls)

  def parse_data(self, soup):
    raw_name = soup.find("div", {"class": "mod-article-intro__header-headline"}).find("h1").get_text().strip()
    raw_price = soup.find("span", {"class": "price__wrapper"}).get_text().strip()

    unwanted_strings = ["\n", "\t", "*"]

    name = cleanup_sring(raw_content=raw_name, list=unwanted_strings)
    price = cleanup_sring(raw_content=raw_price, list=unwanted_strings)

    return {"name": name, "price": price}

if __name__ == '__main__':
  scraper = AldiScraper()
  scraper.start_requests()
  scraper.parse(scraper.parse_data)
  scraper.generate_text_list()
  scraper.store_data()


