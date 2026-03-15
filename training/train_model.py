import pickle
from pathlib import Path

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# Simple training dataset
reviews = [
    # Positive
    "I love this product",
    "This is amazing",
    "Very good quality",
    "Excellent experience",
    "I am very satisfied",
    "Fast delivery and great service",
    "Absolutely fantastic",
    "I recommend it",
    "Works perfectly",
    "Really happy with this purchase",

    # Negative
    "I hate this product",
    "This is terrible",
    "Very bad quality",
    "Awful experience",
    "I am very disappointed",
    "Slow delivery and poor service",
    "Absolutely horrible",
    "I do not recommend it",
    "Works badly",
    "Really unhappy with this purchase",

    # Neutral
    "The product arrived yesterday",
    "It works as expected",
    "The package was delivered",
    "This is a product",
    "The item is available",
    "The service was okay",
    "The quality is average",
    "It does what it should",
    "Nothing special about this product",
    "The experience was normal"
]

labels = [
    # Positive
    "positive","positive","positive","positive","positive",
    "positive","positive","positive","positive","positive",

    # Negative
    "negative","negative","negative","negative","negative",
    "negative","negative","negative","negative","negative",

    # Neutral
    "neutral","neutral","neutral","neutral","neutral",
    "neutral","neutral","neutral","neutral","neutral"
]


# Split dataset for basic evaluation
X_train, X_test, y_train, y_test = train_test_split(
    reviews,
    labels,
    test_size=0.2,
    random_state=42
)


# Text classification pipeline
pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])


# Train model
pipeline.fit(X_train, y_train)


# Evaluate model
predictions = pipeline.predict(X_test)

print("\nModel evaluation:")
print(classification_report(y_test, predictions))


# Ensure model directory exists
model_dir = Path("model")
model_dir.mkdir(exist_ok=True)


# Save trained model
output_path = model_dir / "sentimentanalysismodel.pkl"

with open(output_path, "wb") as f:
    pickle.dump(pipeline, f)


print(f"\nModel trained and saved to: {output_path}")