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
# twitter_client.update_status(status='Hello twitter!')

# api_url = 'https://api.twitter.com/1.1/lists/members.json?list_id=1'
# constructed_url = twitter_client.construct_api_url(api_url, q='python', result_type='popular')
# print(constructed_url)
# https://api.twitter.com/1.1/search/tweets.json?q=python&result_type=popular

# jsonStr = twitter_client.get_list_members('Friends', 'Otto Bot')
#
# print(jsonStr)

# twitter_client.update_status(status='Say Hello to my maker @miguelparis !')


# twitter = Twython()
# followers = twitter_client.get_followers_ids(screen_name='elBot93')
#
# print(followers)
# for ids in followers:
#     print('User with ID %d is following elBot93' % follower_id)


# search_results = twitter_client.search(q="infobarreras", count=3)
#
#
# try:
#     for tweet in search_results["statuses"]:
#         twitter_client.retweet(id = tweet["id_str"])
#         # print(tweet["id_str"])
# except TwythonError as e:
#     print(e)

# Creating an empty list for our followers
followers = []

# Getting today's date
datestamp = datetime.datetime.now().strftime("%Y-%m-%d")

# Asking for the username to get their followers
username = 'miguelparis'

# This is to go through paginated results
next_cursor = -1

while next_cursor:
    # Getting the user's followers
    get_followers = twitter_client.get_followers_list(screen_name=username, count=10, cursor=next_cursor)
    # For each user returned from our get_followers
    for follower in get_followers["users"]:
        # Add their screen name to our followers list
        followers.append(follower["screen_name"].encode("utf-8"))
        next_cursor = get_followers["next_cursor"]

# Create or open a new .txt file
followers_text = open(username + "-" + datestamp + ".txt", "a")

# Write the first "title" line and followers list to the .txt
# Should all be one (very long) line:
followers_text.write(followers.__str__())

followers_text.close()
