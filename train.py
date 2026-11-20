"""Train a simple news headline classifier."""
import csv
from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

BASE_DIR = Path(__file__).resolve().parent


def main():
    with (BASE_DIR / "data" / "news.csv").open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    texts = [row["text"] for row in rows]
    categories = [row["category"] for row in rows]

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])
    model.fit(texts, categories)

    joblib.dump(model, BASE_DIR / "news_model.joblib")
    print(f"Trained on {len(texts)} example headlines.")
    print("Model saved as news_model.joblib")


if __name__ == "__main__":
    main()
