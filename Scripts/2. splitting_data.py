##Splitting data into a training, validation and test dataset_with_all_genders

training_list_male = male_tweet_dicts[0:4335]
training_list_female = female_tweet_dicts[0:4690]
training_list = training_list_male + training_list_female

validation_list_male = male_tweet_dicts[4336:4955]
validation_list_female = female_tweet_dicts[4690:5360]
validation_list = validation_list_male + validation_list_female

test_list_male = male_tweet_dicts[4956:6194]
test_list_female = female_tweet_dicts[5361:6700]
test_list = test_list_male + test_list_female
