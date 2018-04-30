from twython import Twython, TwythonStreamer

# Opens file with name of "key.txt", which has all the
# necessary Keys and Tokens to access the Bot Twitter Account
file = open('key.txt', 'r', encoding='utf8')

# Reads each line.
# The file only contains four lines stored in plain text, no commas and the end
API_KEY = str(file.readline().strip())
API_SECRET = str(file.readline().strip())
ACCESS_TOKEN = str(file.readline().strip())
ACCESS_TOKEN_SECRET = str(file.readline().strip())

file.close()

# Using Twython to handle the Twitter API
twitter_client = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        #if 'text' in data:
            #print(data['text'])
        if 'direct_message' in data:
            msg = data['direct_message']
            print(msg['text'].encode('utf-8'))

    def on_error(self, status_code, data):
        print(status_code)
        self.disconnect()


stream = MyStreamer(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream.statuses.filter(track='message')