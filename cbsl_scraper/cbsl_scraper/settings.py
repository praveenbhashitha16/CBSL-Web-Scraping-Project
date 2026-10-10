
BOT_NAME = "cbsl_scraper"

SPIDER_MODULES = ["cbsl_scraper.spiders"]

NEWSPIDER_MODULE = "cbsl_scraper.spiders"

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS_PER_DOMAIN = 1

DOWNLOAD_DELAY = 10

DOWNLOAD_TIMEOUT = 60

RETRY_TIMES = 2

USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36"
)

FEED_EXPORT_ENCODING = "utf-8"

LOG_LEVEL = "INFO"
