# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShipItem(scrapy.Item):
    Name = scrapy.Field(serializer=str)
    Manufacturer = scrapy.Field(serializer=str)
    Size = scrapy.Field(serializer=str)
    Role = scrapy.Field(serializer=list)
    FlightReady = scrapy.Field(serializer=bool)
    PledgePrice = scrapy.Field(serializer=int)


class ShipImageItem(scrapy.Item):
    Name = scrapy.Field(serializer=str)
    ImageUrls = scrapy.Field(serializer=list)
