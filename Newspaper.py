'Newspaper Module to scrap news'
from newspaper import article


url =https://www.cnn.com/2023/09/03/us/georgia-police-killing-teen-dog/index.html

my_article = Article(url,Lanuage="en")
my_article.download()


