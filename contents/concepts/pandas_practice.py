import pandas as pd


data = pd.read_csv("data/twitter_data/Tweets.csv")
data = data.head(10)

# Select all rows in df where airline_sentiment is neutral and airline_sentiment_confidence is less than 1.
data_one = data[(data['airline_sentiment'] == 'neutral') & (data['airline_sentiment_confidence'] < 1.000)]
print(data_one)

# Select required qualumn based on condition
data_two = data[(data['airline_sentiment'] == 'neutral') & (data['airline_sentiment_confidence'] < 1.000)][['tweet_id', 'airline_sentiment']]
print(data_two)
