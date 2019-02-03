##Building the classifier
def classifier(tweet):
    ft1 = count_reply_tweet(tweet["text"])
    ft2 = contains_links(tweet["text"])
    ft3 = contains_smiley(tweet["text"])
    ft4 = num_hashtags(tweet["text"])
    ft5 = count_number_nouns(tweet["text"])
    ft6 = count_number_verbs(tweet["text"])
    ft7 = count_tokens(tweet["text"])
    ft8 = num_like(tweet["text"])
    ft9 = num_first_person(tweet["text"])
    ft10 = num_lowercase(tweet["text"])
    ft11 = num_uppercase(tweet["text"])
    ft12 = positive_scores(tweet["text"])
    ft13 = negative_scores(tweet["text"])
    ft14 = neutral_scores(tweet["text"])
    ft15 = num_comma(tweet["text"])
    ft16 = num_period(tweet["text"])
    ft17 = num_question_mark(tweet["text"])
    ft18 = count_exl_marks(tweet["text"])
    ft19 = num_numeric(tweet["text"])
    ft20 = count_symbols(tweet["text"])
    distance_fm1 = abs(fm1 - ft1)
    distance_ff1 = abs(ff1 - ft1)
    distance_fm2 = abs(fm2 - ft2)
    distance_ff2 = abs(ff2 - ft2)
    distance_fm3 = abs(fm3 - ft3)
    distance_ff3 = abs(ff3 - ft3)
    distance_fm4 = abs(fm4 - ft4)
    distance_ff4 = abs(ff4 - ft4)
    distance_fm5 = abs(fm5 - ft5)
    distance_ff5 = abs(ff5 - ft5)
    distance_fm6 = abs(fm6 - ft6)
    distance_ff6 = abs(ff6 - ft6)
    distance_fm7 = abs(fm7 - ft7)
    distance_ff7 = abs(ff7 - ft7)
    distance_fm8 = abs(fm8 - ft8)
    distance_ff8 = abs(ff8 - ft8)
    distance_fm9 = abs(fm9 - ft9)
    distance_ff9 = abs(ff9 - ft9)
    distance_fm10 = abs(fm10 - ft10)
    distance_ff10 = abs(ff10 - ft10)
    distance_fm11 = abs(fm11 - ft11)
    distance_ff11 = abs(ff11 - ft11)
    distance_fm12 = abs(fm12 - ft12)
    distance_ff12 = abs(ff12 - ft12)
    distance_fm13 = abs(fm13 - ft13)
    distance_ff13 = abs(ff13 - ft13)
    distance_fm14 = abs(fm14 - ft14)
    distance_ff14 = abs(ff14 - ft14)
    distance_fm15 = abs(fm15 - ft15)
    distance_ff15 = abs(ff15 - ft15)
    distance_fm16 = abs(fm16 - ft16)
    distance_ff16 = abs(ff16 - ft16)
    distance_fm17 = abs(fm17 - ft17)
    distance_ff17 = abs(ff17 - ft17)
    distance_fm18 = abs(fm18 - ft18)
    distance_ff18 = abs(ff18 - ft18)
    distance_fm19 = abs(fm19 - ft19)
    distance_ff19 = abs(ff19 - ft19)
    distance_fm20 = abs(fm20 - ft20)
    distance_ff20 = abs(ff20 - ft20)

    total_distance_m = distance_fm1 + distance_fm2 + distance_fm3 + distance_fm4 + distance_fm5 + distance_fm6 + distance_fm7 + distance_fm8 + distance_fm9 + distance_fm10 + distance_fm11 + distance_fm12 + distance_fm13 + distance_fm14 + distance_fm15 + distance_fm16 + distance_fm17 + distance_fm18 + distance_fm19 + distance_fm20
    total_distance_f = distance_ff1 + distance_ff2 + distance_ff3 + distance_ff4 + distance_ff5 + distance_ff6 + distance_ff7 + distance_ff8 + distance_ff9 + distance_ff10 + distance_ff11 + distance_ff12 + distance_ff13 + distance_ff14 + distance_ff15 + distance_ff16 + distance_ff17 + distance_ff18 + distance_ff19 + distance_ff20

    if total_distance_m > total_distance_f:
        prediction = "female"
    if total_distance_f > total_distance_m:
        prediction = "male"

    return(prediction)