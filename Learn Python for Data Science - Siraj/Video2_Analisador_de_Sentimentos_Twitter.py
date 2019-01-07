#!/usr/bin/env python
# coding: utf-8

# In[2]:


from textblob import TextBlob
import tweepy


# In[3]:


consumer_key = 'FijGtP5JdS57nycbuMWX0gv18'
consumer_secret = 'rjjqCIqOaCn9xMZNM0fnyR1Ez6G0QyflM0HSp6POa6ZcyZGDCt'

access_token = '1082066159321649154-XfC2bxnBqmbl6ijfowFtWDe45hYsIy'
access_token_secret = 'allADuNFAVvhPQNCzS8HwYWdcGSGJFv2oyYCbrj2V0BOJ'


# In[4]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


# In[5]:


auth.set_access_token(access_token, access_token_secret)


# In[6]:


api = tweepy.API(auth)


# In[15]:


public_tweets = api.search('Karen')


# In[16]:


for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


# In[ ]:




