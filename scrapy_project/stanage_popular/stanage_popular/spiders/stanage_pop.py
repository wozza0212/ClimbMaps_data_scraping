import scrapy

# area = response.xpath('//meta[@property="og:title"]/@content')
# area.get()
# latitude = response.xpath('//meta[@property="place:location:latitude"]/@content')
#  longitude = response.xpath('//meta[@property="place:location:longitude"]/@content')



class StanagePopSpider(scrapy.Spider):
    name = 'stanage_pop'
    allowed_domains = ['www.ukclimbing.com/logbook/crags/stanage_popular-104']
    start_urls = ['http://www.ukclimbing.com/logbook/crags/stanage_popular-104/']

    def parse(self, response):
        area = response.xpath('//meta[@property="og:title"]/@content').get()
        latitude = response.xpath('//meta[@property="place:location:latitude"]/@content').get()
        longitude = response.xpath('//meta[@property="place:location:longitude"]/@content').get()

        yield {
            'Area Name': area,
            'Latitude:': latitude,
            'Longitude:': longitude
        }
