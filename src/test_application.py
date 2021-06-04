import os
import unittest
from unittest.mock import patch, MagicMock

import application
from scraping.scraper import Article

ARTICLE_ID = '42'
ARTICLE_URL = 'www.article.com'
ARTICLE = Article(
    image_url='www.image-url.com',
    url='url',
    title='title',
    publication_date='publication date',
    category='category',
    introduction='introduction'
)


class TestApplication(unittest.TestCase):

    @patch('scraping.scraper.get_article', MagicMock(return_value=ARTICLE))
    @patch('rss.feed_reader.get_latest_article_url', MagicMock(return_value=ARTICLE_URL))
    @patch('images.image_service.store_article_metadata_in_database', MagicMock(return_value=ARTICLE_ID))
    @patch('images.image_service.store_image_in_s3', MagicMock)
    def test_application_returns_ok_message(self):
        os.environ['ARTICLE_RSS_FEED_URL'] = 'www.my-feed.com'

        result = application.handler(None, None)

        self.assertEqual(ARTICLE_ID, result['body'])
        self.assertEqual(200, result['statusCode'])