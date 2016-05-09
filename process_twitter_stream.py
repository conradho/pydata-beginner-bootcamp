import json

tweets_list = []
with open('datasets/twitter_data.txt', 'rb') as twitter_file:
    for line in twitter_file:
        if line == b'\n':
            continue
        try:
            tweet = json.loads(line.decode('utf-8'))
            if 'text' in tweet:
                tweets_list.append(tweet)
        except:
            print(line)
            raise

# let's see how many tweets we have
print(len(tweets_list))


import pickle
with open('datasets/twitter_data_2.pkl', 'wb') as pickle_file:
    pickle.dump(tweets_list, pickle_file)
