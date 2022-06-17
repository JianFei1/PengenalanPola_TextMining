import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        dataCSV = pd.read_csv('link.csv')
        dataCSV.head()
        indexData = dataCSV.iloc[:, [0]].values
        arrayData = []
        for i in indexData:
            ambil = i[0]
            arrayData.append(ambil)
        print(arrayData)


        for url in arrayData:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # for i in range(1,6):
        yield {
            'judul': response.css('body > div.wrap > div.container.clearfix > div:nth-child(2) > div > h1::text').extract(),
            'tanggal': response.css('body > div.wrap > div.container.clearfix > div.row.col-offset-fluid.clearfix.js-giant-wp-sticky-parent > div.col-bs10-7.js-read-article > div.read__header.col-offset-fluid.clearfix > div:nth-child(1) > div::text').extract(),
            'label': response.css('body > div.wrap > div.container.clearfix > div:nth-child(2) > div > h3 > ul > li:nth-child(3) > a > span::text').extract(),
            'isi': response.css('body > div.wrap > div.container.clearfix > div.row.col-offset-fluid.clearfix.js-giant-wp-sticky-parent > div.col-bs10-7.js-read-article > div.read__article.mt2.clearfix.js-tower-sticky-parent > div.col-bs9-7 > div.read__content > div > p::text').extract(),
           
        }