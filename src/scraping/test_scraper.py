import unittest
from unittest.mock import patch, MagicMock

import newspaper

from scraping.scraper import get_article, Article


def get_newspaper_article():
    newspaper_article = newspaper.Article(url='url')
    newspaper_article.top_image = 'top image'
    newspaper_article.url = 'url'
    newspaper_article.title = 'title'
    newspaper_article.publish_date = '2021-05-27 08:47:25.160000+00:00'
    newspaper_article.meta_description = 'meta'
    return newspaper_article


class TestScraper(unittest.TestCase):
    newspaper_article = get_newspaper_article()

    @patch('newspaper.Article', MagicMock(return_value=newspaper_article))
    @patch('newspaper.Article.build', MagicMock())
    @patch('nltk.download', MagicMock())
    def test_get_article_returns_article(self):
        expected_article = Article(
            image_url=self.newspaper_article.top_image,
            url=self.newspaper_article.url,
            title=self.newspaper_article.title,
            category='Other',
            introduction=self.newspaper_article.meta_description,
            publication_date='2021-05-27'
        )

        actual_article = get_article('www.google.be')

        self.assertEqual(expected_article, actual_article)
