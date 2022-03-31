import scrapy
from scrapy.item import Item, Field
class Producto(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    id = Field()
    nombre = Field()
    precio = Field()
    urlimagen = Field()
    tipodivisa =Field()
    fecha = Field()

