import os
import unittest
from unittest.mock import patch, MagicMock

from images.image_service import store_article_metadata_in_database
from scraping.scraper import Article

EXPECTED_IMAGE_ID = '23'


class PutResponseMock:
    @staticmethod
    def json():
        return {'id': EXPECTED_IMAGE_ID}


class TestImageService(unittest.TestCase):

    @patch("requests.put", MagicMock(return_value=PutResponseMock))
    def test_when_storing_image_return_id(self):
        os.environ['ARTICLE_ENDPOINT_URL'] = 'article.endpoint'
        os.environ['ARTICLE_BASIC_AUTH_USERNAME'] = 'auth.username'
        os.environ['ARTICLE_BASIC_AUTH_PASSWORD'] = 'auth.password'

        article = Article(
            url="url",
            title="title",
            publication_date="publication_date",
            category="category",
            introduction="introduction",
            image_url="image_url"
        )
        actual_image_id = store_article_metadata_in_database(article)
        self.assertEqual(EXPECTED_IMAGE_ID, actual_image_id)

    @patch("requests.put")
    def test_calls_article_endpoint_with_credentials(self, put_mock):
        os.environ['ARTICLE_ENDPOINT_URL'] = 'article.endpoint'
        os.environ['ARTICLE_BASIC_AUTH_USERNAME'] = 'auth.username'
        os.environ['ARTICLE_BASIC_AUTH_PASSWORD'] = 'auth.password'

        article = Article(
            url="url",
            title="title",
            publication_date="publication_date",
            category="category",
            introduction="introduction",
            image_url="image_url"
        )
        store_article_metadata_in_database(article)
        put_mock.assert_called_once_with(url='article.endpoint', auth=('auth.username', 'auth.password'), json={
            "title": "title",
            "publicationDate": "publication_date",
            "url": "url",
            "category": "category",
            "introduction": "introduction"
        })
