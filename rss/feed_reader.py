import feedparser


class FeedReader(object):
    def __init__(self, url):
        self.news_feed = feedparser.parse(url)

    def get_latest_article(self) -> str:
        news_feed_entries = self.news_feed['entries']
        latest_article = news_feed_entries[0]
        return latest_article['id']
