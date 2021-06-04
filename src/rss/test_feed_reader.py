import unittest
from unittest.mock import patch

from rss.feed_reader import get_latest_article_url


class TestFeedReader(unittest.TestCase):
    @patch('feedparser.parse')
    def test_feed_reader_returns_id_of_latest_article(self, mock_parse):
        expected_latest_article_id = 'an id'
        mock_parse.return_value = {
            'entries': [
                {
                    'id': expected_latest_article_id
                }
            ]
        }
        actual_latest_article_id = get_latest_article_url('an url')

        self.assertEqual(expected_latest_article_id, actual_latest_article_id)
