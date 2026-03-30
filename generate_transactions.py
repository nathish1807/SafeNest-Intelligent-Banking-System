import pandas as pd
import random

data = []

for i in range(1000):
    amount = random.randint(100,50000)

    fraud = 0
    if amount > 40000:
        fraud = 1

    data.append({
        "transaction_id": i,
        "amount": amount,
        "location": random.choice(["India","USA","UK","Singapore"]),
        "fraud": fraud
    })

df = pd.DataFrame(data)

df.to_csv("transactions.csv",index=False)

print("Dataset Created")