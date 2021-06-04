import io
import os
from io import BytesIO

import boto3
import requests
from PIL import Image

from scraping.scraper import Article


def store_article_metadata_in_database(article: Article) -> str:
    json = {
        "title": article.title,
        "publicationDate": article.publication_date,
        "url": article.url,
        "category": article.category,
        "introduction": article.introduction
    }
    result_json = requests.put(url=(os.environ['ARTICLE_ENDPOINT_URL']),
                               auth=((os.environ['ARTICLE_BASIC_AUTH_USERNAME']),
                                     (os.environ['ARTICLE_BASIC_AUTH_PASSWORD'])),
                               json=json).json()
    return result_json['id']


def store_image_in_s3(article, image_id) -> None:
    article_image_content = requests.get(article.image_url).content
    article_pil_image = prepare_preview_image(article_image_content)
    article_image_file = to_jpeg(article_pil_image)
    article_image_filename = f'{image_id}.jpeg'
    save_image_amazon_s3(article_image_file, article_image_filename)


def to_jpeg(pil_image: Image) -> BytesIO:
    jpeg_file = BytesIO()
    pil_image.save(jpeg_file, format="jpeg")
    return io.BytesIO(jpeg_file.getvalue())


def prepare_preview_image(article_image_content: bytes) -> Image:
    article_pil_image = to_pil_image(article_image_content)
    article_pil_image = remove_alpha_channel(article_pil_image)
    article_pil_image = article_pil_image.resize((500, 150))
    return article_pil_image


def to_pil_image(article_image_content):
    return Image.open(io.BytesIO(article_image_content))


def remove_alpha_channel(article_image: Image) -> Image:
    if article_image.mode in ("RGBA", "P"):
        article_image = article_image.convert('RGB')
    return article_image


def save_image_amazon_s3(article_image_file: io.BytesIO, article_image_filename: str) -> None:
    s3 = boto3.resource('s3',
                        aws_access_key_id=(os.environ['ACCESS_KEY']),
                        aws_secret_access_key=(os.environ['SECRET_KEY']))
    bucket = s3.Bucket(os.environ['ARTICLE_BUCKET_IMAGES'])
    bucket_object = bucket.Object(article_image_filename)
    bucket_object.upload_fileobj(article_image_file)