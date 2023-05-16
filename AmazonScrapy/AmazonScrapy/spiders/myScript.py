import scrapy
from ..items import AmazonscrapyItem
# inherit the class

class myScraper(scrapy.Spider):
    name = "AmazonCrawler"
    start_urls = ["https://www.amazon.in/s?k=air+conditioner&rh=n%3A976442031%2Cp_n_date_first_available_absolute%3A1318487031&dc&ds=v1%3ABbsdwCeVIhhGdy1pq8OIMprzuFKWaa24GYQEWYRmOZo&crid=1R3UCB3GZJ3UP&qid=1683728146&rnid=1318486031&sprefix=ai%2Caps%2C1420&ref=sr_nr_p_n_date_first_available_absolute_1"]

    def parse(self, response):
        item = AmazonscrapyItem()


        name_of_product = response.css('.a-color-base.a-text-normal::text').extract()
        price= response.css('.a-price-whole').css('::text').extract()
        discounts = response.css('.a-letter-space+ span').css('::text').extract()
        product_image = response.css('.s-image::attr(src)').extract()

        item['name_of_product'] = name_of_product
        item['price'] = price
        item['discounts'] = discounts
        item['product_image'] = product_image

        yield item

