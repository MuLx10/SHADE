from twitterscraper import query_tweets 
import datetime as dt
import Watson
import re
import json

def get_tweets(user):
    ed = dt.date.today()
    bd = ed - dt.timedelta(days=1)
    tweets = query_tweets(user,limit=20,begindate=bd)
    if not tweets:
        bd = ed - dt.timedelta(days=20)
        tweets = query_tweets(user,limit=20,begindate=bd)
        if not tweets:
            return ["\n"]
    # return [str(i.text).replace('\\','') for i in tweets]
    return  [re.sub('[^A-Za-z0-9#@ .,$&(){}[]]+', ' ', str(i.text)) for i in tweets]




def get_mood(user):
    tweets = get_tweets(user)
    moods = ["anger","fear","joy","sadness","analytical","confident","tentative"]
    score = {i:0 for i in moods}
    if not tweets:
        return score

    for tweet in tweets:
        mood_json = Watson.get_tone_json(tweet)
        mood_json = json.loads(mood_json)
        line = mood_json['result']['document_tone']
        for tone in line['tones']:
            score[tone['tone_id']] += tone['score']
    
    # print score
    return score


if __name__ == '__main__':
    print (get_mood('Twitter'))