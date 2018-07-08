import tweepy, os
from dotenv import load_dotenv
from os.path import join, dirname

#パスの取得＆ロード（多分）
dotenv_path=join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


consumer_key=os.environ.get('CONSUMER_KEY')
consumer_secret=os.environ.get('CONSUMER_SECRET')
access_token=os.environ.get('ACCESS_TOKEN')
access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')

#認証情報を設定する
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

MyID=os.environ.get('MYACCOUNT')

def main():
    followers=api.followers(MyID)
    followerN=0
    for follower in followers:
        print ('@',follower.screen_name)
        followerN+=1
    print ('◆◇◆◇◆◇◆◇Followerは',followerN,'◆◇◆◇◆◇◆◇')
    
    followings=api.friends(MyID)
    followingN=0
    for following in followings:
        print(following.screen_name)
        followingN+=1
    print('◆◇◆◇◆◇◆◇Followingは',followingN,'◆◇◆◇◆◇◆◇')
    
    

if __name__=='__main__':
    main()