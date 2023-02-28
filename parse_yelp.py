import json
from collections import defaultdict
import numpy as np
import pandas as pd

# Using readlines()
file1 = open("/Users/evanroth/Desktop/yelp_dataset/yelp_academic_dataset_review.json", 'r')
Lines = file1.readlines()

count = 0

reviews_by_date = defaultdict(list)

print("parsing file")
# Strips the newline character
for line in Lines:
    count += 1
    review = json.loads(line)
    date = review['date'].split(' ')[0]
    reviews_by_date[date].append(review['stars'])

average_review_by_date = []
print("computing means")
for key, value in reviews_by_date.items():
    average_review_by_date.append([key, np.mean(value)])

pd.DataFrame(average_review_by_date, columns=['date', 'avg_review']).to_csv("avg_reviews_by_date.csv")
