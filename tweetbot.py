from twython import Twython, TwythonError
import datetime

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

twitter_client.update_status(status='https://giphy.com/gifs/rIq6ASPIqo2k0')
