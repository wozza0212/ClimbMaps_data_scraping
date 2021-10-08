import scrapy


class AreasSpider(scrapy.Spider):
    name = 'areas'
    allowed_domains = ['www.ukclimbing.com/']
    start_urls = ['https://www.ukclimbing.com/logbook/map/?g=0&loc=s434wr&dist=150&km=1&q=&rock=0&dir=0&day=0&rain=0#main']

    def parse(self, response):
        areas = response.xpath('//div[@class="panel-heading"]')
        for area in areas:
            name = area.xpath('.//text()').get()
            link = area.xpath('.//')

            yield {
                'Area:': name
            }

        # next_page = response.xpath('//a[@title="Next page"]/@href').get()
        # start = 'https://www.ukclimbing.com/logbook/map/'
        # full = f'{start}{next_page}'
        # if full:
        #     yield scrapy.Request(url=next_page, callback=self.parse)

