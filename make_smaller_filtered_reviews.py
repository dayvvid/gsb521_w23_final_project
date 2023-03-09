import json
from collections import defaultdict
import numpy as np
import pandas as pd

b_pandas = []
r_dtypes = {"stars": np.float16,
            "useful": np.int32,
            "funny": np.int32,
            "cool": np.int32,
            }
with open("/Users/evanroth/Desktop/yelp_dataset/filtered_reviews.json", "r") as f:
    reader = pd.read_json(f, orient="records", lines=True,
                          dtype=r_dtypes, chunksize=1000)

    for chunk in reader:
        reduced_chunk = chunk.drop(columns=['review_id', 'user_id', 'text', 'useful','funny','cool'])
        b_pandas.append(reduced_chunk)

b_pandas = pd.concat(b_pandas, ignore_index=True)

b_pandas = b_pandas[b_pandas['date'] >= pd.to_datetime('2018-01-01')]

b_pandas.to_csv("filtered_reviews.csv")