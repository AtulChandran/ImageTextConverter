from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    return snt


text="This is absolutely brilliant!! But can be terrible at times"
print("\n----------The text for sentiment analysis is \'",text,'\'----------\n')
print("The Positivity of the text is ",print_sentiment_scores(text)['pos']*100,"%")
print("\nThe Negativity of the text is ",print_sentiment_scores(text)['neg']*100,"%")
