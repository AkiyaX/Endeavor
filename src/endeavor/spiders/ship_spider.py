import scrapy
import logging as log


class ShipSpider(scrapy.Spider):
    name = 'ship'

    def start_requests(self):
        urls = [
            'https://starcitizen.tools/Category:Ships'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ship_names = response.xpath(
            '//td/a/text()').extract()
        ship_names = list(filter(lambda x: x != 'Squadron 42', ship_names))
        log.info(f'Total ship count: {len(ship_names)}')
        for name in ship_names:
            log.info(name)
