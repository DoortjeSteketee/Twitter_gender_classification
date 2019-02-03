#saving training set as csv
training_set = "training_set.csv"
with open(training_set, "w") as outfile_training:
    fieldnames = ['gender', 'created', 'retweet_count', 'text']
    writer = csv.DictWriter(outfile_training, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in updated_training_list:
        writer.writerow({'gender': dictionary['gender'], 'created': dictionary['created'], 'retweet_count': dictionary['retweet_count'], 'text': dictionary['text']})

#saving validation set as csv
validation_set = "validation_set.csv"
with open(validation_set, "w") as outfile_validation:
    fieldnames = ['gender', 'created', 'retweet_count', 'text']
    writer = csv.DictWriter(outfile_validation, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in updated_validation_list:
        writer.writerow({'gender': dictionary['gender'], 'created': dictionary['created'], 'retweet_count': dictionary['retweet_count'], 'text': dictionary['text']})

#saving test set as csv
test_set = "test_set.csv"
with open(test_set, "w") as outfile_test:
    fieldnames = ['gender', 'created', 'retweet_count', 'text']
    writer = csv.DictWriter(outfile_test, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in updated_test_list:
        writer.writerow({'gender': dictionary['gender'], 'created': dictionary['created'], 'retweet_count': dictionary['retweet_count'], 'text': dictionary['text']})
        
