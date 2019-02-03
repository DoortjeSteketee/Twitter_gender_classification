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


#creating csv files for calculating the accuracy (using classifier with weights and 13 features)

validation_prediction_weights = "../../../../../../Desktop/validation_weights_prediction.csv"
with open(validation_prediction_weights, "w") as validation_weights_outfile:
    fieldnames = ['text_tweet', 'gold', 'prediction']
    writer = csv.DictWriter(validation_weights_outfile, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in validation_list:
        classification = classifierweights(dictionary)
        writer.writerow({'text_tweet': dictionary['text'], 'gold': dictionary['gender'], 'prediction': classification})

test_prediction_weights = "../../../../../../Desktop/test_weights_prediction.csv"
with open(test_prediction_weights, "w") as test_weights_outfile:
    fieldnames = ['text_tweet', 'gold', 'prediction']
    writer = csv.DictWriter(test_weights_outfile, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in test_list:
        classification = classifierweights(dictionary)
        writer.writerow({'text_tweet': dictionary['text'], 'gold': dictionary['gender'], 'prediction': classification})
