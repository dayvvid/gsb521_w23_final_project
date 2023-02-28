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
with open("/Users/evanroth/Desktop/yelp_dataset/yelp_academic_dataset_review.json", "r") as f:
    reader = pd.read_json(f, orient="records", lines=True,
                          dtype=r_dtypes, chunksize=1000)

    for chunk in reader:
        reduced_chunk = chunk.drop(columns=['review_id', 'user_id', 'text', 'useful','funny','cool'])
        b_pandas.append(reduced_chunk)

b_pandas = pd.concat(b_pandas, ignore_index=True)

# Group the rows by year and business_id, and calculate the average rating for each group
df_grouped = b_pandas.groupby([b_pandas['date'].dt.year, 'business_id']).mean().reset_index()

# Rename the columns to be more descriptive
df_grouped = df_grouped.rename(columns={'date': 'year'})

# Select only the rows where the year is 2019 or 2022
df_selected = df_grouped[df_grouped['year'].isin([2019, 2022])]

df_selected.to_csv("reviews.csv")
#print(df_selected)
