#Storing the training data as csv

outfilename = "../../../../../../Desktop/training_set_features.csv"
with open(outfilename, "w") as outfile:
    fieldnames = ['gender', 'created', 'retweet_count', 'text', 'num_exclamation', 'num_tokens', 'num_replys', 'contains_link', 'num_verbs', 'num_nouns', 'neg_score', 'pos_score', 'neu_score', 'num_commas', 'num_period', 'num_question_mark', 'num_upper', 'num_lower', 'num_num', 'contains_smiley', 'num_likes', 'num_first_person', 'num_hashtags', 'num_symbols']
    writer = csv.DictWriter(outfile, fieldnames = fieldnames)
    writer.writeheader()
    for dictionary in updated_training_list:
        exl_count = count_exl_marks(dictionary["text"])
        token_count = count_tokens(dictionary["text"])
        reply_count = count_reply_tweet(dictionary["text"])
        link_container = contains_links(dictionary["text"])
        verb_count = count_number_verbs(dictionary["text"])
        noun_count = count_number_nouns(dictionary["text"])
        neg_score = negative_scores(dictionary["text"])
        pos_score = positive_scores(dictionary["text"])
        neu_score = neutral_scores(dictionary["text"])
        comma_count = num_comma(dictionary["text"])
        period_count = num_period(dictionary["text"])
        question_count = num_question_mark(dictionary["text"])
        uppercase_count = num_uppercase(dictionary["text"])
        lowercase_count = num_lowercase(dictionary["text"])
        num_count = num_numeric(dictionary["text"])
        smiley_container = contains_smiley(dictionary["text"])
        like_count = num_like(dictionary["text"])
        first_person_count = num_first_person(dictionary["text"])
        hashtag_count = num_hashtags(dictionary["text"])
        symbol_count = count_symbols(dictionary["text"])
        writer.writerow({'gender': dictionary['gender'], 'created': dictionary['created'], 'retweet_count': dictionary['retweet_count'], 'text': dictionary["text"], 'num_exclamation': exl_count, 'num_tokens': token_count, 'num_replys': reply_count, 'contains_link': link_container, 'num_verbs': verb_count, 'num_nouns': noun_count, 'neg_score': neg_score, 'pos_score': pos_score, 'neu_score': neu_score, 'num_commas': comma_count, 'num_period': period_count, 'num_question_mark': question_count, 'num_upper': uppercase_count, 'num_num': num_count, 'contains_smiley': smiley_container, 'num_likes': like_count, 'num_first_person': first_person_count, 'num_hashtags': hashtag_count, 'num_lower': lowercase_count, 'num_symbols': symbol_count})

#Opening the training data
        
with open("../../../../../../Desktop/training_set_features.csv") as csvfile2:
    tweet_reader_2 = csv.DictReader(csvfile2, delimiter=',', quotechar='"')
    tweet_dicts_2 = [dict(d) for d in tweet_reader_2]
