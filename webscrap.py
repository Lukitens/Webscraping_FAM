# scrapy runspider webscrap.py -o atletas.json -t json -s FEED_EXPORT_ENCODING=utf-8
#importamos scrapy y sus metodos
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Atleta(Item):
    nombre = Field()
    apellido = Field()
    club = Field()
    fecha_nacimiento = Field()

class WebfamCrawler(CrawlSpider):
    name = "webfam"

    custom_settings = {        #Le asignamos el header
        "USER_AGENT" : "Opera GX (Windows10)",

        # Le asignamos el limite de paginas que queremos recorrer
        #'CLOSESPIDER_PAGECOUNT' : 5
        }
    
    allowed_domains = ["webfam.com.ar"]

    start_urls = ["https://webfam.com.ar/atletas"]

    download_delay = 1

    rules = (
        Rule(LinkExtractor(
            allow=r'page=\d+'
        ), follow= True),
        Rule(LinkExtractor(
            allow=r'/atleta-interna/atleta/\d+'
        ), follow= True, callback= "parse_items")
    )

    def parse_items(self, response):
        item = ItemLoader(Atleta(), response)
        item.add_xpath("nombre", '//span[@class="top"]/text()')
        item.add_xpath("apellido", '//span[@class="bold"]/text()')
        item.add_xpath("club", '//div[@class="detalles_deportista"]/p[text()="Club"]/following-sibling::p[1]/text()')
        item.add_xpath("fecha_nacimiento", '//div[@class="detalles_deportista"]/p[1]/text()')

        yield item.load_item()