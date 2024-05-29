import csv
from scrapy.exporters import CsvItemExporter

class CsvWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('unsplash_images.csv', 'w+b')  # Измените на 'w+b' для правильного режима записи
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.fields_to_export = ['image_urls', 'images', 'title', 'tags']
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
