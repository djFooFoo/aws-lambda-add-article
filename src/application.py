from rss import feed_reader
from scraping import scraper


def handler(event, context):
    latest_article_url = feed_reader.get_latest_article_url("https://dieterjordens.medium.com/feed")
    article = scraper.get_article(latest_article_url)

    # perform an article update request
    # upload file to amazon s3
    # print(article)

    return {"statusCode": 200, "body": latest_article_url}


if __name__ == "__main__":
    print(handler(None, None))
