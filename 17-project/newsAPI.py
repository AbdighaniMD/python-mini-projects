#install: "pip install newsapi-python"

from newsapi import NewsApiClient

# Init
api_key= "" #'API_KEY'
newsapi = NewsApiClient(api_key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin', category='business', language='en')

dt = top_headlines['articles']

for x,y in enumerate(dt):
    print(f'{x} {y["description"]}')



#print(top_headlines)