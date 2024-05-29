import scrapy
from unsplash_scraper.items import UnsplashImageItem

class UnsplashSpider(scrapy.Spider):
    name = 'unsplash_spider'
    start_urls = ['https://unsplash.com/']

    def parse(self, response):
        # Селектор для нахождения изображений в основной ленте
        images = response.css('figure[itemprop="image"] a::attr(href)').extract()
        for image in images:
            yield response.follow(image, self.parse_image)

    def parse_image(self, response):
        item = UnsplashImageItem()
        # Получаем URL изображения в максимальном размере
        image_url = response.css('img[src*="images.unsplash.com/photo"]::attr(src)').extract_first()
        if image_url:
            max_size_url = image_url.split('?')[0]  # Удаляем параметры, чтобы получить оригинальный размер
            item['image_urls'] = [max_size_url]
            item['title'] = response.css('title::text').extract_first().strip()
            # Извлекаем теги изображения
            item['tags'] = response.xpath('//div[@class="rx3zu _UNLg"]//a[@class="VyS40 GcCli p4rnw"]/text()').extract()
            yield item
