from scrapy.crawler import CrawlerProcess
from endeavor.spiders import ship_spider
from endeavor.spiders import ship_image_spider
from scrapy.settings import Settings
from endeavor import settings


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(ship_spider.ShipSpider)
    process.crawl(ship_image_spider.ShipImageSpider)
    process.start()
