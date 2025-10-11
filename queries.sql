-- Create a table to store tweets and sentiment scores
CREATE TABLE tweets_sentiment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tweet_text TEXT,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    created_at DATETIME
);

-- Insert sample data (replace with Python-inserted data)
INSERT INTO tweets_sentiment (tweet_text, sentiment_label, sentiment_score, created_at)
VALUES
('I love this product!', 'Positive', 0.85, NOW()),
('This is terrible service', 'Negative', -0.65, NOW()),
('It is okay, nothing special', 'Neutral', 0.05, NOW());

-- Count how many tweets fall into each sentiment
SELECT sentiment_label, COUNT(*) AS tweet_count
FROM tweets_sentiment
GROUP BY sentiment_label;

-- Get the top 10 most positive tweets
SELECT tweet_text, sentiment_score
FROM tweets_sentiment
WHERE sentiment_label = 'Positive'
ORDER BY sentiment_score DESC
LIMIT 10;

-- Get the top 10 most negative tweets
SELECT tweet_text, sentiment_score
FROM tweets_sentiment
WHERE sentiment_label = 'Negative'
ORDER BY sentiment_score ASC
LIMIT 10;

-- Sentiment trend over time (daily counts)
SELECT DATE(created_at) AS day, sentiment_label, COUNT(*) AS tweet_count
FROM tweets_sentiment
GROUP BY DATE(created_at), sentiment_label
ORDER BY day;

-- Average sentiment score by day
SELECT DATE(created_at) AS day, AVG(sentiment_score) AS avg_sentiment
FROM tweets_sentiment
GROUP BY DATE(created_at)
ORDER BY day;