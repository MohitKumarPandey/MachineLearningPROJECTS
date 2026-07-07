import pandas as pd
import numpy as np
import os

def create_dataset():
    np.random.seed(42)

    data = {
        "respondent_id": range(1, 201),
        "age_group": np.random.choice(["18-25", "26-35", "36-50"], 200),
        "region": np.random.choice(["North", "South", "East", "West"], 200),
        "question": "Preferred Product",
        "response": np.random.choice(["Product A", "Product B", "Product C"], 200),
        "date": pd.date_range(start="2024-01-01", periods=200)
    }

    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/poll_data.csv", index=False)

    return df

def load_data():
    return pd.read_csv("data/poll_data.csv")