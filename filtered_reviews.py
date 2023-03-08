import json
import csv
from collections import defaultdict
import numpy as np
import pandas as pd

# Load the business IDs from the CSV file
business_ids = set()
print("loading selected restaraunts from csv")
with open('restaurants.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        business_ids.add(row['business_id'])

# Filter the Yelp reviews by business ID
reviews = []
print("filtering reviews of restaurants out of all reviews")
with open('yelp_academic_dataset_review.json', 'r') as json_file:
    for line in json_file:
        review = json.loads(line)
        if review['business_id'] in business_ids:
            reviews.append(review)

# Write the filtered reviews to a new JSON file
print("file written")
with open('filtered_reviews.json', 'w') as json_file:
    for review in reviews:
        json.dump(review, json_file)
        json_file.write('\n')

# Code to aggregate reviews by date for the restaurants
# Using readlines()
print("reading filtered json")
file1 = open("filtered_reviews.json", 'r')
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

pd.DataFrame(average_review_by_date, columns=['date', 'avg_review']).to_csv("restaurant_avg_reviews_by_date.csv")
