from twython import Twython
import giphy_client
from giphy_client.rest import ApiException
from random import randint

# set the apikey and limit
file = open('gif_key.txt', 'r', encoding='utf8')

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = str(file.readline().strip())
file.close()
# str | Search query term or phrase.
q = 'piano'

# int | The maximum number of records to return. (optional) (default to 25)
limit = 25

# int | An optional results offset. Defaults to 0. (optional) (default to 0)
offset = 0

# str | Filters results by specified rating. (optional)
rating = 'g'

# str | Specify default country for regional content; use a 2-letter ISO 639-1 country code.
lang = 'es'

# str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
fmt = 'json'

# str | Initiating the variable.
selected_gif = ''

try:
    # Search Endpoint
    api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)

    data = api_response.data
    data_len = len(data)
    # Generate a random number to pick a random gif
    gif_number = randint(0, limit - 1)

    for item in range(data_len):
        if item == gif_number:
            gif = data[item]
            print('We found the GIF! The number is ' + item.__str__())
            selected_gif = str(gif.url)
            print(str(gif.url))

except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


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

twitter_client.update_status(status=selected_gif)
