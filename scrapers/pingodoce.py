from bs4 import BeautifulSoup
from basescraper import BaseScraper

class PingoDoce(BaseScraper):
  def __init__(self):
    urls = [
        "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/ovos-de-galinhas-criadas-no-solo-classe-l-pingo-doce-12-un/",
        "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/espinafres-frescos-pingo-doce-170-g/",
        "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/atum-posta-ao-natural-pingo-doce-120-g/",
        "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/arroz-vaporizado-pingo-doce-1kg/",
    ]
    super().__init__("Pingo Doce", urls)

  def parse_data(self, soup):
    raw_name = soup.find("h1", {"class": "product-details__title"}).get_text().strip()
    raw_price = soup.find("span", {"class": "product-details_price"}).get_text().strip()

    name = raw_name.replace("\n", "").replace("\t", "")
    price = raw_price.replace("\n", "").replace("\t", "").replace("*", "").replace("€", "").replace("UN", "").replace("/", "")

    return {"name": name, "price": price}

if __name__ == '__main__':
  scraper = PingoDoce()
  scraper.start_requests()
  scraper.parse(scraper.parse_data)
  scraper.generate_text_list()
  scraper.store_data()
