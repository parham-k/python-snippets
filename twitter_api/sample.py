from twitter_api.client import TwitterClient

if __name__ == '__main__':
    client = TwitterClient('random_redcoat')
    print('\n\n'.join(client.get_user_tweet_texts()))
