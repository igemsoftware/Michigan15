# Scrapy settings for BioScraper project

SPIDER_MODULES = ['BioScraper.spiders']
NEWSPIDER_MODULE = 'BioScraper.spiders'
DEFAULT_ITEM_CLASS = 'BioScraper.items.Website'

ITEM_PIPELINES = {'BioScraper.pipelines.CSVPipeline': 300 }

'''to save scrapy output to text
LOG_STDOUT = True
LOG_FILE = 'neb_output.txt'
'''
