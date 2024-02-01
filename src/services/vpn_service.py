from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin
import requests


class VPNService:
    def __init__(self, site_name, original_url):
        self.site_name = site_name
        self.original_url = original_url
        self.response = None
        self.soup = None

    def intercept_request(self):
        self.response = requests.get(self.original_url)

    def parse_content(self,) -> BeautifulSoup:
        self.soup = BeautifulSoup(self.response.content, "html.parser")

    def internal_link_handler(self) -> None:
        for link in self.soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith(("http://", "https://", "www.")):
                link['href'] = f'{self.site_name}{self.original_url}/{href}'

    def external_resource_handler(self) -> None:
        for element in self.soup.find_all(["script", "img", "link"]):
            if "href" in element.attrs:
                element["href"] = urljoin(self.original_url, element["href"])
            elif "src" in element.attrs:
                element["src"] = urljoin(self.original_url, element["src"])

    def process_page(self) -> BeautifulSoup:
        self.intercept_request()
        self.parse_content()
        self.internal_link_handler()
        self.external_resource_handler()
        return self.soup

    def calculate_site_stat(self):
        data_received_mb = round(sys.getsizeof(self.response.content)
                                 / (1024 * 1024), 3)
        return data_received_mb
