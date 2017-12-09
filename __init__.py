import praw
from random import *

reddit = praw.Reddit(client_id='d8CjJ9jTyd-O7g',
                     client_secret='rQGOcfA5u7jIz8_AVvJRw5xWCEc',
                     password='Toystory2wasok',
                     user_agent='realmp7 by /u/57northisok',
                     username='57northisok')



sports = ['sports','nba','nfl','theocho','baseball','soccer','cfb']
news = ['news','worldnews','TrueReddit','UpliftingNews','politics','geopolitics']
science = ['science','technology','space','economics','math','environment','chemistry']
funfacts = ['todayilearned','funfacts','DataIsBeautiful','facts','offbeat','nottheonion']
entertainment = ['television','movies','Documentaries','books','quotes','comics','Music','listentothis','Art', 'gaming', 'games']
stories = ['creepy','LetsNotMeet','casualconversation','TalesFromRetail','IAmA','talesfromtechsupport','AskReddit']
lifestyle = ['LifeProTips','GetMotivated','productivity','personalfinance','DIY','YouShouldKnow','malefashionadvice','femalefashionadvice']
health = ['fitness','cooking','running','EatCheapAndHealthy','health']

choices = {'sports':sports,'news':news,'science':science,'funfacts':funfacts,'entertainment':entertainment,
           'stories':stories,'lifestyle':lifestyle,'health':health}

def pick_sub(topics):
    sub = sample(topics, 1)[0]
    for key in choices:
        if sub == key:
            return returnTop(sample(choices[key],1)[0])


def returnTop(subreddit):
    return reddit.subreddit(subreddit).top('day').next().url