import requests
import xml.etree.ElementTree as ET


class FeedDatasource:

    def __init__(self, url):
        self.__url = url

    def read(self):
        page = requests.get(self.__url)
        return ET.fromstring(page.content)