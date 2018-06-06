from models.builder import TextBlockBuilder
from models.builder import ImageBlockBuilder
from models.builder import LinksBlockBuilder
from commons.html_helper import HtmlHelper

from lxml import html


class Crawler:

    def __init__(self, feed_datasource):
        self.__feed_datasource = feed_datasource
        self.__builders = []

    def read_feed(self):
        root = self.__feed_datasource.read()
        items = root.findall(".//item")

        feed = []

        for item in items:
            feeditem = self.__prepare_item(item)
            feed.append(feeditem)

        return feed

    def add_block_builder(self, builder):
        self.__builders.append(builder)

    def __prepare_item(self, item):
        title = item.find("title").text
        link = item.find("link").text

        description = item.find('description').text

        tree = html.fromstring(description)

        blocks = []

        for builder in self.__builders:
            blocks += builder.build(tree)

        return {'title': title, 'link': link, 'description': blocks}


class Builder:

    def __init__(self, datasource):
        self.__datasource = datasource

    def build(self):

        html_helper = HtmlHelper()

        textblockbuilder = TextBlockBuilder(html_helper)
        imageblockbuilder = ImageBlockBuilder()
        linksblockbuilder = LinksBlockBuilder()

        crawler = Crawler(self.__datasource)
        crawler.add_block_builder(textblockbuilder)
        crawler.add_block_builder(imageblockbuilder)
        crawler.add_block_builder(linksblockbuilder)

        return crawler


