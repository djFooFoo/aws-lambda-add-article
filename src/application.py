from images import image_service
from scraping import scraper


def handler(event, context):
    latest_article_url = 'https://medium.com/p/700b430bc204'
    article = scraper.get_article(latest_article_url)
    image_id = image_service.store_article_metadata_in_database(article)
    image_service.store_image_in_s3(article, image_id)

    return {"statusCode": 200, "body": image_id}


if __name__ == "__main__":
    print(handler(None, None))
