import tweepy
import json
import time
import codecs
import io

class StreamListener(tweepy.StreamListener):
    tweetNumber = 5000 #number of tweet to retrieve
    counter = 1
    def on_status(self, tweet):
        print "------------------"
        
    def on_error(self, status_code):
        print "Error: " + repr(status_code)
        return False

    def on_data(self, data):
        if (self.counter <= self.tweetNumber):
            try:
                d = json.loads(data)
                print "tweet number: "+str(self.counter)
                with io.open(str(time.strftime("%d-%m-%Y"))+".json",'a',encoding='utf-8') as f:
                    f.write(unicode(json.dumps(d, ensure_ascii=False))+"\n")                         
                self. counter += 1
                time.sleep(1)
                return True
            except BaseException as e:
                print("Error on data: %s" % str(e))
                pass
            return True
        else:
            return False
        
    def on_timeout(self):
        print "Time out: not information on time limit..."
        return False

while(True):
    try:
        #english tokens
        consumer_key = "rLAOjdPYAcCQPBdRXSlk"
        consumer_secret = "mCmiEV33SDnV0CW4oNAjkfgOFnL8T0dRUTQnZCpKndjh"
        access_token_key = "2472721027-S4YUze8TZyN1IGR7u81SyqEek6JD46wCyOuc"
        access_token_secret = "DZ126dV3TvGtltqvDnxENTOkUhfrfVqonCz8ya"

        auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth1.set_access_token(access_token_key, access_token_secret)
        setTerms =["china"]
        l = StreamListener()
        streamer = tweepy.Stream(auth=auth1, listener=l, timeout=60)
        streamer.filter(track = setTerms,languages=["en"])
    except BaseException as e:
        print("Error on data: %s" % str(e))
        pass
