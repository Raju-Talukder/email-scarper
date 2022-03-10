import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MailsSpider(CrawlSpider):
    name = 'mails'
    allowed_domains = ['scrapebay.com']
    start_urls = ['http://scrapebay.com']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        emails = re.findall(r'[\w\.]+@[\w\.]+', response.text)
        for email in emails:
            if 'bootstrap' not in email:
                yield {
                    'URL': response.url,
                    'Email': email
                }
