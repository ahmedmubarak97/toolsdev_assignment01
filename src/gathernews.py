import newspaper
import nltk
from newspaper import news_pool
#nltk.download('punkt')


def extract_article(article):
    article.download()
    article.parse()
    article.nlp()
    result = article.title + " - " + ", ".join(article.authors)
    result += "\n" + article.summary
    return result

articles_file = open('news_summary.txt', 'w')

keyword_input = input("Please enter a keyword and press enter: ")

def extract_articles(news_url, iscached=False):
    bna_news = newspaper.build(news_url, memoize_articles=iscached)
    for article in bna_news.articles:
        if keyword_input in article.keywords:
            extract = extract_article(article)
            print(extract + "\n")
            articles_file.write(article.title + " - " + str(article.authors) + "\n")
            articles_file.write(article.summary + "\n\n")
        else:
            extract = extract_article(article)
            print(extract + "\n")
            articles_file.write(article.title + " - " + str(article.authors) + "\n")
            articles_file.write(article.summary)


if __name__ == "__main__":
    news_sources = ['https://www.gamespot.com/','https://www.polygon.com/gaming']
    for news_url in news_sources:
        print(news_url)
        extract_articles(news_url)