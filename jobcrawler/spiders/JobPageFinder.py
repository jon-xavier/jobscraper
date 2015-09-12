'''
Created on Sep 11, 2015

@author: jaaronxavier
'''
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

domainlist = ['docker.com']
starturls = ['http://docker.com']

class JobLinkExtractor(LinkExtractor):
    allow = 

class JobPageFinder(CrawlSpider):
    '''The idea here is that this crawler hits a homepage, follows its most
    likely links to get it to a jobs page, and then once it finds a jobs page
    saves that url to an item. it's going to return a list of links to all the 
    jobs on the site.'''
    name = 'jobpagefinder'
    allowed_domains = domainlist
    start_urls = starturls
    
    rules = (
             Rule(
             
             
             
             )