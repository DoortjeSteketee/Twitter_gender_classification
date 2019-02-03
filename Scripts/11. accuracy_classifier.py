#opening the csvs and calculating the accuracy of the classifier while looking at different sets

with open("../../../../../../Desktop/validation_noweights_prediction.csv") as csvfile3:
    prediction_reader = csv.DictReader(csvfile3, delimiter=',', quotechar='"')
    prediction_dicts = [dict(d) for d in prediction_reader]

with open("../../../../../../Desktop/test_noweights_prediction.csv") as csvfile4:
    prediction_reader_2 = csv.DictReader(csvfile4, delimiter=',', quotechar='"')
    prediction_dicts_2 = [dict(d) for d in prediction_reader_2]

with open("../../../../../../Desktop/validation_weights_prediction.csv") as csvfile5:
    prediction_reader_3 = csv.DictReader(csvfile5, delimiter=',', quotechar='"')
    prediction_dicts_3 = [dict(d) for d in prediction_reader_3]

with open("../../../../../../Desktop/test_weights_prediction.csv") as csvfile6:
    prediction_reader_4 = csv.DictReader(csvfile6, delimiter=',', quotechar='"')
    prediction_dicts_4 = [dict(d) for d in prediction_reader_4]

def accuracy(list_of_tweets):
    correct_count = 0
    total_count = len(list_of_tweets)
    for tweet in list_of_tweets:
        if tweet['gold'] == tweet['prediction']:
            correct_count += 1
    accuracy = correct_count/total_count*100
    return(accuracy)

print("The accuracy of the classifier with all (20) features and without weights on the validation set is:", accuracy(prediction_dicts), "\nThe accuracy of the classifier with all (20) features and without weights on the test set is:", accuracy(prediction_dicts_2), "\nThe accuracy of the classifier with only 13 features and with weights on feature 9 and 12 on the validation set is:", accuracy(prediction_dicts_3), "\nThe accuracy of the classifier with only 13 features and with weights on feature 9 and 12 on the test set is:", accuracy(prediction_dicts_4))
