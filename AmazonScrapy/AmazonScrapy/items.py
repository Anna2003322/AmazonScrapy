# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_of_product = scrapy.Field()
    price = scrapy.Field()
    discounts = scrapy.Field()
    product_image = scrapy.Field()
    pass
