##Creating list of dictionaries
##Containing only relevant information for data processing
###Gender, date/time created, retweet count and text

#Creating a list of dictionaries, only with the relevant information (for training).

updated_training_list = []
updated_validation_list = []

for dictionary in training_list:
    dict_tweets = {}
    for column_name, value in dictionary.items():
        if column_name in ['gender', 'text', 'retweet_count', 'created']:
            dict_tweets[column_name] = value
    updated_training_list.append(dict_tweets)

for dictionary in validation_list:
    validation_tweet_dicts = {}
    for column_name, value in dictionary.items():
        if column_name in ['gender', 'text', 'retweet_count', 'created']:
            validation_tweet_dicts[column_name] = value
    updated_validation_list.append(validation_tweet_dicts)
