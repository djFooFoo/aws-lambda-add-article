from dataclasses import dataclass

import newspaper
import nltk


@dataclass
class Article:
    url: str
    title: str
    publication_date: str
    category: str
    introduction: str


def get_article(article_url) -> Article:
    nltk.download('punkt')
    article = newspaper.Article(url=article_url)
    article.build()
    return Article(
        url=article.url,
        title=article.title,
        publication_date=str(article.publish_date)[:10],
        category='Other',
        introduction=article.meta_description
    )