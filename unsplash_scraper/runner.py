from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from unsplash_scraper.spiders.unsplash_spider import UnsplashSpider

if __name__ == "__main__":
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    process.crawl(UnsplashSpider)
    process.start()
