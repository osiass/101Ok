from icrawler.builtin import GoogleImageCrawler

# Google'dan resim indir
google_crawler = GoogleImageCrawler(storage={"root_dir": "okey_taslari"})

google_crawler.crawl(keyword="okey taşları", max_num=200)
