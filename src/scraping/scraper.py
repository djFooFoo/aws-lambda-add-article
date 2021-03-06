from dataclasses import dataclass

import newspaper


@dataclass
class Article:
    url: str
    title: str
    publication_date: str
    category: str
    introduction: str
    image_url: str


def get_article(article_url) -> Article:
    article = newspaper.Article(url=article_url)
    article.build()
    return Article(
        url=article.url,
        title=article.title,
        publication_date=str(article.publish_date)[:10],
        category='Other',
        introduction=article.meta_description,
        image_url=article.top_image
    )
