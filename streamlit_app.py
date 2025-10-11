import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
nltk.download('vader_lexicon')

st.set_page_config(layout="wide")
st.title("Social Media Sentiment Dashboard")

df = pd.read_csv("data/tweets_sample.csv", parse_dates=['date'])

def simple_clean(t):
    import re
    t = str(t).lower()
    t = re.sub(r'http\S+|www\S+|https\S+', '', t)
    t = re.sub(r'@\w+', '', t)
    t = re.sub(r'#','',t)
    t = re.sub(r'[^a-z0-9\s]','',t)
    return t

df['clean_text'] = df['text'].apply(simple_clean)
sia = SentimentIntensityAnalyzer()
df['sentiment_score'] = df['clean_text'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment'] = df['sentiment_score'].apply(lambda s: 'positive' if s>0.05 else ('negative' if s<-0.05 else 'neutral'))

# Metrics
st.metric("Total tweets", len(df))
st.metric("Positive %", f"{(df['sentiment']=='positive').mean()*100:.1f}%")
st.metric("Negative %", f"{(df['sentiment']=='negative').mean()*100:.1f}%")

# Charts
st.subheader("Sentiment distribution")
st.bar_chart(df['sentiment'].value_counts())

st.subheader("Average sentiment over time")
daily = df.groupby(df['date'].dt.date)['sentiment_score'].mean()
st.line_chart(daily)

st.subheader("Wordcloud")
text = " ".join(df['clean_text'].astype(str))
wc = WordCloud(width=800, height=300, background_color='white').generate(text)
fig, ax = plt.subplots(figsize=(10,4))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

st.subheader("Sample tweets")
st.dataframe(df[['date','username','text','sentiment']].head(50))
