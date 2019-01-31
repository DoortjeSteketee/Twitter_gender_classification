##Functions to find classification features
##Below function is distance number in classifier. Order is different based on saliency of features

##Punctuation and numbers

def num_comma(text_tweet):
    """Counting the number of comma's in a tweet"""
    num_comma = text_tweet.count(',')
    return(num_comma)
#num_comma = 15

def num_period(text_tweet):
    """Counting the number of periods in a tweet"""
    num_period = text_tweet.count('.')
    return(num_period)
#num_period = 16

def num_question_mark(text_tweet):
    """Counting the number of question marks in a tweet"""
    num_question_mark = text_tweet.count('?')
    return(num_question_mark)
#num_question_mark = 17

def num_lowercase(text_tweet):
    """Counting the number of lowercase letters in a tweet"""
    num_lowercase = sum(1 for c in text_tweet if c.islower())
    return(num_lowercase)
#num_lowercase = 10

def num_uppercase(text_tweet):
    """Counting the number of uppercase letters in a tweet"""
    num_uppercase = sum(1 for c in text_tweet if c.isupper())
    return(num_uppercase)
#num_uppercase = 11

def num_numeric(text_tweet):
    """Counting the number of numeric characters in a tweet"""
    num_numeric = sum(1 for c in text_tweet if c.isnumeric())
    return(num_numeric)
#num_numeric = 19

def count_symbols(text_tweet):
    """Counting the amount of symbols in a tweet"""
    import string
    import collections as ct
    special_chars = string.punctuation
    num_symbols = sum(v for k, v in ct.Counter(text_tweet).items() if k in special_chars)
    return(num_symbols)
#count_symbols = 20

def count_exl_marks(text_tweet):
    """Counting exclamation marks in a tweet"""
    count_exl_mark = text_tweet.count("!")
    return(count_exl_mark)
#count_exl_marks = 18


##Extra-linguistic features

def count_reply_tweet(text_tweet):
    """Counting the amount of times an author replies to someone using '@'"""
    count_reply = text_tweet.count('@')
    return(count_reply)
#count_reply_tweet = 1

def contains_links(text_tweet):
    """Determining if a tweet contains a link"""
    if "https:" in text_tweet:
        contains_link = 1
    if "https:" not in text_tweet:
        contains_link = 0
    return(contains_link)
#contains_link = 2 

def contains_smiley(text_tweet):
    """Determining if a tweet contains a happy smiley"""
    if " :) " in text_tweet:
        contains_smiley = 1
    if " :) " not in text_tweet:
        contains_smiley = 0
    return(contains_smiley)
#contains_smiley = 3

##Linguistic features

def count_number_verbs(text_tweet):
    """Counting the number of verbs in a tweet"""
    doc = nlp(text_tweet)
    pos_tags = []
    for token in doc:
        pos_tag = token.pos_
        pos_tags.append(pos_tag)
    count_verbs = pos_tags.count("VERB")
    return(count_verbs)
#count_number_verbs = 6

def count_number_nouns(text_tweet):
    """Counting the number of nouns in a tweet"""
    doc = nlp(text_tweet)
    pos_tags = []
    for token in doc:
        pos_tag = token.pos_
        pos_tags.append(pos_tag)
    count_nouns = pos_tags.count("NOUN")
    return(count_nouns)
#count_number_nouns = 5

def count_tokens(text_tweet):
    """Counting the amount of tokens (words) in a tweet"""
    doc = nlp(text_tweet)
    num_tokens = len(doc)
    return(num_tokens)
#count_tokens = 7

def num_like(text_tweet):
    """Counting the amount of times the author uses the word 'like'"""
    number_likes = text_tweet.count(" like ") + text_tweet.count(" Like ") + text_tweet.count("Like ")
    return(number_likes)
#num_like = 8

def num_first_person(text_tweet):
    """Counting the number of first person singular expressions"""
    num_I = text_tweet.count("I ") + text_tweet.count(" I ") + text_tweet.count(" i ")
    num_my = text_tweet.count("My ") + text_tweet.count(" My ") + text_tweet.count(" my ") + text_tweet.count("my ")
    num_Im = text_tweet.count(" I'm ") + text_tweet.count("I'm ") + text_tweet.count(" Im ") + text_tweet.count(" i'm ") + text_tweet.count(" im ")
    num_Ihave = text_tweet.count(" I have ") + text_tweet.count("I have ") + text_tweet.count(" I Have ") + text_tweet.count("I Have ")
    num_me = text_tweet.count(" me ") + text_tweet.count(" Me ") + text_tweet.count("Me ")
    num_Iam = text_tweet.count(" I am ") + text_tweet.count("I am ")
    num_first_person = num_I + num_my + num_Im + num_Ihave + num_me + num_Iam
    return(num_first_person)
#num_first_person = 9

##Sentiment features

def positive_scores(text_tweet):
    """Measuring the positive sentiment of a text in a tweet"""
    doc=nlp(text_tweet)
    doc.set_extension('polarity_scores', getter=polarity_scores, force=True)
    polarity_score = doc._.polarity_scores
    polarity_scores(doc)
    return(polarity_score["pos"])
#positive_scores = 12


def negative_scores(text_tweet):
    """Measuring the negative sentiment of a text in a tweet"""
    doc=nlp(text_tweet)
    doc.set_extension('polarity_scores', getter=polarity_scores, force=True)
    polarity_score = doc._.polarity_scores
    polarity_scores(doc)
    return(polarity_score["neg"])
#negative_scores = 13

def neutral_scores(text_tweet):
    """Measuring the neutral sentiment of a text in a tweet"""
    doc=nlp(text_tweet)
    doc.set_extension('polarity_scores', getter=polarity_scores, force=True)
    polarity_score = doc._.polarity_scores
    polarity_scores(doc)
    return(polarity_score["neu"])
#neutral_scores = 14
