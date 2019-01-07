#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM


# In[3]:


#fetch data and format it
data = fetch_movielens(min_rating = 4.0)

#print training testing dta
print(repr(data['train']))
print(repr(data['test']))

#create model
model = LightFM(loss='warp')

#train model
model.fit(data['traind'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
    
    #number of users and movies in training data
    n_users, n_items = data['train'].shape
    
    #generate recommendations fro each user we input
    for user_id in user_ids:
        
        #movies they already like
        known_positives = data['item_labels'][data['train'].tocrs()[user_id].indices]
        
        #movies our model predicts they will like
        scores = model.predict(user_id, np.arrange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]
        
        #print out the results
        print("User %s" % user_id)
        print("         Known positives:")
        
        for x in known_positives[:3]:
            print("         %s" % x)
            
        print("      Recommended:")
        
        for x in top_items[:3]:
            print("           %s" % x)
            
sample_recommendation(model, data, [3, 25, 450])


# In[ ]:




