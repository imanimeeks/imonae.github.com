import json

# using json library, open file
tweetFile = open("../TwitterData/tweets_small.json", "r")

# load file to new variable
tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id: ",tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])

# shortcut
for idx in tweetData:
    print("Tweet text: " + tweet["text"])

# other way
for idx in range(len(tweetdata)):
    print("Tweet text: " + tweeDatat[idx]["text"])
