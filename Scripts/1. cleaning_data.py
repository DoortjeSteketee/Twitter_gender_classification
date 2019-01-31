import csv
with open("dataset_with_all_genders.csv", "r", encoding='utf8', errors='ignore') as csvfile:
    tweet_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    tweet_dicts = [dict(d) for d in tweet_reader]

male_tweets_count = 0
female_tweets_count = 0

male_tweet_dicts = []
female_tweet_dicts = []

for item in tweet_dicts:
    if item['gender'] == 'male':
        male_tweets_count += 1
        male_tweet_dicts.append(item)
    if item['gender'] == 'female':
        female_tweets_count += 1
        female_tweet_dicts.append(item)
