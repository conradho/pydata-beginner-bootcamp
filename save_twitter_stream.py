
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 's6et82Yj5PXdDDeKT8ZFT6wi7'
consumer_secret = '0AO073w4xLHx9Dnf6EfU16dTGoNs04BEbiWEolDTbwN5GO5UPv'
access_token = '328841929-lMM9TKcKDodQpmWaQTarikw5DGFR5fW5jiveJuqW'
access_token_secret = '3RgPbhpkqQh7SlXVqLVMwQkmDo2NugzMeaCTDP4calwBz'

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'pydata', 'pydatalondon', 'datascience'])
