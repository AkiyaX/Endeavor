import scrapy
import requests
import logging as log
from scrapy.selector import Selector
from endeavor.items import ShipImageItem

MAX_PAGE = 18
BASE_URL = "https://robertsspaceindustries.com"


class ShipImageSpider(scrapy.Spider):
    name = 'ship image spider for rsi'
    custom_settings = {
        'ITEM_PIPELINES': {
            'endeavor.pipelines.ShipImagePipeline': 300
        }
    }

    def start_requests(self):
        for page in range(1, MAX_PAGE+1):
            # Get ship name and url
            url = BASE_URL + "/api/store/getShips"
            body = {
                "sort": "name_asc",
                "search": "",
                "itemType": "ships",
                "storefront": "pledge",
                "type": "",
                "classification": [],
                "mass": "",
                "manufacturer_id": [],
                "length": "",
                "max_crew": "",
                "msrp": "",
                "page": page
            }
            response = requests.post(url, body)
            html = response.json()['data']['html']

            items = Selector(text=html).xpath(
                '//li[@class="ship-item"]/div[@class="center"]').extract()

            for item in items:

                request_url = BASE_URL + Selector(text=item).xpath(
                    '//a[@class="filet"]/@href').extract_first()

                ship_name = Selector(text=item).xpath(
                    '//a/span[contains(@class,"name")]/text()').extract_first()

                yield scrapy.Request(url=request_url,
                                     meta={'shipName': ship_name},
                                     callback=self.parse)

    def parse(self, response):
        ship_name = response.meta['shipName'].strip()
        log.info(f'Get ship image for [{ship_name}] start...')
        item = ShipImageItem()
        item['Name'] = ship_name
        item['ImageUrls'] = response.xpath(
            '//div[@class="download_source"]/a/@href').extract()
        yield item
