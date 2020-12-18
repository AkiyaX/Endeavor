# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class ShipItem(scrapy.Item):
    Name = scrapy.Field(serializer=str)
    Manufacturer = scrapy.Field(serializer=str)
    Size = scrapy.Field(serializer=str)
    Role = scrapy.Field(serializer=list)
    FlightReady = scrapy.Field(serializer=bool)
    PledgePrice = scrapy.Field(serializer=int)
