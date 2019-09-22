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
        text = soup.get_text()

        if (text.find ("Account") | text.find ("Password") | text.find ("account number") | text.find("scotiabank")):
            print ("FOUND IT!!!!!!!!!!!")


