from twitter_api.client import TwitterClient

if __name__ == '__main__':
    client = TwitterClient('random_redcoat')
    print(client.api.home_timeline())
