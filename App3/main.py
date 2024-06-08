import requests
from send_email import send_email

topic = 'tesla'
url = 'https://newsapi.org/v2/everything?' \
      f'q={topic}&from=2024-05-07&sortBy=' \
      'publishedAt&' \
      'apiKey=837d5e2250fb41f8921149c13656df70&' \
      'language=en' \

api_key = '837d5e2250fb41f8921149c13656df70'

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
body = "Subject: Today's news\n\n"
for article in content["articles"][:20]:
    title = article.get("title", "No Title")
    description = article.get("description", "No Description")
    url = article.get("url", "No URL")
    if title:
        body += f"{title}\n{description}\n{url}\n\n"

body = body.encode('utf-8')
send_email(message=body)