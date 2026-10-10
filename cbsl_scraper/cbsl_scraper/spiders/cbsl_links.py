
import scrapy
from urllib.parse import urlparse

class CbslLinksSpider(scrapy.Spider):

    name = "cbsl_links"

    allowed_domains = ["www.cbsl.gov.lk"]

    start_urls = ["https://www.cbsl.gov.lk/"]

    custom_settings = {
        "DEPTH_LIMIT": 2
        }

    relevant_keywords = [
        "inflation",
        "exchange",
        "monetary",
        "rates-and-indicators"
    ]

    def parse(self, response):

        self.logger.info(f"Opened: {response.url}")

        # Extract normal links

        for link in response.css("a[href]"):
            href = link.attrib.get("href")

            if not href:
                continue

            text = " ".join(link.css("::text").getall()).strip()
            full_url = response.urljoin(href)
            parsed = urlparse(full_url)

            if (parsed.netloc != "www.cbsl.gov.lk"):
                continue

            yield {
                "link_type": "a",
                "link_text": text,
                "url": full_url,
                "source_page": response.url
            }

            combined = (text + " " + full_url).lower()

            relevant = any(
                keyword in combined
                for keyword
                in self.relevant_keywords
            )

            # Follow relevant pages
            if relevant:
                if not full_url.lower().endswith((".pdf",".xls",".xlsx",".csv")):
                    yield response.follow(
                        full_url,
                        callback=self.parse
                    )

        # Extract iframe links

        for iframe in response.css("iframe[src]"):
            src = iframe.attrib.get("src")
            if not src:
                continue

            full_url = response.urljoin(src)
            parsed = urlparse(full_url)

            if (parsed.netloc != "www.cbsl.gov.lk"):
                continue

            yield {
                "link_type": "iframe",
                "link_text": "iframe",
                "url": full_url,
                "source_page": response.url
            }

            # Follow iframe
            yield response.follow(
                full_url,
                callback=self.parse
            )
