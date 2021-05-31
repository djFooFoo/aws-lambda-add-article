import feedparser


def get_latest_article_url(url) -> str:
    news_feed = feedparser.parse(url)
    news_feed_entries = news_feed['entries']
    latest_article = news_feed_entries[0]
    return latest_article['id']
