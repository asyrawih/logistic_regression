import json
import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import pipeline
import pickle


def gen_dataset():
    with open("./models/conversession.json") as file:
        anotations_msg = []
        model = json.load(file)
        # extract model
        for conversation in model["conversations"]:
            for msg in conversation["messages"]:
                anotations_msg.append(
                    {"label": msg["sender"], "message": msg["message"]}
                )


# Export annotations to CSV
    csv_columns = ["label", "message"]
    csv_file = "annotations.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for annotation in anotations_msg:
            writer.writerow(annotation)

    print("Annotations exported to:", csv_file)


def train_model():
    """
    train dataset with Logistic Regression
    and will exported as models
    """
    # load csv and create dataframe
    df = pd.read_csv("./annotations.csv")
    message = df["message"].apply(lambda x: x.lower())
    labels = df["label"]

    # split train model
    X_train, X_test, Y_train, Y_test = train_test_split(
        message, labels, test_size=0.2)

    # vectorize
    vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char')

    pipe = pipeline.Pipeline([('vectorizer', vectorizer),
                              ('clf', LogisticRegression())])

    pipe.fit(X_train, Y_train)

    y_pred = pipe.predict(X_test)

    acc = accuracy_score(Y_test, y_pred)
    print("Accuracy:", acc)

    with open("logistic_regression_model.pkl", "wb") as f:
        pickle.dump(pipe, f)


train_model()
