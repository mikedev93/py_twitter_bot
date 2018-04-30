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

# Creating an empty list for our desired list
followers = []

# Asking for the username to get their followers
username = 'elBot93'

# This is to go through paginated results
next_cursor = -1

while next_cursor:
    # Getting the user's followers
    get_list = twitter_client.get_list_members(list_id=1)
    # For each user returned from our get_followers
    for follower in get_list["users"]:
        # Add their screen name to our followers list
        followers.append(follower["id"].encode("utf-8"))
        next_cursor = get_list["next_cursor"]

# Create or open a new .txt file
followers_text = open(username + "-" + datestamp + ".txt", "a")

# Write the first "title" line and followers list to the .txt
# Should all be one (very long) line:
followers_text.write(followers.__str__())

followers_text.close()