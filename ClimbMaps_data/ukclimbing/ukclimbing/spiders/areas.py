import scrapy
from scrapy_splash import SplashRequest


class AreasSpider(scrapy.Spider):
    name = 'areas'
    allowed_domains = ['www.ukclimbing.com/logbook/map/']

    script = '''
    function main(splash, args)
      splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
      url = args.url
      assert(splash:go(url))
    
      
      input_box3 = assert(splash:select("[name='dist']"))
      input_box3:focus()
      input_box3:send_text('150')
      assert(splash:wait(2))
      
      
      
      input_box2 = assert(splash:select("[name='g']"))
      input_box2:send_keys("<B>")
      input_box2:send_keys("<Enter>")
      assert(splash:wait(5))
      
      input_box = assert(splash:select("#loc"))
      input_box:focus()
      input_box:send_text("ll240ae")
      assert(splash:wait(2))
      
      
      input_box:send_keys("<Enter>")
      assert(splash:wait(5))
      splash:set_viewport_full()
      return {
        
        html = splash:html()
      }
    end
'''

    def start_requests(self):
        yield SplashRequest(url= 'https://www.ukclimbing.com/logbook/map/', callback=self.parse, endpoint='execute', args={
            'lua_source': self.script
        })

    def parse(self, response):
        #print(response.body)
        areas = response.xpath("//div[@class='col-sm-4']/div")
        for area in areas:
            area_name = area.xpath(".//div/text()").get()
            coordinates = area.xpath(".//@onmouseover").get()

            yield {
                'Area Name:': area_name,
                'Coordinates:': coordinates
            }

        next_page = response.xpath('(//a[@title="Next page"])[1]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)