from scrapy.item import Item, Field


class Website(Item):

    title = Field()
    body = Field()
