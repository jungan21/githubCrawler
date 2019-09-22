# -*- coding: utf-8 -*-
import scrapy

from bs4 import BeautifulSoup
from scrapy import Request

import json
import re


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['github.com']
    start_urls = ["https://github.com/pnorman/josm-presets/blob/master/shops.xml"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, features='lxml')
        web_text = soup.get_text()

        sensitive_words = ["Account", "Password", "scotiabank", "wechat"]
        output_found = "FOUND Sensitive word: {0}"
        output_not_found= "Can't find Sensitive word: {0}"


        for word in sensitive_words:
            if ( web_text.find (word) == -1):
                print(output_not_found.format(word))
            else:
                print(output_found.format(word))




