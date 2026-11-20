"""Predict the category of a news headline."""
from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parent / "news_model.joblib"


def main():
    if not MODEL_PATH.exists():
        print("Model not found. Run: python train.py")
        return

    model = joblib.load(MODEL_PATH)
    print("News classifier (type 'quit' to exit)")
    while True:
        headline = input("Enter a news headline: ").strip()
        if headline.lower() == "quit":
            break
        if not headline:
            print("Please enter a headline.")
            continue
        print("Predicted category:", model.predict([headline])[0])


if __name__ == "__main__":
    main()
