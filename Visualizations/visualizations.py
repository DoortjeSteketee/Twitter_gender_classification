import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import numpy as np

#Stacked bar graph showing tweets with and without exclamation marks
N = 2
tweets_without_excl = (3826, 4019)
tweets_with_excl = (509, 671)
fig1 = plt.figure()
ind = np.arange(N)
width = 0.5

p1 = plt.bar(ind,tweets_without_excl, width, color='#2276D2')
p2 = plt.bar(ind, tweets_with_excl, width, bottom = tweets_without_excl, color='#F0A01D')

plt.ylabel('Number of tweets')
plt.title('Number of tweets without and with exclamation marks')
plt.xticks(ind,('Male', 'Female'))
plt.yticks(np.arange(0, 6500, 500))
plt.legend((p1[0], p2[0]), ('Tweets without exclamation mark', 'Tweets with exclamation mark'))
plt.show()

fig1.savefig('Exclamation_Marks')

#Bar graph showing tweets with different number of exclamation marks M/F
n_groups = 6
tweets_male = (7.7, 2.5, 1.0, 0.2, 0.1, 0.1)
tweets_female = (8.9, 3.3, 0.9, 0.7, 0.3, 0.1)
fig2 = plt.figure()

fig2, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.9

rects1 = plt.bar(index, tweets_male, bar_width, alpha=opacity, color='#2276D2', label='Male')
rects2 = plt.bar(index + bar_width, tweets_female, bar_width, alpha=opacity, color='#F0A01D', label='Female')

plt.xlabel('Number of exclamation marks')
plt.ylabel('Number of tweets (%)')
plt.title('Percentage of tweets with number of exclamation marks')
plt.xticks(index +bar_width, ('1!', '2!', '3!', '4!', '5!', '6!'))
plt.legend()

plt.tight_layout()
plt.show()

fig2.savefig('%Exclamation_marks')

#Pie chart males showing tweets with and without link
labels = 'Without link', 'With link'
sizes = [2967, 1368]
colors = ['#2276D2', '#F0A01D']
explode = (0, 0.05)
fig3 = plt.figure()

fig3, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.title('Male tweets with and without link')

plt.show()
fig3.savefig('pie_male_links')

#Pie chart females showing tweets with and without link
labels = 'Without link', 'With link'
sizes = [3325, 1365]
colors = ['#2276D2', '#F0A01D']
explode = (0, 0.05)
fig4 = plt.figure()

fig4, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.title('Female tweets with and without link')

plt.show()
fig4.savefig('pie_female_links')

#Bar graph showing the use of first person expressions
n_groups = 6
tweets_male = (37.8, 8.8, 5.6, 8.9, 2.0, 1.2)
tweets_female = (48.9, 13.3, 9.9, 15.0, 3.2, 1.8)
fig5 = plt.figure()

fig5, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.9

rects1 = plt.bar(index, tweets_male, bar_width, alpha=opacity, color='#2276D2', label='Male')
rects2 = plt.bar(index + bar_width, tweets_female, bar_width, alpha=opacity, color='#F0A01D', label='Female')

plt.xlabel('First person singular expressions')
plt.ylabel('Number of tweets (%)')
plt.title('Male/female comparison of the use of first person singular expressions')
plt.xticks(index +bar_width, ('I', "I'm", 'me', 'my', 'I have', 'I am'))
plt.legend()

plt.tight_layout()
plt.show()

fig5.savefig('Singular_expressions')

#Stacked bar graph showing average nouns&verbs used per tweet
N = 2
tweets_nouns = (3.2, 3.2)
tweets_verbs = (3.6, 3.8)
ind = np.arange(N)
width = 0.5
fig6 = plt.figure()

p1 = plt.bar(ind,tweets_nouns, width, color='#2276D2')
p2 = plt.bar(ind, tweets_verbs, width, bottom = tweets_nouns, color='#F0A01D')

plt.ylabel('Average number of nouns and verbs per tweet')
plt.title('Average use of nouns and verbs per tweet for male and female')
plt.xticks(ind,('Male', 'Female'))
plt.yticks(np.arange(0, 10, 1))
plt.legend((p1[0], p2[0]), ('Average nouns', 'Average verbs'))
plt.show()
fig6.savefig('Nouns_verbs')
