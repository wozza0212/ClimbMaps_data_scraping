import scrapy

# countries = //tbody[@class="jsx-2642336383"]/tr/td/a


class DebtSpider(scrapy.Spider):
    name = 'debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        countries = response.xpath('//tbody[@class="jsx-2642336383"]/tr/td/a')
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            yield response.follow(url=link, callback=self.parse_country_debt, meta={'country_name': name})

    def parse_country_debt(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath('//*[@id="__next"]/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div/div/div[2]/table/tbody')
        for row in rows:
            year = row.xpath('.//tr/td[1]/text()').get()
            growth = row.xpath('.//tr/td[3]/span/text()').get()

            yield {
                'Name': name,
                'Year:': year,
                'Growth': growth

            }
