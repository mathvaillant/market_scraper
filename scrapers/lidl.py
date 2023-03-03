from bs4 import BeautifulSoup
from basescraper import BaseScraper
from utils.parsing import cleanup_sring

class LidlScraper(BaseScraper):
  def __init__(self):
    urls = [
      "https://www.lidl.pt/p/promocoes-de-frutas-e-legumes/batata-doce-polpa-amarela-laranja-nacional/p139679"
    ]
    super().__init__("Lidl", urls)

  def parse_data(self, soup):
    raw_name = soup.find("h1", {"class": "attributebox__headline attributebox__headline--h1"}).get_text().strip()
    raw_price = soup.find("span", {"class": "pricebox__price"}).get_text().strip()

    unwanted_strings = []

    name = cleanup_sring(raw_content=raw_name, list=unwanted_strings)
    price = cleanup_sring(raw_content=raw_price, list=unwanted_strings)

    return {"name": name, "price": price}

if __name__ == '__main__':
  scraper = LidlScraper()
  scraper.start_requests()
  scraper.parse(scraper.parse_data)
  scraper.generate_text_list()
  scraper.store_data()
