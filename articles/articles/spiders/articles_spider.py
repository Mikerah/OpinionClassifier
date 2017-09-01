from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.http import HtmlResponse, Request
from scrapy import Selector
from selenium import webdriver
from scrapy.utils.response import open_in_browser
from bs4 import BeautifulSoup
from articles.items import Article

class ArticlesSpider(CrawlSpider):
    """
    Spider that crawls searchs for New York Times articles from 2016
    """
    
    name = "articles"
    allowed_domains = ["nytimes.com"]
    start_urls = ["http://spiderbites.nytimes.com/free_2016/index.html"]
    
    rules = (Rule(LinkExtractor(restrict_css="div.articlesMonth ul li a", restrict_xpaths="@href"), callback="parse_index_url"),)
    
    def __init__(self, *a, **kw):
        # Initialize webdriver
        super(ArticlesSpider, self).__init__(*a, **kw)
        self.driver = webdriver.Firefox()
        
        
    def parse_index_url(self ,response):
        selector = Selector(text=response.body)
        for article_url in selector.css("ul#headlines li a").xpath("@href").extract():
            # Go to everything link in the index page and call self.parse_article_page
            request = Request(article_url, callback=self.parse_article_page)
            yield request
            
    def parse_article_page(self, response):
        # Give response url to selenium webdriver
        self.driver.get(response.url)
        
        # Store scraped data into ItemLoader object
        item_loader = ItemLoader(item=Article(),response=response)
        item_loader.add_value('url',response.url)
        item_loader.add_xpath('type', '//meta[@property="article:top-level-section"]/@content')
        item_loader.add_xpath('title', '//meta[@name="hdl"]/@content')
        item_loader.add_xpath('author', '//meta[@name="author"]/@content')
        item_loader.add_xpath('text', '//p/text()')
        return item_loader.load_item()