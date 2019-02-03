# Twitter user gender classification
Classification of tweets based on gender
### Lisa Markslag and Doortje Steketee
### l.markslag@student.vu.nl / d.steketee@student.vu.nl
#### 3rd of February 2019

### Table of contents
* [General info](#general-info)
* [How to use the code](#How-to-use-the-code)
* [Explanation of the dataset](#Our-dataset)
* [Splitting the data](#Splitting-the-data)
* [Processing the data](#Processing-the-data)
* [Finding relevant features](#Finding-relevant-features)
* [Implementation on the training set](#Implementation-on-the-training-set)
* [Building the classifier](#Building-the-classifier)
* [Calculating the accuracy](#Calculating-the-accuracy)

### General info
The different usage of language by men and women is a widely discussed topic. Men and women have been found to use different forms of communication (Bamman, Eisenstein & Schnoebelen, 2012). Women have been found to prefer standard or "prestige" forms of language whereas men like to seem more "tough" or establish their local identity (Trudgill, 1972). Twitter is a communication platform where language use is restricted by the limited amount of characters that can go in a tweet (namely 140). With this classification project we want to see if the different language usage patterns of men and women can also be found in tweets. By analysing tweets (comparing their structure with specific features and the corresponding gender of the author) we will build a classifier. When the classifier is given a tweet with an unknown gender, it will predict if it is written by a male or a female twitter user. 

### How to use the code
In the folder 'Data', all the relevant sets can be found. This folder also contains sets with intermediate results such as the training data with all the relevant features that will later be used to build the classifier. In the folder 'Scripts' all the relevant scripts can be found in the correct order (1 - 11) as will be explained in this ReadMe file. The scripts have a number and a title. The mainscript contains all these scripts but in one large file. Every chunk has the title above it with the corresponding .py script number. In the folder 'visualizations' there is one file containing all the graphs and the specific codes for these graphs. The .py script can be run to obtain and save these figures. 

### Our dataset
Our dataset, from Kaggle.com (filename: gender-classifier-DFE-791531), exists of 20.000 tweets, characterized by gender: male/female/brand/unknown. To start we "cleaned the data" and took out all the brand and unknown (see script 1: cleaning_data.py), as we only want to analyse tweets written by male and female twitter users. This left around 13.000 tweets, which we split into a training(70%), validation(10%) and test(20%) set. The number of male tweets differed from the number of female tweets, therefore it was necessary to take 70%, 10% and 20% of male and female tweets seperately. 

### Splitting the data
In script 2 (splitting_data.py) the data is manually seperated into a male and female training, validation and test set. The male and female sets are then combined to form the full training, validation and test set. From all the information (e.g. user ID, retweet count, profile description, text), only some information is relevant for the classification. We extracted:
* gender 
* date/time created
* retweet count
* tweet text 

This can be found in script 4 (processing_data.py). The data is stored in a list of dictionaries (called updated_training_list - can be found in the data folder), every dictionary being a tweet that has the 4 extracted elements as keys and the corresponding values. Before being able to do this, you need to run script 3 to download all the different packages. 
These sets, with the relevant information, need to be stored in a csv-file. This can be done using script 5 (saving_datasets.py)

### Processing the data
To analyze the text written in the tweets we used spaCy (download from script 3) to tokenize and perform part-of-speech tagging as can be seen in script 6, where tokenization and pos-tagging can be seen in separate functions (run script 3 before this):

``` 
import spacy
nlp = spacy.load('en')
```
We chose not the lemmatize the text as the tweets are extremely short. By lemmatizing we could lose relevant information by making the tweets even shorter than they already are. By leaving the tweets as they are, we could focus on lexical variation more. We specifically looked at first person expressions such as 'I'm' and 'I am'. The lemma for 'I'm' and 'I am' is 'be', therefore lemmatizing these expressions would condense the lexical variation. 

### Finding relevant features
Script 6 contains functions for finding the relevant features in our tweets. All the functions have a comment and a docstring defining what the function does. The features we're looking at can be divided into the following categories: 
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

### Implementation on the training set
All the information from the relevant features needs to be stored in a csv-file which can be seen in script 7 (storing_and_opening_training_data.py). From the updated_training_list we can extract the text for the corresponding tweet and perform every function seperately. 

### Building the classifier
From the csv-file built in script 7, we can calculate the total number of found features seperately for male and female. However, because the total amount of tweets is different for male and female, we need to calculate the average amount of found features (relative to the total amount of tweets). So the steps for every function are the following: 
* Count total amount of tweets (using a counter)
* Count number of features for male and female seperately (with the correct function for that feature, also using a counter)
* Divide number of found instances per feature by total amount of tweets (also for both male and female) - this gives the average amount of instances per feature for male and female. Male feature averages are indicated by "fmx", in which "f" stands for "feature", "m" stands for "male" and "x" stands for the number that particular feature has. Female averages are indicated by "ffx", in which the first "f" stands for "feature", the second "f" for "female" and the "x" again stands for the number that particular feature has. This can clearly be seen in script 8 (the_classifier.py).

These average amount of found features is essential for building the classifier, as it is the gold label for the tweet. 
The classifier will look at a tweet of which the gender is unknown and compare it to this gold label. It does so through calculating the sum of the distances between the feature averages (fmx and ffx) and the feature numbers of the test tweet (ftx), in which "t" stands for "test"). Whichever gender's accumulative distance is the smallest compared to the test tweet, will be predicted. For example: the average amount of exclamation marks used by males is 1 and females is 3. If the classifier then sees a tweet that contains 3 exclamation marks, it will see the distance betwen the test tweet and the average features is smaller compared to the female average than the male average. The classifier will then predict the tweet to be written by a female. This has its downsides: due to the lack of data, some features that might have an impact on the training set, might not have that similar impact on the test set. The test set is only around 1000 tweets, which makes it highly susceptible to small data discrepancies. Many features do not bring anything to the table because of this, and only bring the accuracy of the classifier down. To test the features and their impact on the accuracy, we started by first implementing all our features and giving them equal weights (see script 8). Then, we tested whether the accuracy would go up or down by removing certain features or giving them certain weights. By doing this, we created a classifier that was (however slightly) more accurate. The classifier that includes only relevant features and has specified weights can be found in script 9 (classifier_with_adjusted_weights.py). 

### Calculating the Accuracy
For calculating the accuracy, we wrote a function that looks at a csv-file, checks how many gold labels are the same as the prediction labels, and calculates the accuracy. First you need to save the classifier outcomes in a csv-file, which can be found in script 10 (creating_csv_accuracy.py). Then, in script 11 (accuracy_classifier.py) calculated the accuracy from the information stored in script 10.
The accuracy of our classfier by using all features without any weights, is 53.1% for the validation set and 57.7% for the test set, both above baseline level (50%). By adjusting weights and removing unnecessary features, we managed to get an accuracy for the validation set that was alightly higher: 54.5%. Unfortunately, when testing this on the test set, the accuracy went down to 55.7%. It is therefore safe to say that there is probably simply a problem with the lack of data.


