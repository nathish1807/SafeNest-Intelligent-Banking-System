import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("N:/Code warriors/data/transactions.csv")

X = df[["amount"]]
y = df["fraud"]

model = RandomForestClassifier()
model.fit(X, y)


def detect_fraud(amount):

    prediction = model.predict([[amount]])

    if prediction[0] == 1:
        return "⚠ Fraud Risk Detected"
    else:
        return "Transaction Safe"