from bs4 import BeautifulSoup
from basescraper import BaseScraper
from utils.parsing import cleanup_sring

class ContinenteScraper(BaseScraper):
  def __init__(self):
    urls = [
        "https://www.continente.pt/produto/infusao-cidreira-saquetas-tetley-4037760.html?cgid=mercearias-cafe-cha",
        "https://www.continente.pt/produto/infusao-camomila-saquetas-tetley-5070838.html?cgid=home",
        "https://www.continente.pt/produto/cafe-moido-torrado-moagem-universal-origins-brasil-int-9-delta-6278018.html?cgid=home",
        "https://www.continente.pt/produto/cafe-moido-torrado-moagem-universal-lote-tradicao-int-11-sical-5722586.html?cgid=mercearias-cafe-cha",
        "https://www.continente.pt/produto/batata-doce-continente-2076703.html?cgid=home"
      ]
    super().__init__("Continente", urls)

  def parse_data(self, soup):
    raw_name = soup.find("h1", {"class": "product-name ct-h3 ct-font--opensans-extrabold mb-0"}).get_text().strip()
    raw_price = soup.find("span", {"class": "ct-price-formatted"}).get_text().strip()

    unwanted_strings = []

    name = cleanup_sring(raw_content=raw_name, list=unwanted_strings)
    price = cleanup_sring(raw_content=raw_price, list=unwanted_strings)

    return {"name": name, "price": price}

if __name__ == '__main__':
  scraper = ContinenteScraper()
  scraper.start_requests()
  scraper.parse(scraper.parse_data)
  scraper.generate_text_list()
  scraper.store_data()
