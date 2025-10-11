# Social Media Sentiment Analysis

## Overview
Analyze public sentiment around a topic or brand using social media text. Demonstrates NLP, EDA, visualization, and a simple dashboard with Streamlit.

## Files
- `data/tweets_sample.csv` — sample data (replace with your collection)
- `notebooks/sentiment_analysis.ipynb` — analysis & plots
- `streamlit_app.py` — interactive dashboard
- `dashboards/` — exported images/screenshots
- `requirements.txt` — Python dependencies

## How to run
1. Create & activate virtualenv.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the notebook or:
```bash
python notebooks/sentiment_analysis.py
streamlit run streamlit_app.py
```

## Methodology
1. Collect tweets (sample CSV / snscrape / Twitter API).
2. Clean text: remove URLs, mentions, punctuation; lowercase; optional stopword removal.
3. Analyze sentiment using VADER — compute compound score and classify into positive, neutral, negative.
4. Explore & visualize: distribution, trend over time, word clouds, top hashtags.
5. Present results in an interactive dashboard.

## Contact
Your Name — email@example.com
