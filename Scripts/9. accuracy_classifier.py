##Calculating accuracy of the classifier without weights

#creating csv files for calculating the accuracy (using classifier without weights and all features)

validation_prediction_noweights = "../../../../../../Desktop/validation_noweights_prediction.csv"
with open(validation_prediction_noweights, "w") as validation_noweights_outfile:
    fieldnames = ['text_tweet', 'gold', 'prediction']
    writer = csv.DictWriter(validation_noweights_outfile, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in validation_list:
        classification = classifier(dictionary)
        writer.writerow({'text_tweet': dictionary['text'], 'gold': dictionary['gender'], 'prediction': classification})

test_prediction_noweights = "../../../../../../Desktop/test_noweights_prediction.csv"
with open(test_prediction_noweights, "w") as test_noweights_outfile:
    fieldnames = ['text_tweet', 'gold', 'prediction']
    writer = csv.DictWriter(test_noweights_outfile, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in test_list:
        classification = classifier(dictionary)
        writer.writerow({'text_tweet': dictionary['text'], 'gold': dictionary['gender'], 'prediction': classification})
