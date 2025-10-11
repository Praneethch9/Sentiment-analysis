# Sentiment Analysis Project

This project demonstrates how to perform sentiment analysis using Python, SQL, and Tableau.  
We analyze text data, preprocess it, perform sentiment classification, and finally visualize the insights.

---

## Technologies Used
- Python → Data preprocessing, sentiment analysis, and word clouds  
- SQL → Storing, retrieving, and aggregating sentiment data  
- Tableau → Dashboard for visualization  

---

## Project Structure
project/
│── notebooks/ # Jupyter notebooks for analysis
│── dashboards/ # Tableau and Python-generated visuals
│ └── Sentiment_Analysis.png
│── queries/ # SQL queries
│ └── queries.sql
│── README.md # Documentation


---

## Python Work
1. Clean and preprocess text (NLTK stopwords, tokenization).  
2. Perform sentiment analysis using VADER.  
3. Generate word clouds for positive, negative, and neutral sentiments.  

---

## SQL Work
SQL is used to store and query sentiment results. Example queries are in [`queries/queries.sql`](queries/queries.sql).

Example query: Count reviews by sentiment  
```sql
SELECT sentiment, COUNT(*) AS total_reviews
FROM reviews
GROUP BY sentiment;

Tableau Dashboard

We built a Tableau dashboard to visualize sentiment distribution and trends.

Dashboard snapshot:
![Sentiment Dashboard](dashboards/Sentiment_Analysis.png)
