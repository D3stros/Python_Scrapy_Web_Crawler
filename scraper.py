import scrapy


class BookSpider(scrapy.Spider):
    name = "bookspider"
    url = "INSERT URL"
    start_urls = [url]

    def parse(self, response):
        for article in response.css("article.product_pod"):
            yield {
                "price": article.css(".price_color::text").extract_first(),
                "title": article.css("h3 > ::attr(title)").extract_first()
            }
            next = response.css(".next > a::attr(href)").extract_first()
            if next:
                yield response.follow(next, self.parse)
