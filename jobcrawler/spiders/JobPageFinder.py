'''
Created on Sep 11, 2015

@author: jaaronxavier
'''
import tldextract
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from jobcrawler.items import JobsPagesItem
from jobcrawler.config import domainlist, starturls, whitelist,\
    blacklist, keys

whitelist_regex = '|'.join(whitelist)
blacklist_regex = '|'.join(blacklist)

class JobPageFinder(CrawlSpider):
    '''The idea here is that this crawler hits a homepage, follows its most
    likely links to get it to a jobs page, and then once it finds a jobs page
    saves that url to an item. it's going to return a list of links to all the 
    jobs on the site.'''
    name = 'jobpagefinder'
    allowed_domains = domainlist
    start_urls = starturls
     
    rules = (
             Rule (
                  LxmlLinkExtractor (
                                    allow= '/{}/g'.format(whitelist_regex), 
                                    deny= '/{}/g'.format(blacklist_regex, 
                                    follow=True), 
                                    ),
                  callback="parse_items",
                  ),
             )
             
    def parse_items(self, response):
        item = JobsPagesItem
        sel = Selector(response)
        print response.url
        if any(key in response.body for key in keys):
           #ext = tldextract.extract(response.url)
           item['company'] = ext.domain
           item['jobtitle'] = sel.xpath('//title/text()').extract()
           item['link'] = response.url
           yield item
         
            
             
    
    