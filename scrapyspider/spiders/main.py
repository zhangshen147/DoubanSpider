from scrapy import cmdline
cmdline.execute("scrapy crawl douban_spider -o douban.csv".split())
