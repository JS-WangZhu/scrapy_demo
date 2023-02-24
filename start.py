from scrapy import cmdline
import os
import sys
# pip3 install scrapy
# scrapy genspider 爬虫名 域名
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
cmdline.execute('scrapy crawl baidu'.split())
# cmdline.execute('scrapy crawl baidu -o hotsearch.csv'.split())