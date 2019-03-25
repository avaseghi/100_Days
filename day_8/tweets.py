import twitter
api = twitter.Api(consumer_key="IdrA8DJSswgeDi60GwPtt55sU",
      consumer_secret="ePbNAA46GiL3AYFKyjRQkibMGnWX4y5oFMSFdZBUSbyOWiAnXy",
      access_token_key="1094817230217531392-cDA8JL6iiiHah2sohP9bNJy19gBxPr",
      access_token_secret="W3Fl44VpEmWYvLl905rDHFk9N0EZglj03lp1VxFi12Fyg")

def get_tweets(screen_name):

    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    for tweet in timeline:
        if "@" not in tweet.text and "https" not in tweet.text:
            print(tweet.text)

get_tweets("@sosadtoday")
