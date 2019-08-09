import json
from textblob import TextBlob
import matplotlib.pyplot as plt
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarityList = []
subjectivityList = []

for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    polarityList.append(tweetblob.polarity)
    subjectivityList.append(tweetblob.subjectivity)

print(polarityList[0])
print(subjectivityList[0])

print()
print("polarityList")
print(polarityList)
print()
print("subjectivityList")
print(subjectivityList)


plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])

plt.xlabel("polarity")
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

plt.plot(polarityList, subjectivityList, "ro")
plt.xlabel('polarities')
plt.ylabel('subjectivity')
plt.title('Tweet Polarity vs subjectivity')
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()

import matplotlib
import matplotlib.pyplot as fill
import numpy as np
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = fill.subplots()
ax.fill(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
