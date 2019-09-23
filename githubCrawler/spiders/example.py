# -*- coding: utf-8 -*-
import scrapy
from ..items import GithubcrawlerItem


class AppSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['github.com']
    content_domains = 'https://github.com/'
    start_urls = []



    def __init__(self, urls=None, *args, **kwargs):
        super(AppSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls.split(',')

    def parse(self, response):
        raw_url = response.css('a#raw-url').xpath('@href').extract_first()
        if raw_url:
                href = self.content_domains+raw_url
                print("scrapy from href --> ", href)
                yield scrapy.Request(href, callback=self.parse_link)
        else:
            for link in response.selector.xpath('//a[@class="js-navigation-open"]/@href').extract()[1:]:
                href = self.content_domains+link
                yield scrapy.Request(href, callback=self.parse)

    def parse_link(self, response):
        responseStr = str(response).strip()
        # print('Jun response.text --> ', response.text)
        url = responseStr.strip()[5:len(responseStr) - 1]


        sensitive_words = ["Account", "Password", "scotiabank", "colorPrimary"]
        output_found = "FOUND SENSITIVE Information: {0} in file {1}"
        output_not_found = "Can't find Sensitive word: {0}"
        output_start_check = "<========================= Start Checking Sensitive Information for file: {0} =========================>"
        output_end_check = "<========================= End Checking Sensitive Information for file: {0} =========================>"

        print(output_start_check.format(url))
        for word in sensitive_words:
            if (response.text.find(word) != -1):
                print(output_found.format(word, responseStr))
        print(output_end_check.format(url))

        item = GithubcrawlerItem()
        item['file_urls'] = [url]
        return item



