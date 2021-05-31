import unittest
from unittest.mock import patch

import application
from scraping.scraper import Article


class TestApplication(unittest.TestCase):

    @patch('scraping.scraper.get_article')
    @patch('rss.feed_reader.get_latest_article_url')
    def test_application_returns_ok_message(self, mock_get_latest_article_url, mock_get_article):
        mock_get_latest_article_url.return_value = 'my latest article'
        mock_get_article.return_value = Article(
            url='url',
            title='title',
            publication_date='publication date',
            category='category',
            introduction='introduction'
        )

        result = application.handler(None, None)

        self.assertEqual('my latest article', result['body'])
        self.assertEqual(200, result['statusCode'])


if __name__ == '__main__':
    unittest.main()
