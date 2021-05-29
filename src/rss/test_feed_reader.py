import unittest
from unittest.mock import patch

from rss.feed_reader import FeedReader


class TestApplication(unittest.TestCase):
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

        feed_reader = FeedReader('an url')
        actual_latest_article_id = feed_reader.get_latest_article()

        self.assertEqual(expected_latest_article_id, actual_latest_article_id)


if __name__ == '__main__':
    unittest.main()
