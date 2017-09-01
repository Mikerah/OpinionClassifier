import pymongo
import nltk

# Retrieve New York Times articles database and collection
client = pymongo.MongoClient()
nyt_database = client['nyt']
all_articles_collection = nyt_database['articles']

# Check all the types of articles in the articles collection
print(all_articles_collection.distinct('type'))

# Combine types such as 'Sunday Review' into single type Opinion
modified_collection_result = all_articles_collection.update_many(
    {'type':'Sunday Review', 'type':'Book Review', 'type':'Public Editor'}, 
    {'$set': {'type': 'Opinion'}})

# Combine repeat types into one type
# movies and Movie
modified_collection_result = all_articles_collection.update_many({'type':'movies'}, {'$set':{'type':'Movies'}})

# Arts & Design and Arts
modified_collection_result = all_articles_collection.update_many({'type':'Arts & Design'}, {'$set': {'type':'Arts'}})

# Personal Tech and Technology
modified_collection_result = all_articles_collection.update_many({'type': 'Personal Tech'}, {'$set': {'type':'Technology'}})

# Combine types such as 'Soccer' and 'Baseball' into type Sports
modified_collection_result = all_articles_collection.update_many(
{'type': 'Soccer', 'type': 'Baseball', 'type':'Hockey', 'type': 'Golf', 'type':'Olympics', 'type':'College Football'
'type': 'Pro Football', 'type':'Pro Basketball', 'type': 'College Basketball', 'type' : 'sports'},
{'$set': {'type': 'Sports'}})

# 

# Count the number of opinion articles and news articles