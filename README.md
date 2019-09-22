# Prerequisite 
install Python first :)

Then, run following commands to install depended packages:

pip install Scrapy

pip install beautifulsoup4

# How to run
cd githubCrawler/

modify settings.py file to change ROBOTSTXT_OBEY = True to ROBOTSTXT_OBEY = False

cd spiders/

modify example.py file (change this variable to URL you want to check: start_urls = ["https://github.com/****/shops.xml"] i.e. https://github.com/jungan21/githubCrawler/blob/master/githubCrawler/spiders/example.py#L14)

modify this line of code to add whatever sensitive words you want to search: 
https://github.com/jungan21/githubCrawler/blob/master/githubCrawler/spiders/example.py#L20

scrapy crawl example (please make sure you run this command in the fold where you have settings.py)


