"""
This file contains all the code I ran in the python shell to clean the database
"""

import pymongo

# Retrieve New York Times articles database and collection
client = pymongo.MongoClient()
nyt_database = client['nyt']
all_articles_collection = nyt_database['articles']

# Check all the types of articles in the articles collection
print(all_articles_collection.distinct('type'))

# Find the number of opinion articles
print(all_articles_collection.)

# Combine types such as 'Sunday Review' into single type Opinion
modified_collection_result = all_articles_collection.update_many(
    {'type':'sunday-review'}, 
    {'$set': {'type': 'opinion'}})

modified_collection_result = all_articles_collection.update_many(
    {'type': 'public-editor'},
    {'$set': {'type': 'opinion'}})
    
# Remove 'We’re interested in your feedback on this page'
for i in all_articles_collection.find({}):
    new_text = i['text'].replace("We’re interested in your feedback on this page.","")
    all_articles_collection.update_one(i,{'$set':{'text': new_text}})
    
# Remove 'A version of this article ...'
for i in all_articles_collection.find({}):
    if 'A version of this article appears in print on' in i['text']:
        beginning_index = i['text'].find('A version of this article appears in print on')
        collection.update_one(i,{'$set':{'text':i['text'][:beginning_index]}})
        
# Remove Non-English articles from collection
all_articles_collection.delete_many({'type':'universal'})