from rss.feed_reader import FeedReader


def handler(event, context):
    feed_reader = FeedReader('https://dieterjordens.medium.com/feed')
    latest_article = feed_reader.get_latest_article()
    print(latest_article)

    return {
        'statusCode': 200,
        'body': latest_article
    }


if __name__ == '__main__':
    print(handler(None, None))