import os
import requests
from bs4 import BeautifulSoup


class BaseScraper:
  def __init__(self, market_name, urls):
    self.market_name = market_name
    self.urls = urls
    self.raw_pages_content = []
    self.items_data = []
    self.content = ""

  def start_requests(self):
    raw_pages_content = []
     
    for url in self.urls:
      try:
        response = requests.get(url)
        website_text = response.text
        raw_pages_content.append(website_text)
      except requests.exceptions:
        print(requests.exceptions)
        continue
    
    self.raw_pages_content = raw_pages_content
  
  def generate_text_list(self):
    list_header = f"\n-------------------------- {self.market_name} 🏪 --------------------------"
    
    items_str = "\n".join([ f"🔵 {item['name']} - €{item['price']}" for item in self.items_data ])
    
    content_str = f"{list_header}\n{items_str}"

    self.content = content_str
  
  def parse(self, parse_data):
    items_data = []

    for html_content in self.raw_pages_content:
      soup = BeautifulSoup(html_content, 'html.parser')
      
      parsed_data = parse_data(soup=soup)
      items_data.append(parsed_data)

    self.items_data = items_data
  
  def store_data(self):
    try:
      file_path = "email.txt"
      new_content = f"{self.content}\n"
      
      # Check if file exists
      if os.path.isfile(file_path):
        with open(file_path, "a") as file:
          file.write(new_content)
      else:
        with open(file_path, "w") as file:
          file.write(new_content)
    except:
      pass

