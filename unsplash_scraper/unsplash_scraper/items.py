import scrapy

class UnsplashImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    tags = scrapy.Field()
