import unittest
from unittest.mock import patch

import application


class TestApplication(unittest.TestCase):
    @patch('rss.feed_reader.FeedReader.get_latest_article')
    def test_application_returns_ok_message(self, mock_latest_article):
        expected_latest_article = 'my latest article'
        mock_latest_article.return_value = expected_latest_article

        result = application.handler(None, None)

        self.assertEqual(expected_latest_article, result['body'])
        self.assertEqual(200, result['statusCode'])


if __name__ == '__main__':
    unittest.main()
