import scrapy
import logging as log
from endeavor.items import ShipItem


class ShipSpider(scrapy.Spider):
    name = 'ship basic info spider from wiki'
    custom_settings = {
        'ITEM_PIPELINES': {
            'endeavor.pipelines.ShipItemPipeline': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://starcitizen.tools/Category:Ships'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ships = response.xpath('//table//tr')
        count = 0
        for ship in ships[1:]:
            item = ShipItem()
            # name
            item['Name'] = ship.xpath(
                'td[1]//text()').extract_first().replace(' (replica)', '')
            # manufacturer
            item['Manufacturer'] = ship.xpath(
                'td[2]//text()').extract_first().replace('\n', '')
            # role
            item['Role'] = ship.xpath(
                'td[3]//text()').extract_first().replace(
                    '\n', '').replace(' ', '').split('/')
            # size
            item['Size'] = ship.xpath(
                'td[4]//text()').extract_first().replace('\n', '')
            # flight ready
            state = ship.xpath(
                'td[6]//text()').extract_first().replace('\n', '')
            item['FlightReady'] = state == 'Flight ready'
            # price
            price = ship.xpath(
                'td[7]//text()').extract_first().replace('\n', '')
            sc_state = ['Flight ready', 'In concept', 'In production']
            if state in sc_state and price:
                item['PledgePrice'] = int(price)
                count += 1
                log.info(f'Get ship: [{item["Name"]}]')
                yield item
        log.info(f'Total ship count: {count}.')
