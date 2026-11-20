# Basic News Classification Pipeline

A small beginner-friendly Python project that predicts whether a news headline is about **World**, **Sports**, **Business**, or **Sci/Tech**.

## How it works

1. Read example headlines from `data/news.csv`.
2. Convert the words into numbers using TF-IDF.
3. Train a Logistic Regression classifier.
4. Save the trained model.
5. Enter a new headline to predict its category.

## Files

```text
pipelining/
├── data/
│   └── news.csv
├── train.py
├── predict.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run it

Install Python 3.10 or newer, then open a terminal in this folder.

```bash
python -m pip install -r requirements.txt
python train.py
python predict.py
```

On some computers, use `python3` instead of `python`.

Example input:

```text
Enter a news headline: The football team won the match
Predicted category: Sports
```

Type `quit` to exit.

## Add your own examples

Open `data/news.csv` and add more rows with two columns: `text` and `category`. Use one of the four existing categories, then run `python train.py` again.

## Limitations

This project uses only 40 hand-written sample headlines. It is meant to demonstrate a simple machine learning pipeline, **not** to give reliable predictions on real-world news. For better results, use a larger labeled dataset.

## Tools used

Python, scikit-learn, TF-IDF, Logistic Regression, and joblib.
