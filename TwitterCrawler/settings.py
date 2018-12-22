# -*- coding: utf-8 -*-

USER_AGENT = 'TwitterCrawler'

# settings for spiders
BOT_NAME = 'TwitterCrawler'
LOG_LEVEL = 'DEBUG'
DOWNLOAD_HANDLERS = {'s3': None, }

SPIDER_MODULES = ['TwitterCrawler.spiders']
NEWSPIDER_MODULE = 'TwitterCrawler.spiders'
ITEM_PIPELINES = {
}