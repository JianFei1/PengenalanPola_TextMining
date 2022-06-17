import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):

        arrayData = []
        for i in range(0, 5):
            inArray = 'https://indeks.kompas.com/?site=news&page=' + str(i)
            arrayData.append(inArray)
        for url in arrayData:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(1,16):
            yield {
                'link': response.css('body > div.wrap > div.container.clearfix > div:nth-child(3) > div.col-bs10-7 > div.latest--indeks.mt2.clearfix > div:nth-child(' + str(i) +') > div.article__list__title > h3 > a::attr(href)').extract(),
            }







