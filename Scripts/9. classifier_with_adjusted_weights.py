## The classifier with adjusted weights

def classifierweights(tweet):
    ft2 = contains_links(tweet["text"])
    ft4 = num_hashtags(tweet["text"])
    ft5 = count_number_nouns(tweet["text"])
    ft6 = count_number_verbs(tweet["text"])
    ft7 = count_tokens(tweet["text"])
    ft9 = num_first_person(tweet["text"])
    ft11 = num_uppercase(tweet["text"])
    ft12 = positive_scores(tweet["text"])
    ft15 = num_comma(tweet["text"])
    ft16 = num_period(tweet["text"])
    ft17 = num_question_mark(tweet["text"])
    ft18 = count_exl_marks(tweet["text"])
    ft19 = num_numeric(tweet["text"])
    distance_fm2 = abs(fm2 - ft2)
    distance_ff2 = abs(ff2 - ft2)
    distance_fm4 = abs(fm4 - ft4)
    distance_ff4 = abs(ff4 - ft4)
    distance_fm5 = abs(fm5 - ft5)
    distance_ff5 = abs(ff5 - ft5)
    distance_fm6 = abs(fm6 - ft6)
    distance_ff6 = abs(ff6 - ft6)
    distance_fm7 = abs(fm7 - ft7)
    distance_ff7 = abs(ff7 - ft7)
    distance_fm9 = abs(fm9 - ft9)
    distance_ff9 = abs(ff9 - ft9)
    distance_fm11 = abs(fm11 - ft11)
    distance_ff11 = abs(ff11 - ft11)
    distance_fm12 = abs(fm12 - ft12)
    distance_ff12 = abs(ff12 - ft12)
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

    total_distance_m = distance_fm2 + distance_fm4 + distance_fm5 + distance_fm6 + distance_fm7 + distance_fm9*50 + distance_fm11 + distance_fm12*10 + distance_fm15 + distance_fm16 + distance_fm17 + distance_fm18 + distance_fm19
    total_distance_f = distance_ff2 + distance_ff4 + distance_ff5 + distance_ff6 + distance_ff7 + distance_ff9*50 + distance_ff11 + distance_ff12*10 + distance_ff15 + distance_ff16 + distance_ff17 + distance_ff18 + distance_ff19

    if total_distance_m > total_distance_f:
        prediction = "female"
    if total_distance_f > total_distance_m:
        prediction = "male"

    return(prediction)
