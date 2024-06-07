import requests

url = 'https://newsapi.org/v2/everything?q=tesla&from=' \
      '2024-05-06&sortBy=publishedAt&apiKey=837d5e2250fb41f8921149c13656df70'

api_key = '837d5e2250fb41f8921149c13656df70'

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])