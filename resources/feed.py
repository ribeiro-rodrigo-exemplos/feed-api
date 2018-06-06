from models.crawler import Builder as CrawlerBuilder
from models.datasource import FeedDatasource
from resources.protected import Protected
import configparser


class Feed(Protected):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        datasource = FeedDatasource(config['feed']['url'])
        self.__crawler = CrawlerBuilder(datasource).build()

    def get(self):
        try:
            feed = self.__crawler.read_feed()
            return {'feed': feed}
        except:
            return {'', 500}
