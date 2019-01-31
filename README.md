# Twitter user gender classification
Classification of tweets based on gender
### Lisa Markslag and Doortje Steketee
### 3rd of February 2019


#### Gender classification on twitter
The different usage of language by men and women is a widely discussed topic. Men and women have been found to use different forms of communication (Bamman, Eisenstein & Schnoebelen, 2012). Women have been found to prefer standard or "prestige" forms of language whereas men like to seem more "tough" or establish their local identity (Trudgill, 1972). Twitter is a communication platform where language use is restricted by the limited amount of characters that can go in a tweet (namely 140). With this classification project we want to see if the different language usage patterns of men and women can also be found in tweets. 

### Our dataset
Our dataset exists of 20.000 tweets, characterized by gender: male/female/brand/unknown. To start we took out all the brand and unknown, as we only want to analyse tweets written by male and female twitter users. This left around 13.000 tweets, which we split into a training(70%), validation(10%) and test(20%) set. The number of male tweets differed from the number of female tweets, therefore it was necessary to take 70%, 10% and 20% of male and female tweets seperately. 

### Splitting the data
In section X the data is manually seperated into a male and female training, validation and test set. The male and female sets are then combined to form the full training, validation and test set. From all the information (e.g. user ID, retweet count, profile description, text), only some information is relevant for the classification. We extracted gender, date/time created, retweet count and the tweet text as relevant information. 
