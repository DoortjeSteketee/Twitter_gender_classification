# Twitter user gender classification
Classification of tweets based on gender
### Lisa Markslag and Doortje Steketee
#### 3rd of February 2019

### Table of contents
* [General info](#general-info)
* [Explanation of the dataset](#Our-dataset)

#### General info
The different usage of language by men and women is a widely discussed topic. Men and women have been found to use different forms of communication (Bamman, Eisenstein & Schnoebelen, 2012). Women have been found to prefer standard or "prestige" forms of language whereas men like to seem more "tough" or establish their local identity (Trudgill, 1972). Twitter is a communication platform where language use is restricted by the limited amount of characters that can go in a tweet (namely 140). With this classification project we want to see if the different language usage patterns of men and women can also be found in tweets. 

### Our dataset
Our dataset exists of 20.000 tweets, characterized by gender: male/female/brand/unknown. To start we took out all the brand and unknown, as we only want to analyse tweets written by male and female twitter users. This left around 13.000 tweets, which we split into a training(70%), validation(10%) and test(20%) set. The number of male tweets differed from the number of female tweets, therefore it was necessary to take 70%, 10% and 20% of male and female tweets seperately. 

### Splitting the data
In section X the data is manually seperated into a male and female training, validation and test set. The male and female sets are then combined to form the full training, validation and test set. From all the information (e.g. user ID, retweet count, profile description, text), only some information is relevant for the classification. We extracted:
* gender 
* date/time created
* retweet count
* tweet text 

The data is stored in a list of dictionaries (called updated_training_list), every dictionary being a tweet that has the 4 extracted elements as keys and the corresponding values. 

### Processing the data
To analyze the text written in the tweets we used spaCy to tokenize and perform part-of-speech tagging as can be seen in section X. For this step you will need to download and import spacy):

``` 
import spacy
nlp = spacy.load('en')
```
We chose not the lemmatize the text as the tweets are extremely short. By lemmatizing we could lose relevant information by making the tweets even shorter than they already are. By leaving the tweets as they are, we could focus on lexical variation more. We specifically looked at first person expressions such as 'I'm' and 'I am'. The lemma for 'I'm' and 'I am' is 'be', therefore lemmatizing these expressions would condense the lexical variation. 

### Finding relevant features
Section X contains functions for finding the relevant features in our tweets. All the functions have a comment and a docstring defining what the function does. The features we're looking at can be divided into the following categories: 
* Punctuation
* Extra-linguistic features
* Linguistic features
* Sentiment features

The first couple of functions look at features such as punctuation (e.g. exclamation marks, commas and use of symbols). The next functions look at extra-linguistic features such as symbols that have a specific function on Twitter (e.g. '#' and '@'). Functions after that look at linguistic features, that analyse the text on a deeper level. These functions require tokenization and pos-tagging, so as to count the number of verbs and nouns. Finally, the last functions look at sentiment in the tweets. For this we used the VADER sentiment intesity analyzer. This shows the positive, negative and neutral sentiment of a tweet. For this last step you need to import nltk and the vader lexicon:

```
import nltk
nltk.downloader.download('vader_lexicon')
from spacy.tokens import Doc
from nltk.sentiment.vader import SentimentIntensityAnalyzer
```

We calculated differences between male and female, which can be found in the visualization python file. 

### Finding the relevant features in the training set
All the information from the relevant features needs to be stored in a csv-file which can be seen in section X. From the updated_training_list we can extract the text for the corresponding tweet and perform every function seperately. 

### Building a classifier
From the csv-file built in section X, we can calculate the total number of found features seperately for male and female. However, because the total amount of tweets is different for male and female, we need to calculate the average amount of found features (relative to the total amount of tweets). So the steps for every function are the following: 
* Count total amount of tweets (using a counter)
* Count number of features for male and female seperately (with the correct function for that feature) (also using a counter)
* Divide number of found features by total amount of tweets - this gives the average amount of found features for male and female. 

These average amount of found features is essential for building the classifier, as it is the gold label for the tweet. 
The classifier will look at a tweet of which the gender is unknown, count the number of specific features and compare it to this gold label. The classifier will then predict the gender based on the gold label. 
For example, if the average amount of exclamation marks used by males is 1 and females is 3. If the classifier then sees a tweet that contains 3 exclamation marks, it will predict the tweet to be written by a female. 

