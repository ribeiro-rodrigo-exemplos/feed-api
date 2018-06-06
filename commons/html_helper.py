from bs4 import BeautifulSoup
from lxml import html


class HtmlHelper:
    @staticmethod
    def extract_text(element):
        return ' '.join(BeautifulSoup(html.tostring(element), "html.parser").stripped_strings)